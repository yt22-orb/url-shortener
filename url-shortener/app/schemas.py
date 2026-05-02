from pydantic import BaseModel

class URLCreate(BaseModel):
    
    original: str