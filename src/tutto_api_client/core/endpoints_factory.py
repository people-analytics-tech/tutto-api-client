"""This module provides a factory method to create an endpoint object."""

from typing import Any

from tutto_api_client.helpers.api_client import APIClient
from tutto_api_client.models.authorization import Authorization
from tutto_api_client.models.endpoints import (
    Endpoint,
    _Deductions,
    _DirfAdditionalInfos,
    _DirfInfos,
    _Employees,
    _EmployeesOccupations,
    _Occupations,
    _Purchases,
    _ServiceTickets,
    _ServiceTypes,
)

__all__ = []


class _EndpointCatalog:
    """
    A catalog of endpoints for the Tutto API.

    This class provides a collection of endpoints that can be used to interact with the Tutto API.
    It also provides methods to get and set services required by the endpoints.
    """

    __catalog = {
        "deductions": _Deductions,
        "purchases": _Purchases,
        "service_types": _ServiceTypes,
        "dirf_infos": _DirfInfos,
        "dirf_additional_infos": _DirfAdditionalInfos,
        "employees": _Employees,
        "employees_occupations": _EmployeesOccupations,
        "occupations": _Occupations,
        "service_tickets": _ServiceTickets,
    }

    def __init__(self) -> None:
        self.__services = {
            "http_client": None,
            "authorization": None,
        }
        self.__setters = ["http_client", "authorization"]

    def get_endpoint(self, name: str, **kwargs) -> Endpoint:
        """
        Get an endpoint instance by name.

        Args:
            name (str): The name of the endpoint.

        Returns:
            Endpoint: An instance of the requested endpoint.

        # TODO
        Return if endpoint not found:
            Endpoint(ABC): An instance of the endpoint abstract dataclass, so you can
            use it to create an endpoint that this library does not support yet.
        """
        if not all(self.__services):
            raise ValueError("Services not set. Please set all required services first")

        endpoint = _EndpointCatalog.__catalog.get(name)
        if endpoint:
            endpoint_class = endpoint(
                http_client=self.__services["http_client"],
                authorization=self.__services["authorization"],
                **kwargs,
            )
            return endpoint_class
        if not endpoint:
            raise NotImplementedError(
                "The Endpoint abstract base class return isn't supported yet."
            )

    def set_services(self, name: str, value: Any) -> None:
        """
        Set a service required by the endpoints.

        Args:
            name (str): The name of the service.
            value (Any): The value of the service.

        Returns:
            None

        Raises:
            NameError: If the provided name is not accepted in the `set_services` method.
        """
        if name in self.__setters:
            self.__services[name] = value
        else:
            raise NameError(f"Name '{name}' not accepted in set_services() method")


class _EndpointFactory:
    def create_endpoint(
        base_url: str, endpoint: str, authorization: Authorization, **kwargs
    ) -> Endpoint:
        """Factory method to create an endpoint object"""
        # Fill the services catalog with the required services
        http_client = APIClient(base_url=base_url)
        catalog_instance = _EndpointCatalog()
        catalog_instance.set_services(name="http_client", value=http_client)
        catalog_instance.set_services(name="authorization", value=authorization)
        return catalog_instance.get_endpoint(name=endpoint, **kwargs)
