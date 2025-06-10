"""
This module contains the function to encrypt and decrypt the given plaintext using the given public and private keys.
"""

import base64
import hybrid_pke
import json
from hpke.jwk import import_public_key, import_private_key, JWK


# flake8: noqa
# pylint: disable=all
# mypy: ignore-errors

hpke = hybrid_pke.default(
  mode=hybrid_pke.Mode.BASE, 
  kem=hybrid_pke.Kem.DHKEM_P256,
  kdf=hybrid_pke.Kdf.HKDF_SHA256,
  aead=hybrid_pke.Aead.AES_128_GCM
)
info = b""  # shared metadata, correspondance-level


def encrypt_integrated(public_key: str, plaintext: bytes) -> tuple[bytes, bytes]:
    """
    Encrypt the given plaintext using the given public key.
    """
    jwk = JWK.model_validate_json(public_key)
    public_key_r = import_public_key(public_key)
    protected_header_json = json.dumps({
        "alg": jwk.alg,
        "end": "int",
        "kid": jwk.kid
    })
    protected_header = base64.urlsafe_b64encode(protected_header_json.encode(encoding='utf-8')).decode(encoding='utf-8').rstrip('=')
    aad = protected_header.encode(encoding='utf-8')
    encap, ciphertext = hpke.seal(public_key_r, info, aad, plaintext)
    ct = base64.urlsafe_b64encode(ciphertext).decode(encoding='utf-8').rstrip('=')
    encrypted_key = base64.urlsafe_b64encode(encap).decode(encoding='utf-8').rstrip('=')
    iv = ''
    tag = ''
    return f"{protected_header}.{encrypted_key}.{iv}.{ct}.{tag}"


def decrypt_integrated(private_key: str, jwe: str) -> bytes:
    """
    Decrypt the given ciphertext using the given private key.
    """
    _public_key_r, secret_key_r = import_private_key(private_key)

    protected_header, encrypted_key, iv, ct, tag = jwe.split('.')
    aad = protected_header.encode(encoding='utf-8')
    encap = base64.urlsafe_b64decode(encrypted_key + '=')
    ciphertext = base64.urlsafe_b64decode(ct + '=')

    plaintext = hpke.open(encap, secret_key_r, info, aad, ciphertext)
    return plaintext