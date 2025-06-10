"""
This module contains the functions to encrypt and decrypt the given plaintext using the given public and private keys.
"""
from hpke.jwe.integrated_encryption import encrypt_integrated, decrypt_integrated

__all__ = ["encrypt_integrated", "decrypt_integrated"]
