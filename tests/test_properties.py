"""Property-based tests for the Dropdown Backend API.

Uses Hypothesis library for property-based testing.
Minimum 100 iterations per property test.

Feature: dropdown-backend-api
"""

from hypothesis import given, strategies as st, settings
from app.services.number_service import NumberService
from app.services.letter_service import LetterService
from app.services.selection_service import SelectionService


# Get valid values for strategies
VALID_NUMBERS = NumberService.VALID_NUMBERS
VALID_LETTERS = LetterService.VALID_LETTERS


class TestPropertyValidSelections:
    """Property 3: Valid selections are accepted.
    
    *For any* number from the valid numbers list and *any* letter from 
    the valid letters list, a POST to /api/selection with that combination 
    SHALL return success with status 200.
    
    **Validates: Requirements 3.1**
    """

    @settings(max_examples=100)
    @given(
        number=st.sampled_from(VALID_NUMBERS),
        letter=st.sampled_from(VALID_LETTERS)
    )
    def test_valid_selections_are_accepted(self, number: int, letter: str):
        """Feature: dropdown-backend-api, Property 3: Valid selections are accepted.
        
        For any valid number and valid letter, validation should succeed.
        """
        is_valid, error = SelectionService.validate_selection(number, letter)
        assert is_valid is True, f"Expected valid selection for number={number}, letter={letter}, got error: {error}"
        assert error is None


class TestPropertyInvalidInputs:
    """Property 4: Invalid inputs are rejected.
    
    *For any* number NOT in the valid numbers list OR *any* letter NOT in 
    the valid letters list, a POST to /api/selection SHALL return status 400 
    with an error message.
    
    **Validates: Requirements 3.3, 3.4**
    """

    @settings(max_examples=100)
    @given(
        number=st.integers().filter(lambda x: x not in VALID_NUMBERS),
        letter=st.sampled_from(VALID_LETTERS)
    )
    def test_invalid_number_is_rejected(self, number: int, letter: str):
        """Feature: dropdown-backend-api, Property 4: Invalid inputs are rejected.
        
        For any invalid number with valid letter, validation should fail.
        """
        is_valid, error = SelectionService.validate_selection(number, letter)
        assert is_valid is False, f"Expected rejection for invalid number={number}"
        assert error == "Número inválido"

    @settings(max_examples=100)
    @given(
        number=st.sampled_from(VALID_NUMBERS),
        letter=st.text(min_size=1, max_size=1).filter(lambda x: x not in VALID_LETTERS)
    )
    def test_invalid_letter_is_rejected(self, number: int, letter: str):
        """Feature: dropdown-backend-api, Property 4: Invalid inputs are rejected.
        
        For any valid number with invalid letter, validation should fail.
        """
        is_valid, error = SelectionService.validate_selection(number, letter)
        assert is_valid is False, f"Expected rejection for invalid letter={letter}"
        assert error == "Letra inválida"
