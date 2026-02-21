from pydantic import BaseModel, computed_field
from typing import Dict

class Patients(BaseModel):
    name: str
    age: int
    height: float
    weight: float
    email: str
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)


def insert_data(patient: Patients):
    print(f"Inserting {patient.name} into the database")
    print(f"Inserting {patient.age} into the database")
    print(f"Inserting {patient.height} into the database")
    print(f"Inserting {patient.weight} into the database")
    print(f"Inserting {patient.email} into the database")
    print(f"BMI of {patient.name} is {patient.bmi}")
    print(f"Inserting {patient.contact_details} into the database")
    print("Data inserted successfully")


patient_info = {
    "name": "John",
    "age": 30,
    "height": 1.75,
    "weight": 70,
    "email": "abc@gmail.com",
    "contact_details": {"phone": "1234567890"}
}

patient_obj1 = Patients(**patient_info)
print(patient_obj1)
insert_data(patient_obj1)