"""
This module contains the models for the JSON Web Key (JWK) format.
"""
from typing import Optional, List
from pydantic import BaseModel, Field
import hashlib
import base64
import hybrid_pke

# flake8: noqa
# pylint: disable=all
# mypy: ignore-errors

class JWK(BaseModel):
    """JSON Web Key (JWK) model following RFC 7517, but only for the HPKE-0 algorithm."""
    kty: str = Field("EC", description="Key Type")
    use: Optional[str] = Field(None, description="Public Key Use")
    key_ops: Optional[List[str]] = Field(None, description="Key Operations")
    alg: str = Field("HPKE-0", description="Algorithm")
    kid: Optional[str] = Field(None, description="Key ID")
    x5u: Optional[str] = Field(None, description="X.509 URL")
    x5c: Optional[List[str]] = Field(None, description="X.509 Certificate Chain")
    x5t: Optional[str] = Field(None, description="X.509 Certificate SHA-1 Thumbprint")
    x5t_S256: Optional[str] = Field(None, description="X.509 Certificate SHA-256 Thumbprint")
    crv: Optional[str] = Field("P-256", description="Curve")
    x: str = Field(None, description="X Coordinate")
    y: str = Field(None, description="Y Coordinate")
    d: Optional[str] = Field(None, description="Private Key")
    
    @classmethod
    def generate_key(
        cls,
        kty: str = "EC",
        use: Optional[str] = None,
        key_ops: Optional[List[str]] = None,
        alg: Optional[str] = None,
        kid: Optional[str] = None
    ) -> "JWK":
        """Generate a JWK with the given parameters."""
        return cls(
            kty=kty,
            use=use,
            key_ops=key_ops,
            alg=alg,
            kid=kid
        )

