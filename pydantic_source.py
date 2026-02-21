from pydantic import BaseModel

class Item(BaseModel):
    name: str
    age: int
    email: str
    phone: int
    address: str
    city: str
    state: str
    zip: int
    country: str
def insert_data(item: Item):
    print(f"inserting {item.name} into the database")
    print(f"inserting {item.age} into the database")
    print(f"inserting {item.email} into the database")
    print(f"inserting {item.phone} into the database")
    print(f"inserting {item.address} into the database")
    print(f"inserting {item.city} into the database")
    print(f"inserting {item.state} into the database")
    print(f"inserting {item.zip} into the database")
    print(f"inserting {item.country} into the database")
    print("Data inserted successfully")
    
info={
    "name":"John",
    "age":30,
    "email":"random@gmail.com",
    "phone":1234567890,
    "address":"123 Main St",
    "city":"New York",
    "state":"NY",
    "zip":12345,
    "country":"USA"
}

data_ob1=Item(**info)
print(data_ob1)
insert_data(data_ob1)
    
    