import jwt

JWT_SECRET = 'thesecretoflogin'


def decode_token(token):
    try:
        payload = jwt.decode(token, JWT_SECRET)
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
