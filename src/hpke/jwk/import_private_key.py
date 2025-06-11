"""
This module contains the function to import a public key from a JWK.
"""



from .models import JWK
from hpke.base64url import base64url_no_padding_decode

def import_private_key(key: str) -> tuple[bytes, bytes]:
    """Import a private key from the given JWK."""
    jwk = JWK.model_validate_json(key)
    expanded_public_key = bytes.fromhex('04' + base64url_no_padding_decode(jwk.x).hex() + base64url_no_padding_decode(jwk.y).hex())
    private_key = base64url_no_padding_decode(jwk.d)
    return expanded_public_key, private_key