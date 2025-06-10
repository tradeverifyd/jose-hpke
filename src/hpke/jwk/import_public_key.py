"""
This module contains the function to import a public key from a JWK.
"""
import base64
from .models import JWK


def import_public_key(key: str) -> bytes:
    """Import a public key from the given JWK."""
    jwk = JWK.model_validate_json(key)
    expanded_public_key = '04' + base64.urlsafe_b64decode(jwk.x + '=').hex() + base64.urlsafe_b64decode(jwk.y + '=' ).hex()
    return bytes.fromhex(expanded_public_key)