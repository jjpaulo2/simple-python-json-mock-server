from pydantic import BaseModel

class MockNotFoundResponse(BaseModel):
    message: str
    mock: str
    