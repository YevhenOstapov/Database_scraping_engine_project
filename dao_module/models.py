from sqlalchemy import PrimaryKeyConstraint, Column, Date, String, Boolean

from dao_module.connection_db import Base


class Person(Base):
    __tablename__ = 'summer_school'
    __table_args__ = (
        PrimaryKeyConstraint('date', 'name', 'gender', 'country'),
    )

    date = Column(Date)
    name = Column(String)
    gender = Column(String)
    country = Column(String)
    is_saved = Column(Boolean, default=False)

    def __init__(self, date, name, gender, country, is_saved=False):
        super().__init__()
        self.date = date
        self.name = name
        self.gender = gender
        self.country = country
        self.is_saved = is_saved
