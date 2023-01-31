# from pydantic import BaseModel, Field, validator, root_validator
# from pydantic.types import Decimal
#
# emails = {'dfghjk@sdfg.d', 'sdfgh@hjk.gh'}
#
# class Passport:
#     pass
#
#
# class User(BaseModel):
#     username: str = Field(min_length=4, max_length=64)
#     age: int = Field(ge=18, lt=100)
#     is_human: bool = Field(True)
#     # email = 'fghh@jk.hgh'
#     passport: Passport
#
#     @validator('email', pre=True):
#     def email111(cls, value):
#         if value not in emails:
#             return value.lower()
#         else:
#             raise ValueError
#     @root_validator()
#     def root111(cls, values: dict):
#         if values.get
#
#
# user = {
#     'username': 'Alex',
#     'age': 25,
#     'email': 'fghh@jk.hgh',
# }
# user = User(**user)
# print(user)
# print(user.dict())

from yaml import load, dump, FullLoader
with open('input.yaml', 'r') as file:
    pass