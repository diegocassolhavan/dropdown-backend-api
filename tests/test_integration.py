"""Integration tests for API endpoints.

Tests the complete flow: GET numbers → GET letters → POST selection
Also tests error responses.

Validates: Requirements 1.1, 2.1, 3.1
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


class TestNumbersEndpoint:
    """Integration tests for GET /api/numbers."""

    def test_get_numbers_returns_200(self):
        """Test that GET /api/numbers returns status 200."""
        response = client.get("/api/numbers")
        assert response.status_code == 200

    def test_get_numbers_returns_json_with_numbers(self):
        """Test that response contains numbers array."""
        response = client.get("/api/numbers")
        data = response.json()
        assert "numbers" in data
        assert data["numbers"] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class TestLettersEndpoint:
    """Integration tests for GET /api/letters."""

    def test_get_letters_returns_200(self):
        """Test that GET /api/letters returns status 200."""
        response = client.get("/api/letters")
        assert response.status_code == 200

    def test_get_letters_returns_json_with_letters(self):
        """Test that response contains letters array."""
        response = client.get("/api/letters")
        data = response.json()
        assert "letters" in data
        assert data["letters"] == ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


class TestSelectionEndpoint:
    """Integration tests for POST /api/selection."""

    def test_post_valid_selection_returns_200(self):
        """Test that valid selection returns status 200."""
        response = client.post("/api/selection", json={"number": 5, "letter": "C"})
        assert response.status_code == 200

    def test_post_valid_selection_returns_success(self):
        """Test that valid selection returns success response."""
        response = client.post("/api/selection", json={"number": 1, "letter": "A"})
        data = response.json()
        assert data["success"] is True
        assert data["message"] == "Seleção recebida com sucesso"
        assert data["selection"]["number"] == 1
        assert data["selection"]["letter"] == "A"

    def test_post_invalid_number_returns_400(self):
        """Test that invalid number returns status 400."""
        response = client.post("/api/selection", json={"number": 99, "letter": "A"})
        assert response.status_code == 400

    def test_post_invalid_letter_returns_400(self):
        """Test that invalid letter returns status 400."""
        response = client.post("/api/selection", json={"number": 1, "letter": "Z"})
        assert response.status_code == 400


class TestCompleteFlow:
    """Integration test for complete flow: GET → GET → POST."""

    def test_complete_flow(self):
        """Test fetching options and making a selection."""
        # Get numbers
        numbers_response = client.get("/api/numbers")
        assert numbers_response.status_code == 200
        numbers = numbers_response.json()["numbers"]
        
        # Get letters
        letters_response = client.get("/api/letters")
        assert letters_response.status_code == 200
        letters = letters_response.json()["letters"]
        
        # Make selection using first number and first letter
        selection_response = client.post(
            "/api/selection",
            json={"number": numbers[0], "letter": letters[0]}
        )
        assert selection_response.status_code == 200
        assert selection_response.json()["success"] is True
