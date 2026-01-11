"""Letter Service - Provides list of letters for dropdown."""

from typing import List


class LetterService:
    """Service responsible for providing the list of available letters."""
    
    VALID_LETTERS: List[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    
    @classmethod
    def get_letters(cls) -> List[str]:
        """Return list of letters ["A"-"J"].
        
        Returns:
            List[str]: List of uppercase letters from A to J.
        """
        return cls.VALID_LETTERS.copy()
