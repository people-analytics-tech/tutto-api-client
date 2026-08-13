"""Module to define the entities of Tutto API, a class-like to the body of requests."""

from dataclasses import dataclass, field
from datetime import date


### Entities ###
@dataclass(init=True, frozen=True)
class Relative:
    """Class to represent a relative entity.\n
    Args:
        name (str, optional): Relative name.
        code (str, optional): Relative code.
        birthday_date (date, optional): Relative birthday date.
        vat (str, optional): Relative VAT number.
        id_card (str, optional): Relative ID card number.
        id_card_entity (str, optional): Relative ID card entity.
        id_card_emission (date, optional): Relative ID card emission date.
        id_card_emission_state (str, optional): Relative ID card emission
        gender (str, optional): Relative gender.
        kinship_degree (str, optional): Relative kinship degree.
        marital_status (str, optional): Relative marital status.
        sus_card (str, optional): Relative SUS card number.
        mother_name (str, optional): Relative mother name.
        father_name (str, optional): Relative father name.
        race (str, optional): Relative pet race.
        species (str, optional): Relative pet species.
    """

    name: str = field(default="")
    code: str = field(default="")
    birthday_date: date = field(default=None)
    vat: str = field(default="")
    id_card: str = field(default="")
    id_card_entity: str = field(default="")
    id_card_emission: date = field(default=None)
    id_card_emission_state: str = field(default="")
    gender: str = field(default="")
    kinship_degree: str = field(default="")
    marital_status: str = field(default="")
    sus_card: str = field(default="")
    mother_name: str = field(default="")
    father_name: str = field(default="")
    race: str = field(default="")
    species: str = field(default="")


@dataclass(init=True, frozen=True)
class Occurrence:
    """Class to represent an occurrence entity.\n
    Args:
        type (str, optional): Occurrence type.
        start_date (date, optional): Occurrence date.
        end_date (date, optional): Occurrence end date.
        absence_reason_code (str, optional): Absence reason code.
        absence_reason_name (str, optional): Absence reason name.
    """

    type: str = field(default="")
    start_date: date = field(default=None)
    end_date: date = field(default=None)
    absence_reason_code: str = field(default="")
    absence_reason_name: str = field(default="")
