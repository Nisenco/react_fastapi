import datetime
from pydantic import BaseConfig, BaseModel


def convert_datetime_to_realworld(dt: datetime.date) -> str:
    return str(dt)


def convert_field_to_camel_case(string: str) -> str:
    return "".join(
        word if index == 0 else word.capitalize()
        for index, word in enumerate(string.split("_"))
    )


class RWModel(BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        json_encoders = {datetime.date: convert_datetime_to_realworld}


class RWSchema(RWModel):
    class Config(RWModel.Config):
        orm_mode = True