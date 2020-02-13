# -*- coding: utf-8 -*-
'''
棋盘(Polybius)密码
2020 1 19 17:16
@ 焱灬火火火
'''

d = { 1:"ABCDE", 2:"FGHIK", 3:"LMNOP", 4:"QRSTU", 5:"VWXYZ"}

class Polybius():
    '''
        Encrypt:加密  
        Decrypt:解密
    '''
    def __init__(self):
        pass

    def Output(self, strings):
        '''
			作用：输出数据
			args={
				strings：将输出的数据
			}
        '''
        
        print(strings)

    def Encrypt(self, text = "", blank = ' '):
        '''
            对输入字符串加密
            args{
                text:需要加密的字符串
                blank:间隔符号
            }
        '''
        text = text.upper()
        text = text.replace(blank,"")
        text = text.replace('J','I')

        self.CipherText = ''
        for i in text:
            for k in d:
                j = d[k].find(i)
                if(j != -1): 
                    self.CipherText += chr(ord('0') + k) + chr(ord('1') + j ) + blank
        
        self.Output("Polubius加密:" + self.CipherText)

    def Decrypt(self, text = "", blank = ' '):
        '''
            对输入的字符串解密
            args{
                text:需要解密的字符串
                blank:间隔符号
            }
        '''

        text = text.upper()
        section = []
        section = text.split(blank)
        self.PlainText = ""

        for i in section: 
            k = ord(i[0]) - ord('0')
            j = ord(i[1]) - ord('1')
            self.PlainText += d[k][j]
        
        self.Output("Polybius解密:" + self.PlainText)

if __name__ == '__main__':
    c = Polybius()
    c.Encrypt("ij")
    c.Decrypt("21 31 54")