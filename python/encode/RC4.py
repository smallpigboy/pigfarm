# -*- coding: utf-8 -*-
'''
棋盘(Polybius)密码
2020 2 7 17:16
@ 焱灬火火火
'''
class RC4():
    def __init__(self, key):
        '''
            初始化函数
            args{
                key:密钥
            }
        '''
        self.key = key
        pass

    def swap(self, L, a, b):
        '''
            交换列表L中下标a b 的值 
        '''

        t = L[a]
        L[a] = L[b]
        L[b] = t

    def Sinit(self, key = ''):
        '''
            初始化S-box
            args{
                key: 密钥
            }
        '''

        self.s = list(range(256))
        while len(key) < 256:
            key += key
        key = key[:256]
        #print(len(key))
        #print(key)
        i = j = 0

        while i < 256:
            j = (j + ord(key[i]) + self.s[i]) % 256
            self.swap(self.s, i, j)
            i += 1
        #print(self.s)

    def Encrypt_or_Decrypt(self, text = ''):
        '''
            加密或解密
            args{
                text:需要加密或解密的字符串
            }
        '''

        self.Sinit(self.key)

        i = j = 0
        text = list(text)
        print(text)
        length = len(text)
        while length > 0:
            length -= 1
            i = (i + 1) % 256
            j = (j + self.s[i]) % 256
            self.swap(self.s, i, j)
            t = (self.s[i] + self.s[j]) % 256
            text[length] = chr(ord(text[length]) ^ self.s[t])

        s = ''
        for c in text:
            s += c
        return s
        

if __name__ == '__main__':
    a = RC4(key = 'abc')
    #a = RC4(key = '123')
    s = a.Encrypt_or_Decrypt('朱焱好帅啊')
    print(s)
    print(a.Encrypt_or_Decrypt(s))