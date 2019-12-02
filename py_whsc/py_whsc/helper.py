#
__author__ = 'bob'
__date__ = '2019/6/26 9:25'
import hashlib


def make_password(pwd_str):
    return hashlib.md5(('@&$whsc' + pwd_str + 'whsc$&@').encode()).hexdigest()
