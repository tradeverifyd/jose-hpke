
"""
This module contains the functions to encode and decode base64url strings.
https://gist.github.com/cameronmaske/f520903ade824e4c30ab
"""

import base64


def base64url_no_padding_encode(string):
    """
    Removes any `=` used as padding from the encoded string.
    """
    encoded = base64.urlsafe_b64encode(string).decode(encoding='utf-8')
    return encoded.rstrip("=")


def base64url_no_padding_decode(string):
    """
    Adds back in the required padding before decoding.
    """
    padding = 4 - (len(string) % 4)
    string = string + ("=" * padding)
    return base64.urlsafe_b64decode(string)