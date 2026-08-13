from __future__ import annotations

import asyncio
from typing import Any

from src.tutto_api_client.helpers.http import HTTPRequest


class AsyncJobPoller:
    """Handles polling and waiting for asynchronous background tasks to complete."""

    def __init__(
        self,
        http_client: HTTPRequest,
        poll_interval: float = 2.0,
        timeout: float = 300.0,
    ) -> None:
        """
        Args:
            http_client: Instance of HTTPRequest used to dispatch status checks.
            poll_interval: Delay in seconds between polling requests.
            timeout: Maximum allowed time in seconds before raising a TimeoutError.
        """
        self.http_client = http_client
        self.poll_interval = poll_interval
        self.timeout = timeout

    async def poll_until_finished(
        self,
        verification_url: str,
        headers: dict | None = None,
        timeout: float | None = None,
    ) -> Any:
        """Polls the `verification_url` via GET requests until the status becomes 'finished'.

        Args:
            verification_url: Endpoint or full URL to poll for job completion status.
            headers: Optional HTTP headers (e.g. authorization) to send on each poll.
            timeout: Optional override for the configured timeout, in seconds.

        Returns:
            The contents of the 'results' key from the response dictionary.

        Raises:
            RuntimeError: If the job status reports 'failed' or 'error'.
            TimeoutError: If the task does not finish within the configured timeout window.
        """
        # Falls back to the instance default when no override is provided
        effective_timeout = timeout if timeout is not None else self.timeout
        start_time = asyncio.get_running_loop().time()

        while True:
            # Perform a GET request to the verification endpoint
            response = await self.http_client.request(
                endpoint=verification_url,
                method="get",
                headers=headers,
            )

            status = response.get("process").get("status")

            if status == "finished":
                return response.get("process").get("result")
            elif status in ("failed", "error"):
                raise RuntimeError(
                    f"Async job failed with status '{status}'. Payload: {response}"
                )

            # Check timeout condition
            elapsed = asyncio.get_running_loop().time() - start_time
            if elapsed >= effective_timeout:
                raise TimeoutError(
                    f"Job polling timed out after waiting for {elapsed:.1f} seconds."
                )

            await asyncio.sleep(self.poll_interval)
