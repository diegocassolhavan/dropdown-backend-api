# Dropdown Backend API v2
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data
VALID_NUMBERS = [1, 2, 3, 4, 5]
VALID_LETTERS = ["a", "b", "c", "d", "e"]

# Models
class SelectionRequest(BaseModel):
    number: int
    letter: str

class SelectionData(BaseModel):
    number: int
    letter: str

class SelectionResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    error: Optional[str] = None
    selection: Optional[SelectionData] = None

@app.get("/")
def root():
    return {"message": "Dropdown Backend API"}

@app.get("/api/numbers")
def get_numbers():
    return {"numbers": VALID_NUMBERS}

@app.get("/api/letters")
def get_letters():
    return {"letters": VALID_LETTERS}

@app.post("/api/selection")
def post_selection(selection: SelectionRequest):
    if selection.number not in VALID_NUMBERS:
        raise HTTPException(status_code=400, detail={"success": False, "error": "Número inválido"})
    if selection.letter not in VALID_LETTERS:
        raise HTTPException(status_code=400, detail={"success": False, "error": "Letra inválida"})
    
    return SelectionResponse(
        success=True,
        message="Seleção recebida com sucesso",
        selection=SelectionData(number=selection.number, letter=selection.letter)
    )
