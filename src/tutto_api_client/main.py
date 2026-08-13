"""This module provides the main client class for the Tutto API."""

from typing import List
from datetime import date

from src.tutto_api_client.models.authorization import Authorization
from src.tutto_api_client.models.entities import Relative, Occurrence
from src.tutto_api_client.models.endpoints import (
    _Deductions,
    _Purchases,
    _ServiceTypes,
    _DirfInfos,
    _DirfAdditionalInfos,
    _Employees,
    _EmployeesOccupations,
    _Occupations,
    _ServiceTickets,
)
from src.tutto_api_client.core.endpoints_factory import _EndpointFactory

__all__ = ["TuttoAPIClient"]


class TuttoAPIClient:
    """
    The main client class for the Tutto API.

    This class provides a client to interact with the Tutto API.
    It provides methods to authenticate, get and set services required by the endpoints,
    and get an endpoint instance by name.
    """

    def __init__(
        self,
        base_url: str,
        authorization: Authorization,
    ) -> None:
        self.__base_url = base_url
        self.__authorization = authorization

    def get_deductions(
        self,
        reference: str,
        type: str = "",
        start_date: str = "",
        end_date: str = "",
        id: int = 0,
    ) -> _Deductions:
        """
        Get an instance of the Deductions endpoint.

        Returns:
            Deductions: An instance of the Deductions endpoint.
        """
        return _EndpointFactory.create_endpoint(
            base_url=self.__base_url,
            endpoint="deductions",
            authorization=self.__authorization,
            reference=reference,
            type=type,
            start_date=start_date,
            end_date=end_date,
            id=id,
        )

    def get_purchases(
        self,
        reference: str,
        type: str = "",
        start_date: str = "",
        end_date: str = "",
        id: int = 0,
    ) -> _Purchases:
        """
        Get an instance of the Purchases endpoint.

        Returns:
            Purchases: An instance of the Purchases endpoint.
        """
        return _EndpointFactory.create_endpoint(
            base_url=self.__base_url,
            endpoint="purchases",
            authorization=self.__authorization,
            reference=reference,
            type=type,
            start_date=start_date,
            end_date=end_date,
            id=id,
        )

    def get_service_types(self) -> _ServiceTypes:
        """
        Get an instance of the ServiceTypes endpoint.

        Returns:
            ServiceTypes: An instance of the ServiceTypes endpoint.
        """
        return _EndpointFactory.create_endpoint(
            base_url=self.__base_url,
            endpoint="service_types",
            authorization=self.__authorization,
        )

    def get_dirf_infos(
        self,
        reference: str,
        layout: str = "",
        company_id: int = 0,
        type: str = "",
        start_date: str = "",
        end_date: str = "",
        id: int = 0,
    ) -> _DirfInfos:
        """
        Get an instance of the DirfInfos endpoint.

        Returns:
            DirfInfos: An instance of the DirfInfos endpoint.
        """
        return _EndpointFactory.create_endpoint(
            base_url=self.__base_url,
            endpoint="dirf_infos",
            authorization=self.__authorization,
            reference=reference,
            layout=layout,
            company_id=company_id,
            type=type,
            start_date=start_date,
            end_date=end_date,
            id=id,
        )

    def get_dirf_additional_infos(
        self,
        reference: str,
        layout: str = "",
        company_id: int = 0,
        type: str = "",
        start_date: str = "",
        end_date: str = "",
        id: int = 0,
    ) -> _DirfAdditionalInfos:
        """
        Get an instance of the DirfAdditionalInfos endpoint.

        Returns:
            DirfAdditionalInfos: An instance of the DirfAdditionalInfos endpoint.
        """
        return _EndpointFactory.create_endpoint(
            base_url=self.__base_url,
            endpoint="dirf_additional_infos",
            authorization=self.__authorization,
            reference=reference,
            layout=layout,
            company_id=company_id,
            type=type,
            end_date=end_date,
            start_date=start_date,
            id=id,
        )

    def get_employees(
        self,
        company_code: str,
        company_vat: str,
        name: str,
        badge: str,
        vat: str,
        id_card: str,
        id_card_entity: str,
        id_card_emission: date,
        id_card_emission_state: str,
        sus_card: str,
        ctps_number: str,
        pis_pasep: str,
        mother_name: str,
        address: str,
        address_number: str,
        complement: str,
        neighborhood: str,
        city: str,
        state: str,
        zipcode: str,
        phone: str,
        email: str,
        personal_email: str,
        gender: str,
        marital_status: str,
        salary: float,
        birthday_date: date,
        admission_date: date,
        resignation_date: date,
        experience_end_date: date,
        status_in_payroll: str,
        organizational_unit_code: str,
        organizational_unit_name: str,
        position_code: str,
        position_name: str,
        occupation_code: str,
        occupation_name: str,
        workplace_code: str,
        workplace_name: str,
        syndicate_name: str,
        transfer_date: date,
        bank_code: str,
        bank_agency: str,
        bank_account: str,
        resignation_reason_code: str,
        resignation_reason_name: str,
        relatives: List[Relative] = [],
        occurrences: List[Occurrence] = [],
    ) -> _Employees:
        """
        Get an instance of the Employees endpoint.

        Returns:
            Employees: An instance of the Employees endpoint.
        """
        return _EndpointFactory.create_endpoint(
            base_url=self.__base_url,
            endpoint="employees",
            authorization=self.__authorization,
            company_code=company_code,
            company_vat=company_vat,
            name=name,
            badge=badge,
            vat=vat,
            id_card=id_card,
            id_card_entity=id_card_entity,
            id_card_emission=id_card_emission,
            id_card_emission_state=id_card_emission_state,
            sus_card=sus_card,
            ctps_number=ctps_number,
            pis_pasep=pis_pasep,
            mother_name=mother_name,
            address=address,
            address_number=address_number,
            complement=complement,
            neighborhood=neighborhood,
            city=city,
            state=state,
            zipcode=zipcode,
            phone=phone,
            email=email,
            personal_email=personal_email,
            gender=gender,
            marital_status=marital_status,
            salary=salary,
            birthday_date=birthday_date,
            admission_date=admission_date,
            resignation_date=resignation_date,
            experience_end_date=experience_end_date,
            status_in_payroll=status_in_payroll,
            organizational_unit_code=organizational_unit_code,
            organizational_unit_name=organizational_unit_name,
            position_code=position_code,
            position_name=position_name,
            occupation_code=occupation_code,
            occupation_name=occupation_name,
            workplace_code=workplace_code,
            workplace_name=workplace_name,
            syndicate_name=syndicate_name,
            transfer_date=transfer_date,
            bank_code=bank_code,
            bank_agency=bank_agency,
            bank_account=bank_account,
            resignation_reason_code=resignation_reason_code,
            resignation_reason_name=resignation_reason_name,
            relatives=relatives,
            occurrences=occurrences,
        )

    def get_employees_occupations(
        self,
        badge: str,
        vat: str,
        occupation_code: str,
        company_code: str = "",
        company_vat: str = "",
    ) -> _EmployeesOccupations:
        """
        Get an instance of the EmployeesOccupations endpoint.

        Returns:
            EmployeesOccupations: An instance of the EmployeesOccupations endpoint.
        """
        return _EndpointFactory.create_endpoint(
            base_url=self.__base_url,
            endpoint="employees_occupations",
            authorization=self.__authorization,
            badge=badge,
            vat=vat,
            occupation_code=occupation_code,
            company_code=company_code,
            company_vat=company_vat,
        )

    def get_occupations(
        self,
        name: str,
        code: str,
        description: str,
        points: int,
        company_code: str = "",
        company_vat: str = "",
    ) -> _Occupations:
        """
        Get an instance of the Occupations endpoint.

        Returns:
            Occupations: An instance of the Occupations endpoint.
        """
        return _EndpointFactory.create_endpoint(
            base_url=self.__base_url,
            endpoint="occupations",
            authorization=self.__authorization,
            name=name,
            code=code,
            description=description,
            points=points,
            company_code=company_code,
            company_vat=company_vat,
        )

    def get_service_tickets(
        self,
        employee_badge: str,
        employee_vat: str,
        employee_email: str,
        title: str,
        description: str,
        service_type_id: int,
    ) -> _ServiceTickets:
        """
        Get an instance of the ServiceTickets endpoint.

        Returns:
            ServiceTickets: An instance of the ServiceTickets endpoint.
        """
        return _EndpointFactory.create_endpoint(
            base_url=self.__base_url,
            endpoint="service_tickets",
            authorization=self.__authorization,
            employee_badge=employee_badge,
            employee_vat=employee_vat,
            employee_email=employee_email,
            title=title,
            description=description,
            service_type_id=service_type_id,
        )
