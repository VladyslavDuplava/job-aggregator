from pydantic import BaseModel, ConfigDict

class Vacancy(BaseModel):
    title: str
    link: str
    source: str
    location: str | None = None
    date: str | None = None
    description: str | None = None
    details: str | None = None

    model_config = ConfigDict(from_attributes=True)


