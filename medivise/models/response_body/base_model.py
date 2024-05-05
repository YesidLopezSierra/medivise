from pydantic import BaseModel


class BaseModelPayload(BaseModel):
    class Config:
        use_enum_values = True
