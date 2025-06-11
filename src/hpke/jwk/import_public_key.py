"""
This module contains the function to import a public key from a JWK.
"""

from .models import JWK
from hpke.base64url import base64url_no_padding_decode

def import_public_key(key: str) -> bytes:
    """Import a public key from the given JWK."""
    jwk = JWK.model_validate_json(key)
    expanded_public_key = '04' + base64url_no_padding_decode(jwk.x).hex() + base64url_no_padding_decode(jwk.y).hex()
    return bytes.fromhex(expanded_public_key)