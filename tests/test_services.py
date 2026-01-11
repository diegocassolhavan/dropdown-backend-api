"""Unit tests for services.

Tests for:
- NumberService.get_numbers()
- LetterService.get_letters()
- SelectionService.validate_selection()

Validates: Requirements 1.1, 2.1, 3.3, 3.4
"""

import pytest
from app.services.number_service import NumberService
from app.services.letter_service import LetterService
from app.services.selection_service import SelectionService


class TestNumberService:
    """Tests for NumberService."""

    def test_get_numbers_returns_list(self):
        """Test that get_numbers returns a list."""
        result = NumberService.get_numbers()
        assert isinstance(result, list)

    def test_get_numbers_returns_integers_1_to_10(self):
        """Test that get_numbers returns [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]."""
        result = NumberService.get_numbers()
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_get_numbers_all_elements_are_integers(self):
        """Test that all elements in the list are integers."""
        result = NumberService.get_numbers()
        assert all(isinstance(n, int) for n in result)


class TestLetterService:
    """Tests for LetterService."""

    def test_get_letters_returns_list(self):
        """Test that get_letters returns a list."""
        result = LetterService.get_letters()
        assert isinstance(result, list)

    def test_get_letters_returns_a_to_j(self):
        """Test that get_letters returns ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]."""
        result = LetterService.get_letters()
        assert result == ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    def test_get_letters_all_elements_are_strings(self):
        """Test that all elements in the list are strings."""
        result = LetterService.get_letters()
        assert all(isinstance(letter, str) for letter in result)


class TestSelectionService:
    """Tests for SelectionService."""

    def test_validate_selection_valid_input(self):
        """Test validation with valid number and letter."""
        is_valid, error = SelectionService.validate_selection(5, "C")
        assert is_valid is True
        assert error is None

    def test_validate_selection_invalid_number(self):
        """Test validation with invalid number."""
        is_valid, error = SelectionService.validate_selection(99, "A")
        assert is_valid is False
        assert error == "Número inválido"

    def test_validate_selection_invalid_letter(self):
        """Test validation with invalid letter."""
        is_valid, error = SelectionService.validate_selection(1, "Z")
        assert is_valid is False
        assert error == "Letra inválida"

    def test_validate_selection_none_number(self):
        """Test validation with None number."""
        is_valid, error = SelectionService.validate_selection(None, "A")
        assert is_valid is False
        assert error == "Dados incompletos"

    def test_validate_selection_none_letter(self):
        """Test validation with None letter."""
        is_valid, error = SelectionService.validate_selection(1, None)
        assert is_valid is False
        assert error == "Dados incompletos"
