# flake8: noqa
# pylint: disable=all
# mypy: ignore-errors

from hpke.jwk import generate_key, export_public_key, export_private_key
from hpke.jwe import encrypt_integrated, decrypt_integrated


def test_integrated_encryption_decryption():
    """
    Test the integrated encryption and decryption.
    """
    # Test generating a key with default parameters
    key = generate_key()
    public_key = export_public_key(key)
    private_key = export_private_key(key)

    message = b"hello from the other side!"
    jwe = encrypt_integrated(public_key, message)
    print(jwe)
    plaintext = decrypt_integrated(private_key, jwe)
    assert plaintext == message