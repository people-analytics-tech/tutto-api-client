"""Module to handle requests to an API."""

import aiohttp
from urllib.parse import urljoin
from dataclasses import dataclass, field
from typing import Any, Literal


@dataclass(init=True, frozen=True)
class HTTPRequest:
    """Class to handle requests to an API"""

    base_url: str = field(init=True)

    async def request(
        self,
        endpoint: str,
        method: Literal["get", "post", "put", "patch", "delete"],
        headers: dict = None,
        parameters: dict = None,
        data: Any = None,
        json: Any = None,
    ) -> dict:
        request_url = urljoin(base=self.base_url, url=endpoint)
        headers = {**headers} if headers else {}
        response = None

        async with aiohttp.ClientSession() as session:
            if method == "get":
                response = await session.get(
                    url=request_url,
                    headers=headers,
                    params=parameters,
                )
            elif method == "post":
                response = await session.post(
                    url=request_url,
                    headers=headers,
                    params=parameters,
                    data=data,
                    json=json,
                )
            elif method == "put":
                response = await session.put(
                    url=request_url,
                    headers=headers,
                    params=parameters,
                    data=data,
                    json=json,
                )
            elif method == "patch":
                response = await session.patch(
                    url=request_url,
                    headers=headers,
                    params=parameters,
                    data=data,
                    json=json,
                )
            elif method == "delete":
                response = await session.delete(
                    url=request_url,
                    headers=headers,
                    params=parameters,
                    data=data,
                    json=json,
                )
            else:
                raise ValueError("Invalid HTTP method")

            # Check response
            response.raise_for_status()
            response_json = await response.json()

            return response_json
