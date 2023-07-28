from datetime import datetime
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from dao_module.connection_db import engine, Base
from dao_module.models import Person


class Dao:

    def __init__(self):
        session = sessionmaker(engine)
        self.session = session()
        Base.metadata.create_all(engine)

    def create_one(self, person: dict):
        if not self.session.get(Person, person):
            self.session.add(Person(**person))
            self.session.commit()

    def update_one(self, person: dict):
        el = self.session.get(Person, person)
        if el:
            el.is_saved = True
            self.session.commit()

    def get_non_saved_data(self) -> List[list]:
        non_saved_data_list = []
        statement = select(Person).filter_by(is_saved=False).order_by(Person.date)
        result = self.session.execute(statement).scalars().all()
        for person in result:
            non_saved_data_list.append([person.date.strftime('%Y/%m/%d'), person.name, person.gender, person.country])
        return non_saved_data_list

    def get_all_data(self) -> List[list]:
        all_data_list = []
        result = self.session.query(Person)
        for person in result:
            all_data_list.append([person.date.strftime('%Y/%m/%d'), person.name, person.gender, person.country])
        return all_data_list

    def table_is_empty(self):
        if not self.session.query(Person).first():
            return True
        return False

    def save_all(self, data: List[dict]):
        data_list = sorted(data, key=lambda person: person.get("date"))
        [self.create_one(person) for person in data_list]

    def update_all(self, data: List[list]):
        list_of_dicts = self._convert_to_list_of_dicts(data)
        [self.update_one(person) for person in list_of_dicts]

    @staticmethod
    def _convert_to_list_of_dicts(data: List[list]) -> List[dict]:
        dict_keys = ["date", "name", "gender", "country"]
        list_of_dictionaries = [dict(zip(dict_keys, i)) for i in data]
        for dictionary in list_of_dictionaries:
            dictionary.update(
                (k, datetime.strptime(v, "%Y/%m/%d").date()) for k, v in dictionary.items() if k == "date")
        return list_of_dictionaries
