from pydantic import BaseModel,Field,field_validator,EmailStr,AnyUrl
from typing import Optional,Dict,List,Annotated

class patients(BaseModel):
    name:str
    age:Annotated[int,Field(gt=0,lt=100,description="Age of the person",examples=["25","30"])]
    email:str
def insert_data(patient:patients):
    print(f"inserting {patient.name} into the database")
    print(f"inserting {patient.age} into the database")
    print(f"inserting {patient.email} into the database")
    print("Data inserted successfully")
    
@field_validator("email") 
@classmethod
def validate_email(cls,value):
     domain=['hbl.com','gov.com']
     domain_name=value.split("@")[-1]
     if domain_name not in domain:
         raise ValueError("Invalid email")
     return value

@field_validator("name")
@classmethod
def validate_name(cls,value):
    return value.upper()
   
patient_info={
    "name":"John",
    "age":30,
    "email":"abc@gmail.com"
}
patient_ob1=patients(**patient_info)
print(patient_ob1)
insert_data(patient_ob1)

    
    