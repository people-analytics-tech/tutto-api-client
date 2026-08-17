from __future__ import annotations

from typing import Any, Literal

from tutto_api_client.helpers.http import HTTPRequest
from tutto_api_client.helpers.job_pooler import AsyncJobPoller


class APIClient:
    """High-level facade client orchestrating HTTP requests and async polling behavior."""

    def __init__(self, base_url: str) -> None:
        self.http = HTTPRequest(base_url=base_url)
        self.poller = AsyncJobPoller(http_client=self.http)

    async def fetch_data(
        self,
        endpoint: str,
        method: Literal["get", "post", "put", "patch", "delete"] = "get",
        is_async: bool = False,
        headers: dict | None = None,
        parameters: dict | None = None,
        timeout: float | None = None,
        **kwargs: Any,
    ) -> dict:
        """Executes an HTTP request and automatically manages async job polling if enabled.

        Args:
            endpoint: Target API endpoint.
            method: HTTP method to perform.
            is_async: If True, appends 'async=true' query parameter and polls 'verification_url'.
            headers: Optional HTTP headers dictionary.
            parameters: Optional query parameters dictionary.
            timeout: Optional override for the async job polling timeout, in seconds.
            **kwargs: Extra arguments passed to the HTTP request (e.g., json, data).

        Returns:
            The raw JSON response dict, or the extracted 'results' dict if polled asynchronously.
        """
        # Copy parameter dict to prevent mutating the caller's reference
        params = parameters.copy() if parameters else {}

        if is_async:
            params["async"] = "true"

        response = await self.http.request(
            endpoint=endpoint,
            method=method,
            headers=headers,
            parameters=params,
            **kwargs,
        )

        # If async mode was requested and a verification URL exists, initiate polling
        if is_async and "verification_url" in response:
            verification_url = response["verification_url"]
            return await self.poller.poll_until_finished(
                verification_url, headers=headers, timeout=timeout
            )

        return response
