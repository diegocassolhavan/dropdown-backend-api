"""Pydantic models for API request/response validation."""

from typing import List, Optional
from pydantic import BaseModel


class NumberListResponse(BaseModel):
    """Response model for GET /api/numbers endpoint.
    
    Validates: Requirements 1.1
    """
    numbers: List[int]


class LetterListResponse(BaseModel):
    """Response model for GET /api/letters endpoint.
    
    Validates: Requirements 2.1
    """
    letters: List[str]


class SelectionRequest(BaseModel):
    """Request model for POST /api/selection endpoint.
    
    Validates: Requirements 3.1
    """
    number: int
    letter: str


class SelectionData(BaseModel):
    """Nested model for selection data in response."""
    number: int
    letter: str


class SelectionResponse(BaseModel):
    """Response model for POST /api/selection endpoint.
    
    Validates: Requirements 3.1
    """
    success: bool
    message: Optional[str] = None
    error: Optional[str] = None
    selection: Optional[SelectionData] = None
