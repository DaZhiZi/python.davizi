from utils import log

"""
 一个简单的爬虫：
 https://www.cnblogs.com/liez/p/5399967.html
 
 第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。
 密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
 
 http://zhuoqiang.me/password-storage-and-python-example.html
 
 https://www.jianshu.com/p/d54a4f592dc7
"""
import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8) # 64 bits.

    assert 8 == len(salt)
    assert isinstance(salt, str)

    if isinstance(password, 'unicode'):
        password = password.encode('UTF-8')

    assert isinstance(password, str)

    result = password
    for i in range(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result