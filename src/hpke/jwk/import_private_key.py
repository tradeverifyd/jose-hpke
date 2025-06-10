"""
This module contains the function to import a public key from a JWK.
"""
import base64
from .models import JWK


def import_private_key(key: str) -> tuple[bytes, bytes]:
    """Import a private key from the given JWK."""
    jwk = JWK.model_validate_json(key)
    expanded_public_key = bytes.fromhex('04' + base64.urlsafe_b64decode(jwk.x + '=').hex() + base64.urlsafe_b64decode(jwk.y + '=' ).hex())
    private_key = bytes.fromhex(base64.urlsafe_b64decode(jwk.d + '=').hex())
    return expanded_public_key, private_key