from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal
from urllib.parse import urljoin

import aiohttp


@dataclass(init=True, frozen=True)
class HTTPRequest:
    """Class to handle requests to an API."""

    base_url: str = field(init=True)

    async def request(
        self,
        endpoint: str,
        method: Literal["get", "post", "put", "patch", "delete"],
        headers: dict | None = None,
        parameters: dict | None = None,
        data: Any = None,
        json: Any = None,
    ) -> dict:
        request_url = urljoin(base=self.base_url, url=endpoint)
        headers = headers or {}
        parameters = parameters or {}

        async with (
            aiohttp.ClientSession() as session,
            session.request(
                method=method.upper(),
                url=request_url,
                headers=headers,
                params=parameters,
                data=data,
                json=json,
            ) as response,
        ):
            response.raise_for_status()
            return await response.json()
