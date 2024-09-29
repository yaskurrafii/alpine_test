"""
model.py

all of the table model should be in here
"""

from sqlmodel import SQLModel, Field
from typing import Optional

class Payload(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    list_1 : str
    list_2 :str
    output : str