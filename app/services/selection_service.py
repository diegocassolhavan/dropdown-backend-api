"""Selection Service - Validates and processes user selections."""

from typing import Dict, Any, Tuple, Optional

from .number_service import NumberService
from .letter_service import LetterService


class SelectionService:
    """Service responsible for validating and processing user selections."""
    
    @classmethod
    def validate_selection(cls, number: Optional[int], letter: Optional[str]) -> Tuple[bool, Optional[str]]:
        """Validate if number and letter are valid selections.
        
        Args:
            number: The selected number (or None if missing).
            letter: The selected letter (or None if missing).
            
        Returns:
            Tuple[bool, Optional[str]]: (is_valid, error_message)
                - (True, None) if valid
                - (False, error_message) if invalid
        """
        # Check for incomplete data
        if number is None or letter is None:
            return False, "Dados incompletos"
        
        # Validate number
        valid_numbers = NumberService.get_numbers()
        if number not in valid_numbers:
            return False, "Número inválido"
        
        # Validate letter
        valid_letters = LetterService.get_letters()
        if letter not in valid_letters:
            return False, "Letra inválida"
        
        return True, None
    
    @classmethod
    def process_selection(cls, number: int, letter: str) -> Dict[str, Any]:
        """Process and return confirmation of the selection.
        
        Args:
            number: The validated selected number.
            letter: The validated selected letter.
            
        Returns:
            Dict[str, Any]: Response with success status and selection details.
        """
        is_valid, error = cls.validate_selection(number, letter)
        
        if not is_valid:
            return {
                "success": False,
                "error": error
            }
        
        return {
            "success": True,
            "message": "Seleção recebida com sucesso",
            "selection": {
                "number": number,
                "letter": letter
            }
        }
