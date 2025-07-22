from pydantic import BaseModel, EmailStr, constr, conint

class Address(BaseModel):
    street: constr(min_length=3)
    number: conint(gt=0)
    county: constr(min_length=2)
    country: constr(min_length=2)
    eircode: constr(pattern=r"^[A-Z0-9]{7}$")

class User(BaseModel):
    user_id: int
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    age: conint(gt=18)
    address: Address


