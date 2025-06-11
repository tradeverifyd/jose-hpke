
import hashlib
import hybrid_pke
from .models import JWK
from hpke.base64url import base64url_no_padding_encode

# flake8: noqa
# pylint: disable=all
# mypy: ignore-errors


def _rfc7638_thumbprint(kty: str, crv: str, x: str, y: str) -> str:
    """Generate a RFC 7638 thumbprint for the given parameters."""
    return base64url_no_padding_encode(
        hashlib.sha256(
            f"{{\"kty\":\"{kty}\",\"crv\":\"{crv}\",\"x\":\"{x}\",\"y\":\"{y}\"}}"
            .encode(encoding="utf-8")
        ).digest()
    )


# Keep the standalone function for backward compatibility
def generate_key(alg: str = "HPKE-0") -> JWK:
    """Generate a JWK for the given algorithm."""

    if alg != "HPKE-0":
        raise ValueError(f"Unsupported algorithm: {alg}")

    hpke = hybrid_pke.default(
      mode=hybrid_pke.Mode.BASE, 
      kem=hybrid_pke.Kem.DHKEM_P256,
      kdf=hybrid_pke.Kdf.HKDF_SHA256,
      aead=hybrid_pke.Aead.AES_128_GCM
    )
    secret_key_r, public_key_r = hpke.generate_key_pair()
    x_coord = base64url_no_padding_encode(public_key_r[1:33])  # Skip first byte (0x04) and take next 32 bytes
    y_coord = base64url_no_padding_encode(public_key_r[33:65])  # Take last 32 bytes
    d_coord = base64url_no_padding_encode(secret_key_r)
    kid = _rfc7638_thumbprint("P-256", "EC", x_coord, y_coord)
    return JWK(kty="EC", use="enc", alg=alg, kid=kid, x=x_coord, y=y_coord, d=d_coord)