import dataclasses
from datetime import date

from homework9.pages.enums import Hobby, Gender


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile_number: str
    date_of_birth: date
    subject: str
    hobbies: Hobby
    address: str
    state: str
    city: str


user = User('Олег', 'Олегович', 'oleg.olegovich@example.com', Gender.MALE, '1234567890', date(2000, 7, 10),
            'Maths', Hobby.MUSIC, 'г. Москва, ул. 9-мая, д. 1', 'NCR', 'Delhi')

