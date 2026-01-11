from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.models import NumberListResponse, LetterListResponse, SelectionRequest, SelectionResponse, SelectionData
from app.services.number_service import NumberService
from app.services.letter_service import LetterService
from app.services.selection_service import SelectionService

app = FastAPI(
    title="Dropdown Backend API",
    description="API REST para fornecer listas de números e letras para dropdowns",
    version="1.0.0"
)

# Configurar CORS middleware para permitir requisições cross-origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Dropdown Backend API"}


@app.get("/api/numbers", response_model=NumberListResponse)
async def get_numbers():
    """Retorna a lista de números disponíveis para o dropdown.
    
    Returns:
        NumberListResponse: Lista de números inteiros [1-10].
        
    Validates: Requirements 1.1, 1.2, 1.3
    """
    numbers = NumberService.get_numbers()
    return NumberListResponse(numbers=numbers)


@app.get("/api/letters", response_model=LetterListResponse)
async def get_letters():
    """Retorna a lista de letras disponíveis para o dropdown.
    
    Returns:
        LetterListResponse: Lista de letras ["A"-"J"].
        
    Validates: Requirements 2.1, 2.2, 2.3
    """
    letters = LetterService.get_letters()
    return LetterListResponse(letters=letters)


@app.post("/api/selection", response_model=SelectionResponse)
async def post_selection(selection: SelectionRequest):
    """Recebe e processa a seleção do usuário.
    
    Args:
        selection: SelectionRequest com número e letra selecionados.
        
    Returns:
        SelectionResponse: Confirmação de sucesso ou erro.
        
    Raises:
        HTTPException: 400 se a seleção for inválida.
        
    Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5
    """
    is_valid, error = SelectionService.validate_selection(selection.number, selection.letter)
    
    if not is_valid:
        raise HTTPException(
            status_code=400,
            detail=SelectionResponse(success=False, error=error).model_dump()
        )
    
    return SelectionResponse(
        success=True,
        message="Seleção recebida com sucesso",
        selection=SelectionData(number=selection.number, letter=selection.letter)
    )
