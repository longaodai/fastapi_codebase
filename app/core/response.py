from typing import Any, Optional, Dict
from pydantic import BaseModel


class ResponseSuccess(BaseModel):
    status_code: int = 200
    success: bool = True
    message: str = "Success"
    data: Optional[Any] = None


class ResponseError(BaseModel):
    success: bool = False
    message: str = "Error"
    error_code: Optional[str] = None
    details: Optional[Dict[str, Any]] = None
    
    def dict(self, **kwargs):
        return self.model_dump(**kwargs)