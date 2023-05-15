from pydantic import BaseModel


class Location_Post(BaseModel):
    lat: float
    lng: float
    radius: int
