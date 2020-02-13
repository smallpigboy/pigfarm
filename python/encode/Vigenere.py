# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:02:02 2020
#维吉尼亚密码
@author: 焱灬火火火
"""

from Cipher import Cipher

class Vigenere(Cipher):
    def __init__(self,PlainText='',CipherText='',secret=''):#PlainText为明文 为偏移量
         Cipher.__init__(self,PlainText,CipherText)
         self.secret = secret
    def Encryption(self):#加密
        text = self.PlainText.upper()
        secret = self.secret.upper()
        s = ''
        i = 0
        while i < len(text):
            a = chr((ord(text[i]) + ord(secret[i]) - 2 * ord('A'))%26 + ord('A'))
            s += a
            i = i+1
        return s
    def Decryption(self):#解密
        text = self.CipherText.upper()
        secret = self.secret.upper()
        s = ''
        i = 0
        while i < len(text):
            a = chr((ord(text[i]) - ord(secret[i]) )%26 + ord('A'))
            s += a
            i = i+1
        return s
'''test
c = Vigenere(PlainText='ATTACKATDAWN',secret='LEMONLEMONLE')
c.EncryptionCipherText()
print(c.CipherText)
c.DecryptionPlainText()
print(c.PlainText)
'''