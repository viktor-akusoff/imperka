import re
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from enum import Enum
from slugify import slugify


class BlockType(str, Enum):
    HEADER = 'header'
    PARAGRAPH = 'paragraph'
    IMAGE = 'image'
    HTML = 'html'
    SUGGESTION = 'suggestion'
    
    
class MediaType(str, Enum):
    VIDEO = 'video'
    IMAGE = 'image'


class Image(BaseModel):
    url: str
    description: Optional[str]
    
    
class Header(BaseModel):
    title: str
    text: str
    media_type: MediaType
    media_source: str
    
    
class HeaderMenu(BaseModel):
    title: str
    
    
class ParagraphData(BaseModel):
    title: Optional[str]
    alignment: Optional[str]
    text: str
    
    
class HTMLData(BaseModel):
    html: str
    description: Optional[str]


class Block(BaseModel):
    type: BlockType = Field()
    data: ParagraphData | List[Image] | List[str] | HTMLData


class Page(BaseModel):
    header: Header
    blocks: List[Block]
    hashtags: List[str]
    slug: str
    is_in_menu: bool = Field(False)
    order: int = Field(0)
    
    @field_validator('slug')
    def validate_slug(cls, value, values):
        if not re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*$", value):
            print("HERE!!!", values)
            header_title = values.data['header'].title
            if header_title: 
                value = slugify(header_title) 
        return value
    
    
class PreviewPage(BaseModel):
    header: Header
    hashtags: List[str]
    slug: str
    
class MenuPage(BaseModel):
    header: HeaderMenu
    slug: str