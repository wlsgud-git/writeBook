from calendar import week
from lib2to3.pgen2.tokenize import TokenError
from os import access
from xml.sax.handler import all_properties
from itsdangerous import Serializer, base64_decode
import jwt, datetime
from rest_framework.authentication import exceptions
from writeBook.settings import SECRET_KEY, JWT_ALGORITHM

# 로그인 jwt 토큰 만들기
def create_access_token(email, admin):
    payload = {
        'email' : email,
        'admin' : admin
    }
    try:
        exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
    except TokenError:
        raise Exception('error')
    payload['exp'] = exp
    payload['iat'] = datetime.datetime.utcnow()
    access_token = jwt.encode(payload, SECRET_KEY, JWT_ALGORITHM)
    return access_token

def create_refresh_token(email, admin):
    payload = {
        'email' : email,
        'admin' : admin
    }
    try:
        exp = datetime.datetime.utcnow() + datetime.timedelta(seconds=300)
    except TokenError:
        raise Exception('error')
    
    payload['exp'] = exp
    payload['iat'] = datetime.datetime.utcnow()
    refresh_token = jwt.encode(payload, SECRET_KEY, JWT_ALGORITHM)

    return refresh_token

# JWT토큰 검사하기

def decode_access_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, leeway=datetime.timedelta(seconds=10), algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False

def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, leeway=datetime.timedelta(seconds=10) ,algorithms=["HS256"])
        return {"email": payload['email'], 'admin': payload['admin']}
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False


# def CheckTokenExp(time):
#     print("일단 여기가지 옴")
#     if time <= datetime.datetime.utcnow():
#         print("만료된 토큰 이라능")
#     else:
#         print('no')
#     return True
