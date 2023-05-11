from pydantic import BaseModel, StrictStr, Field
from uuid import UUID, uuid4


class ChangePasswordModel(BaseModel):
    login: StrictStr
    token: UUID = Field(default_factory=uuid4)
    old_password: StrictStr = Field(alias='oldPassword')
    new_password: StrictStr = Field(alias='newPassword')
