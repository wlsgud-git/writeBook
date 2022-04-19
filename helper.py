import re
import random
# 비밀번호 유효성 검사 알고리즘
def pwValidate(password):
    if len(password) < 8 or not re.findall("[0-9]+", password) or not re.findall("[a-z]+", password) or not re.findall("[`~!@#$%^&*(),<.>/?]+", password):return False

    return True

# def getAuthenticatedNumber():


