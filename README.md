# jose-hpke

[![Python Tests](https://github.com/tradeverifyd/jose-hpke/actions/workflows/ci.yaml/badge.svg)](https://github.com/tradeverifyd/jose-hpke/actions/workflows/ci.yaml)

This is a Python implementation of the [draft-ietf-jose-hpke-encrypt-08](https://datatracker.ietf.org/doc/html/draft-ietf-jose-hpke-encrypt-08) specification.

This implementation is based on the [hybrid-pke](https://github.com/capeprivacy/hybrid-pke) library.

Only a subset of the JWE is implemented, and only the HPKE-0 algorithm is supported.

⚠️ This implementation is not yet ready for production use.

## Usage

See [docs/usage.md](docs/usage.md) for usage examples.

## Credits

- [hybrid-pke](https://github.com/capeprivacy/hybrid-pke)
- [RFC 9180](https://www.rfc-editor.org/rfc/rfc9180)
- [draft-ietf-jose-hpke-encrypt-08](https://datatracker.ietf.org/doc/html/draft-ietf-jose-hpke-encrypt-08)