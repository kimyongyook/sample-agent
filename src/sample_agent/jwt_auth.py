import jwt


def decode_access_token(token: str, verification_key: str) -> dict:
    return jwt.decode(
        token,
        verification_key,
        algorithms=["HS256", "RS256"],
    )
