"""
This module contains the function to export the public key from the given JWK.
"""
import json
from .models import JWK
def export_private_key(key: JWK) -> str:
    """Export the private key from the given JWK."""

    jwk = key.model_dump(exclude_none=True)
    jwk_json = json.dumps(jwk)
    return jwk_json
