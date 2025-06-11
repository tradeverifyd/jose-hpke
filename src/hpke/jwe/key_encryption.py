"""
This module contains the function to encrypt and decrypt the given plaintext using the given public and private keys.
"""

import base64
import hybrid_pke
import json
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from hpke.jwk import import_public_key, import_private_key, JWK
from hpke.base64url import base64url_no_padding_encode, base64url_no_padding_decode

# flake8: noqa
# pylint: disable=all
# mypy: ignore-errors

hpke = hybrid_pke.default(
  mode=hybrid_pke.Mode.BASE, 
  kem=hybrid_pke.Kem.DHKEM_P256,
  kdf=hybrid_pke.Kdf.HKDF_SHA256,
  aead=hybrid_pke.Aead.AES_128_GCM
)

def encrypt_key_encryption(public_key: str, plaintext: bytes) -> tuple[bytes, bytes]:
    """
    Encrypt the given plaintext using the given public key.
    """
    jwk = JWK.model_validate_json(public_key)
    public_key_r = import_public_key(public_key)
   
    content_encryption_key = AESGCM.generate_key(bit_length=128)
    encap, ciphertext = hpke.seal(public_key_r, b"", b"", content_encryption_key)
    encrypted_key = base64url_no_padding_encode(ciphertext)
    ek = base64url_no_padding_encode(encap)

    protected_header_json = json.dumps({
        "enc": "A128GCM",
    })
    protected_header = base64url_no_padding_encode(protected_header_json.encode(encoding='utf-8'))
  
    aad = protected_header.encode(encoding='utf-8')

   
    aesgcm = AESGCM(content_encryption_key)
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, plaintext, aad)
    ct_without_tag = ct[:-16]
    tag_bytes = ct[-16:]
    iv = base64url_no_padding_encode(nonce)
    tag = base64url_no_padding_encode(tag_bytes)
    message_ciphertext = base64url_no_padding_encode(ct_without_tag)

    return json.dumps({
        "protected": protected_header,
        "ciphertext": message_ciphertext,
        "iv": iv,
        "tag": tag,
        "recipients": [
            {
                "encrypted_key": encrypted_key,
                "header":{
                    "alg": jwk.alg,
                    "kid": jwk.kid,
                    "ek": ek
                },
            }
        ]
    })


def decrypt_key_encryption(private_key: str, jwe: str) -> bytes:
    """
    Decrypt the given ciphertext using the given private key.
    """
    _public_key_r, secret_key_r = import_private_key(private_key)
    jwe_json = json.loads(jwe)

    encrypted_key = base64url_no_padding_decode(jwe_json["recipients"][0]["encrypted_key"])
    ek = base64url_no_padding_decode(jwe_json["recipients"][0]["header"]["ek"])

    content_encryption_key = hpke.open(ek, secret_key_r, b"", b"", encrypted_key)

    nonce = base64url_no_padding_decode(jwe_json["iv"])
    tag = base64url_no_padding_decode(jwe_json["tag"])
    ciphertext = base64url_no_padding_decode(jwe_json["ciphertext"])

    ciphertext_with_tag = ciphertext + tag
    aad = jwe_json["protected"].encode(encoding='utf-8')

    aesgcm = AESGCM(content_encryption_key)
    plaintext = aesgcm.decrypt(nonce, ciphertext_with_tag, aad)

    return plaintext    