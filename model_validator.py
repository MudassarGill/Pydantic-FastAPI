from pydantic import BaseModel, Field, model_validator
from typing import Dict

class Patient(BaseModel):
    name: str
    age: int
    email: str
    contact_details: Dict[str, str]

    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age > 60 and "emergency_contact" not in model.contact_details:
            raise ValueError("Emergency contact is required for patients above 60")
        return model

def insert_data(patient: Patient):
    print(f"Inserting {patient.name} into the database")
    print(f"Inserting {patient.age} into the database")
    print(f"Inserting {patient.email} into the database")
    print("Data inserted successfully")

# Patient info
patient_info = {
    "name": "John",
    "age": 30,
    "email": "abc@gmail.com",
    "contact_details": {"phone": "1234567890"}  # Missing emergency_contact
}

# This will raise the validator error
try:
    patient_obj = Patient(**patient_info)
    print(patient_obj)
    insert_data(patient_obj)
except ValueError as e:
    print(f"Validation Error: {e}")