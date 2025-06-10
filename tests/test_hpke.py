"""
This module contains the tests for the HPKE operations.
"""

import hybrid_pke

# flake8: noqa
# pylint: disable=all
# mypy: ignore-errors

def test_hpke():
    """
    Test the HPKE operations.
    """
    hpke = hybrid_pke.default(
      mode=hybrid_pke.Mode.BASE, 
      kem=hybrid_pke.Kem.DHKEM_P256,
      kdf=hybrid_pke.Kdf.HKDF_SHA256,
      aead=hybrid_pke.Aead.AES_128_GCM
    )
    info = b""  # shared metadata, correspondance-level
    aad = b""  # shared metadata, message-level
    secret_key_r, public_key_r = hpke.generate_key_pair()
    assert secret_key_r is not None
    assert public_key_r is not None

    first_byte = public_key_r[0]
    assert first_byte == 0x04, f"Expected first byte to be 0x04, got {hex(first_byte)}"
    x_coord = public_key_r[1:33]  # Skip first byte (0x04) and take next 32 bytes
    y_coord = public_key_r[33:65]  # Take last 32 bytes
    assert len(x_coord) == 32, f"Expected x coordinate to be 32 bytes, got {len(x_coord)}"
    assert len(y_coord) == 32, f"Expected y coordinate to be 32 bytes, got {len(y_coord)}"
    assert len(secret_key_r) == 32, f"Expected secret key to be 32 bytes, got {len(secret_key_r)}"

    message = b"hello from the other side!"
    encap, ciphertext = hpke.seal(public_key_r, info, aad, message)

    plaintext = hpke.open(encap, secret_key_r, info, aad, ciphertext)

    assert plaintext is not None
    assert plaintext.decode("utf-8") == message.decode("utf-8")
