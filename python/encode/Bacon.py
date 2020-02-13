# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 18:22:45 2020
#培根密码
@author: 焱灬火火火
"""

from Cipher import Cipher

class Bacon(Cipher):
    def __init__(self,PlainText='',CipherText='',a='a',b='b'):#PlainText为明文a,b为每组的表示
        Cipher.__init__(self,PlainText,CipherText)
        self.a = a
        self.b = b
        self.dic={'aaaaa':'a','aaaab':'b','aaaba':'c','aaabb':'d','aabaa':'e','aabab':'f','aabba':'g',
                  'aabbb':'h','abaaa':'i','abaab':'j','ababa':'k','ababb':'l','abbaa':'m','abbab':'n',
                  'abbba':'o','abbbb':'p','baaaa':'q','baaab':'r','baaba':'s','baabb':'t','babaa':'u',
                  'babab':'v','babba':'w','babbb':'x','bbaaa':'y','bbaab':'z'}
    def FindKey(self,a):#找到值对应的键
        for k in self.dic:
            if self.dic[k] == a:
                return k
        return ''
    def Encryption(self):#加密
        text=str(self.PlainText.lower())
        print(text)
        text = text.replace(' ','')
        print(text)
        text.lower()
        print(text)
        s=''
        for i in text:
            s += self.FindKey(i)
        return s
    def Decryption(self):#解密
        text=str(self.CipherText)
        text = text.replace(' ','')
        text.lower()
        text = text.replace(self.a,'a')
        text = text.replace(self.b,'b')
        i = 0
        s = ''
        while i <len(text):
            s += self.dic[text[i:i+5]]
            i = i + 5 
        return s
'''test 
c=Bacon(CipherText='000000000100010000110010000101',a='0',b='1')
c.DecryptionPlainText()
print(c.PlainText)
'''