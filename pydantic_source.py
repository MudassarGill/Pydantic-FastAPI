from pydantic import BaseModel,AnyUrl,EmailStr,Field
from typing import Optional,Dict,List,Annotated

class Item(BaseModel):
    name: Annotated[str,Field(min_length=2,max_length=10,description="Name of the person",examples=["John","Jane"])]
    age: Annotated[int,Field(gt=0,lt=100,description="Age of the person",examples=["25","30"])]
    email: Annotated[EmailStr,Field(description="Email of the person",examples=["random@gmail.com"])]
    phone: Annotated[int,Field(min_length=10,max_length=10,description="Phone number of the person",examples=["1234567890"])]
    address: Annotated[Optional[str],Field(description="Address of the person",examples=["123 Main St"])]=None
    linkedin: Annotated[AnyUrl,Field(description="LinkedIn profile URL of the person",examples=["https://www.linkedin.com/in/john-doe/"])]
    city: Annotated[str,Field(description="City of the person",examples=["New York"])]
    state: Annotated[str,Field(description="State of the person",examples=["NY"])]
    zip: Annotated[int,Field(description="Zip code of the person",examples=["12345"])]
    country: Annotated[str,Field(description="Country of the person",examples=["USA"])]
def insert_data(item: Item):
    print(f"inserting {item.name} into the database")
    print(f"inserting {item.age} into the database")
    print(f"inserting {item.email} into the database")
    print(f"inserting {item.phone} into the database")
    print(f"inserting {item.address} into the database")
    print(f"inserting {item.linkedin} into the database")
    print(f"inserting {item.city} into the database")
    print(f"inserting {item.state} into the database")
    print(f"inserting {item.zip} into the database")
    print(f"inserting {item.country} into the database")
    print("Data inserted successfully")
    
info={
    "name":"John",
    "age":  30,
    "email":"random@gmail.com",
    "phone":1234567890,
    "address":"123 Main St",
    "linkedin":"https://www.linkedin.com/in/john-doe/",
    "city":"New York",
    "state":"NY",
    "zip":12345,
    "country":"USA"
}

data_ob1=Item(**info)
print(data_ob1)
insert_data(data_ob1)
    
    