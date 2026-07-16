from database import SessionLocal
from models import Employee


def seed_database():
    session = SessionLocal()

    session.query(Employee).delete()

    employees = [
        Employee(name="John Smith", department="IT", salary=6500),
        Employee(name="Emma Johnson", department="HR", salary=4200),
        Employee(name="Michael Brown", department="Finance", salary=7100),
        Employee(name="Olivia Davis", department="Marketing", salary=4800),
        Employee(name="William Wilson", department="IT", salary=8300),
        Employee(name="Sophia Moore", department="Sales", salary=5600),
        Employee(name="James Taylor", department="Finance", salary=6900),
        Employee(name="Isabella Anderson", department="HR", salary=4500),
        Employee(name="Benjamin Thomas", department="IT", salary=9200),
        Employee(name="Charlotte Jackson", department="Marketing", salary=5100),
        Employee(name="Daniel White", department="Sales", salary=4700),
        Employee(name="Mia Harris", department="Finance", salary=7600),
        Employee(name="Lucas Martin", department="IT", salary=6100),
        Employee(name="Amelia Thompson", department="HR", salary=4300),
        Employee(name="Henry Garcia", department="Marketing", salary=5900),
        Employee(name="Evelyn Martinez", department="Sales", salary=6200),
        Employee(name="Alexander Robinson", department="IT", salary=9800),
        Employee(name="Harper Clark", department="Finance", salary=8100),
        Employee(name="David Lewis", department="HR", salary=4100),
        Employee(name="Ella Walker", department="Marketing", salary=5400),
    ]

    session.add_all(employees)
    session.commit()
    session.close()

    print("Database seeded successfully.")


if __name__ == "__main__":
    seed_database()