# Key Generation

```python
key = generate_key()
public_key = export_public_key(key)
# {"kty": "EC", "use": "enc", "alg": "HPKE-0", "kid": "G5N__CqMv_kJGieGSFuAugvl0jrQJCZ3yKwVK6sUM4o", "crv": "P-256", "x": "gixQJ0qg4Ag-6HSMaIEDL_zbDhoXavMyKlmdn__AQVE", "y": "ZxTgRLWaKONCL_GbZKLNPsW9EW6nBsN4AwQGEFAFFbM"}

private_key = export_private_key(key)
# {"kty": "EC", "use": "enc", "alg": "HPKE-0", "kid": "G5N__CqMv_kJGieGSFuAugvl0jrQJCZ3yKwVK6sUM4o", "crv": "P-256", "x": "gixQJ0qg4Ag-6HSMaIEDL_zbDhoXavMyKlmdn__AQVE", "y": "ZxTgRLWaKONCL_GbZKLNPsW9EW6nBsN4AwQGEFAFFbM", "d": "g2DXtKapi2oN2zL_RCWX8D4bWURHCKN2-ZNGC05ZaR8"}

message = "hello 🌎".encode(encoding='utf-8')
```

# Compact JWE

```python
message = "hello 🌎".encode(encoding='utf-8')
compact_jwe = encrypt_integrated(public_key, message)
# eyJhbGciOiAiSFBLRS0wIiwgImVuYyI6ICJpbnQiLCAia2lkIjogIkc1Tl9fQ3FNdl9rSkdpZUdTRnVBdWd2bDBqclFKQ1ozeUt3Vks2c1VNNG8ifQ.BIh6I40uiBbK8-UK7nHdo3ISEfgwJ_MF3zWjQzLt00GhFF2-1VgWKHSYLXdeVeRV7AinyocYiCYmISvW0yqiDmc..Ov-llz6VUyiw8nZL0OPGLGZckLTm5UcTZFg.
```

# JSON JWE

```python
json_jwe = encrypt_key_encryption(public_key, message)
# {"protected": "eyJlbmMiOiAiQTEyOEdDTSJ9", "ciphertext": "9AxOd65ROJY1cQ", "iv": "2u3NRi3CSr-x7Wuj", "tag": "1NKYSWVV4pw5thsq7t6m6Q", "recipients": [{"encrypted_key": "l9VRW1K5CA037fY2ZqVF4bDej413TaAtfjoe3k89-eI", "header": {"alg": "HPKE-0", "kid": "G5N__CqMv_kJGieGSFuAugvl0jrQJCZ3yKwVK6sUM4o", "ek": "BJl0V6KLl3HOAZbzFwiAL9eaYbFQPg7-ROmIJpluIQjNS5zultZsC4rGhGzmW1GUWG8bzJUWLQtxFF9oze0AKhU"}}]}
```