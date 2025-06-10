"""
This module contains the tests for the JSON Web Key (JWK) operations.
"""

import json

# flake8: noqa
# pylint: disable=all
# mypy: ignore-errors

from hpke.jwk import JWK, generate_key, export_public_key, export_private_key, import_public_key, import_private_key

def test_generate_key():
    """
    Test the generate_key function.
    """
    # Test generating a key with default parameters
    key = generate_key()
    assert key.kty == "EC"
    assert key.use == "enc"
    assert key.alg == "HPKE-0"
    assert key.kid is not None
    assert key.x is not None
    assert key.y is not None
    assert key.d is not None


def test_export_public_key():
    """
    Test the export_public_key function.
    """
    # Test generating a key with default parameters
    key = generate_key()
    public_key = json.loads(export_public_key(key))
    assert public_key["kty"] == "EC"
    assert public_key["use"] == "enc"
    assert public_key["alg"] == "HPKE-0"
    assert public_key["kid"] is not None
    assert public_key["x"] is not None
    assert public_key["y"] is not None
    assert public_key.get("d") is None

def test_export_private_key():
    """
    Test the export_private_key function.
    """
    # Test generating a key with default parameters
    key = generate_key()
    private_key = json.loads(export_private_key(key))
    assert private_key["kty"] == "EC"
    assert private_key["use"] == "enc"
    assert private_key["alg"] == "HPKE-0"
    assert private_key["kid"] is not None
    assert private_key["x"] is not None
    assert private_key["y"] is not None
    assert private_key["d"] is not None


def test_import_public_key():
    """
    Test the import_public_key function.
    """
    # Test generating a key with default parameters
    key = generate_key()
    public_key = export_public_key(key)
    imported_key = import_public_key(public_key)
    assert len(imported_key) == 65

def test_import_private_key():
    """
    Test the import_private_key function.
    """
    # Test generating a key with default parameters
    key = generate_key()
    private_key = export_private_key(key)
    public_key, private_key = import_private_key(private_key)
    assert len(public_key) == 65
    assert len(private_key) == 32