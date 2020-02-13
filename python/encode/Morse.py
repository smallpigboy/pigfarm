# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 09:15:31 2020
#摩斯密码
@author: 焱灬火火火
"""

from Cipher import Cipher

class Morse(Cipher):
    def __init__(self,PlainText='',CipherText=''):#PlainText为明文 num为每段的字符个数
        self.PlainText  = PlainText.lower()
        self.CipherText = CipherText.lower()
        self.Alphabet={'.-':'a','-...':'b','-.-.':'c','----':'ch','-..':'d','.':'e',
                       '..-.':'f','--.':'g','....':'h','..':'i','.---':'j','-.-':'k',
                       '.-..':'l','--':'m','-.':'n','---':'o','.--.':'p','--.-':'q',
                       '.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w',
                       '-..-':'x','-.--':'y','--..':'z','.----':'1','..---':'2',
                       '...--':'3','....-':'4','.....':'5','-....':'6','--...':'7',
                       '---..':'8','----.':'9','-----':'0'}
    def FindKey(self,a):#找到a的键值
        for k in self.Alphabet:
            if self.Alphabet[k] == a:
                return k
        return -1
    
    def Encryption(self):#加密
        text=self.PlainText
        en=''
        slist=text.split(' ')
        for s in slist:
            for c in s:
                d = self.FindKey(c)
                if d != -1:
                    en = en + d + ' '
        return en.rstrip()
    
    def Decryption(self):#解密
        text=self.CipherText
        slist=text.split(' ')
        en = ''
        for s in slist:
            en = en + self.Alphabet[s]
        return en.rstrip()
'''test
c=Morse('123 456 789')
c.EncryptionCipherText()
print(c.CipherText)
c.DecryptionPlainText()
print(c.PlainText)
'''