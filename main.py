"""
Copyright (C) 2022  pacourbet

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    mail: pierreandre.courbet@gmail.com
"""

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID

app  = FastAPI()


class Mesure(BaseModel):
    id : UUID
    username: str = Field(min_length=1)
    systolique : int = Field(gt=0)
    diastolique : int = Field(gt=0)
    datetime : Optional[str] = datetime.now().strftime("%Y-%m-%d %H:%M")

    class Config:
        schema_extra = {
            "example" : {
                "id" : "6b9fbb64-6a07-4e94-b794-631da9a52b35",
                "username": "jean",
                "systolique" : 78,
                "diastolique" : 114,
                "datetime": "2022-03-16 13:09"
            }
        } 


MESURES = []

@app.get("/")
def read_all_measures():
    return MESURES

@app.post("/")
def create_measure(mesure: Mesure):
    MESURES.append(mesure)
    return mesure

def create_book():
    return None



