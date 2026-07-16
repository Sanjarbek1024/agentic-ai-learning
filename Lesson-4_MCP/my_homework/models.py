
# Employee
#   ~ id
#   ~ name
#   ~ department
#   ~ salary

from database import Base 
from sqlalchemy import Integer, String, Column


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    salary = Column(Integer, nullable=False)
