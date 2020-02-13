# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 23:36:30 2020

@author: 焱灬火火火
"""

class Cipher(object):
   #CipherText密文PlainText明文 
    def __init__(self,PlainText='',CipherText=''):#初始化明文
        self.PlainText  = PlainText
        self.CipherText = CipherText
    def GetCipherText(self):#返回密文
        return self.CipherText
    
    def GetPlainText(self):#返回明文
        return self.PlainText
    
    def SetPlainText(self,PlainText = ''):#设置明文
        self.PlainText = PlainText
        
    def SetCipherText(self,CipherText = ''):#设置密文
        self.CipherText=CipherText
    
    def Decryption(self):#加密函数
        pass
    
    def Encryption(self):#解密函数
        pass
    
    def EncryptionCipherText(self):#求密文
        self.CipherText =  self.Encryption()
        
    def DecryptionPlainText(self):#解密文
        self.PlainText = self.Decryption()
        
    def BruteForce(self):#暴力破解
        pass