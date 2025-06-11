# flake8: noqa
# pylint: disable=all
# mypy: ignore-errors

from hpke.jwk import generate_key, export_public_key, export_private_key
from hpke.jwe import encrypt_integrated, decrypt_integrated, encrypt_key_encryption, decrypt_key_encryption


def line_wrap_for_rfc(text: str) -> str:
    """
    Line wrap the given text for RFC compliance.
    """
    return "\n".join(text.split("\n"))

def test_make_markdown_examples():
    """
    Test the make_markdown_examples function.
    """
    key = generate_key()
    public_key = export_public_key(key)
    private_key = export_private_key(key)

    message = "hello 🌎".encode(encoding='utf-8')
    compact_jwe = encrypt_integrated(public_key, message)
    plaintext = decrypt_integrated(private_key, compact_jwe)
    assert plaintext == message

    json_jwe = encrypt_key_encryption(public_key, message)
    plaintext = decrypt_key_encryption(private_key, json_jwe)
    assert plaintext == message

    markdown = f"""
# Private Key
```json
{private_key}
```

# Compact JWE
```python
{compact_jwe}
```

# JSON JWE
```python
{json_jwe}
```
    """.strip()
    print(markdown)


