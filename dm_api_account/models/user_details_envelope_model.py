from enum import Enum
from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, StrictStr, Field, StrictBool, ConstrainedDate


class PagingSettings(BaseModel):
    posts_per_page: int = Field(alias='postsPerPage')
    comments_per_page: int = Field(alias='commentsPerPage')
    topics_per_page: int = Field(alias='topicsPerPage')
    messages_per_page: int = Field(alias='messagesPerPage')
    entities_per_page: int = Field(alias='entitiesPerPage')


class ColorSchema(Enum):
    MODERN = 'Modern'
    PALE = 'Pale'
    CLASSIC = 'Classic'
    CLASSIC_PALE = 'ClassicPale'
    NIGHT = 'Night'


class UserSettings(BaseModel):
    color_schema: Optional[ColorSchema]
    nanny_greetings_message: Optional[StrictStr] = Field(alias='nannyGreetingsMessage')
    paging: Optional[PagingSettings]


class BbParseModel(Enum):
    COMMON = 'Common'
    INFO = 'Info'
    POST = 'Post'
    CHAT = 'Chat'


class InfoBbText(BaseModel):
    value: Optional[StrictStr]
    parse_mode: Optional[BbParseModel] = Field(alias='parseMode')


class Roles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


class UserDetails(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(alias='mediumPictureUrl')
    small_picture_url: Optional[StrictStr] = Field(alias='smallPictureUrl')
    status: Optional[StrictStr]
    rating: Rating
    online: Optional[datetime]
    name: Optional[StrictStr]
    location: Optional[StrictStr]
    registration: Optional[datetime]
    icq: Optional[StrictStr]
    skype: Optional[StrictStr]
    original_picture_url: Optional[StrictStr] = Field(alias='originalPictureUrl')
    info: Optional[InfoBbText]
    settings: Optional[UserSettings]


class UserDetailsEnvelopeModel(BaseModel):
    resource: Optional[UserDetails]
    metadata: Optional[StrictStr]
