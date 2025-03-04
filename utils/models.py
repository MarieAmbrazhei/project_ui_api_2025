from pydantic import BaseModel, EmailStr, constr


class ValidateRegistrationModel(BaseModel):
    first_name: constr(min_length=1, max_length=50)
    last_name: constr(min_length=1, max_length=50)
    email: EmailStr
    password: constr(min_length=8, max_length=8)
    confirm_password: constr(min_length=8, max_length=8)
