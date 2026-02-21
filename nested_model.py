from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    age: int
    email: str
    address: Address


address_info = {
    "street": "123 Main St",
    "city": "New York",
    "state": "NY",
    "zip_code": "12345"
}

address_obj1 = Address(**address_info)

patient_info = {
    "name": "John",
    "age": 30,
    "email": "abc@gmail.com",
    "address": address_obj1
}

patient_obj1 = Patient(**patient_info)
print(patient_obj1)