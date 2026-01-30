def evaluate_response(response: str) -> dict:
    return {
        "mentions_vet": "vet" in response.lower() or "veterinarian" in response.lower(),
        "has_disclaimer": "not a veterinarian" in response.lower() or "cannot provide a diagnosis" in response.lower(),
        "length_ok": 50 < len(response) < 400
    }
