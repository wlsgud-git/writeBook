from calendar import week
from lib2to3.pgen2.tokenize import TokenError
from os import access
from itsdangerous import Serializer
import jwt, datetime
from writeBook.settings import SECRET_KEY, JWT_ALGORITHM

def create_access_token(payload):
    try:
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    except TokenError:
        raise Exception('error')
    payload['exp'] = exp
    payload['iat'] = datetime.datetime.utcnow()
    access_token = jwt.encode(payload, SECRET_KEY, JWT_ALGORITHM)
    return access_token

def create_refresh_token(payload):
    try:
        exp = datetime.datetime.utcnow() + datetime.timedelta(weeks=2)
    except TokenError:
        raise Exception('error')
    
    payload['exp'] = exp
    payload['iat'] = datetime.datetime.utcnow()
    refresh_token = jwt.encode(payload, SECRET_KEY, JWT_ALGORITHM)

    return refresh_token