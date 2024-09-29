"""
Schema.py

This file to create serializer of the data that want to put in payload
or data for response, all of class is serializer

"""

from pydantic import BaseModel
from typing import List

class Create(BaseModel):
    list_1 : List[str]
    list_2 : List[str]

class Response(BaseModel):
    output:str