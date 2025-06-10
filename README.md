# jose-hpke

[![Python Tests](https://github.com/tradeverifyd/jose-hpke/actions/workflows/ci.yaml/badge.svg)](https://github.com/tradeverifyd/jose-hpke/actions/workflows/ci.yaml)

This is a Python implementation of the [draft-ietf-jose-hpke-encrypt-08](https://datatracker.ietf.org/doc/html/draft-ietf-jose-hpke-encrypt-08) specification.

This implementation is based on the [hybrid-pke](https://github.com/capeprivacy/hybrid-pke) library.

Only a subset of the JWE is implemented, and only the HPKE-0 algorithm is supported.

⚠️ This implementation is not yet ready for production use.

## Usage

```python
from hpke.jwk import generate_key
from hpke.jwe import encrypt_integrated, decrypt_integrated

key = generate_key()
public_key = export_public_key(key)
# {"kty":"EC","crv":"P-256","alg": "HPKE-0","x":"...","y":"..."}
private_key = export_private_key(key)
# {"kty":"EC","crv":"P-256","alg": "HPKE-0","x":"...","y":"...","d":"..."}

jwe = encrypt_integrated(public_key, b"Hello world!")
# eyJhbGciOiAiSFBLRS0wIiwgImVuZCI6ICJpbnQiLCAia2lkIjogIlRWU1MzNzFWUjhiVEJkUUJya01fMmtONnM3ZFBGUnZROTREa2ZSbmlLeFUifQ.BO1RFLhRhrtHILUVvi8iSswMbaO6Wi8xYFs2K-5TPi7MTK80C_viaMxYNRK2kC8x69Uh34XQ4hVjcyonvTtRtmY..pNB47pv2AHkHgIRHrxtrigG7dzKrKmrHc9-a_KjuvOzat1y4XW4GPbRP.

plaintext = decrypt_integrated(private_key, jwe)
print(plaintext) # b"Hello world!"
```

## Credits

- [hybrid-pke](https://github.com/capeprivacy/hybrid-pke)
- [RFC 9180](https://www.rfc-editor.org/rfc/rfc9180)
- [draft-ietf-jose-hpke-encrypt-08](https://datatracker.ietf.org/doc/html/draft-ietf-jose-hpke-encrypt-08)