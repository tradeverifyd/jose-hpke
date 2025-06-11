"""
This module contains the functions to encrypt and decrypt the given plaintext using the given public and private keys.
"""
from hpke.jwe.integrated_encryption import encrypt_integrated, decrypt_integrated
from hpke.jwe.key_encryption import encrypt_key_encryption, decrypt_key_encryption

__all__ = ["encrypt_integrated", "decrypt_integrated", "encrypt_key_encryption", "decrypt_key_encryption"]
