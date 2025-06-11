# flake8: noqa
# pylint: disable=all
# mypy: ignore-errors

import os
from hpke.jwk import generate_key, export_public_key, export_private_key
from hpke.jwe import encrypt_integrated, decrypt_integrated, encrypt_key_encryption, decrypt_key_encryption

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
# Key Generation

```python
key = generate_key()
public_key = export_public_key(key)
# {public_key}

private_key = export_private_key(key)
# {private_key}

message = "hello 🌎".encode(encoding='utf-8')
```

# Compact JWE

```python
message = "hello 🌎".encode(encoding='utf-8')
compact_jwe = encrypt_integrated(public_key, message)
# {compact_jwe}
```

# JSON JWE

```python
json_jwe = encrypt_key_encryption(public_key, message)
# {json_jwe}
```
    """.strip()

    # with open("docs/usage.md", "w") as f:
    #     f.write(markdown)


