"""Number Service - Provides list of numbers for dropdown."""

from typing import List


class NumberService:
    """Service responsible for providing the list of available numbers."""
    
    VALID_NUMBERS: List[int] = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    @classmethod
    def get_numbers(cls) -> List[int]:
        """Return list of integers [1-10].
        
        Returns:
            List[int]: List of integers from 1 to 10.
        """
        return cls.VALID_NUMBERS.copy()
