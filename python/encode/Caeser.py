# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 21:11:50 2020
#恺撒密码
@author: 焱灬火火火
"""
from Cipher import Cipher

class Caeser(Cipher):
    def __init__(self,PlainText='',CipherText='',offset=1):#PlainText为明文 offset为偏移量
        Cipher.__init__(self,PlainText,CipherText)
        self.offset = offset
    def Encryption(self):#加密
        s = ''
        for i in self.PlainText:
            s = s + chr(ord(i) + self.offset)
        return s
    def Decryption(self):#解密
        s = ''
        for i in self.CipherText:
           s = s + chr(ord(i) - self.offset)
        return s
    def BruteForce(self,min,max):#min为下限 max为上限 偏移值从min到max尝试破解
        cp=[]
        i=min
        while i<=max:
            self.offset=i
            cp.append(self.Decryption())
            i=i+1
        return cp