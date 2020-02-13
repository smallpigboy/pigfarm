# -*- coding: utf-8 -*-
"""
栅栏密码
Created on Sat Jan 18 18:32:03 2020

@author: 焱灬火火火
"""

class RailFence():
    '''
		Encrypt:    加密
		Decrypt:    解密
        Encryption: 加密方法
        Decryption: 解密方法
	'''
    
    def __init__(self):
        pass
    
    def Encrypt(self, text = "",num=1, mode = 0):#加密
        '''
            对输入字符串进行加密
			args={
				text：用于加密的字符串
                num： 密文段数
				mode：说明加密模式 0 or 1 默认形式 orWWW型； 2 两种形式		
			}
		'''
        
        if mode == 0 or mode == 1:
            self.__Encryption(text, num, mode)
            
        elif mode == 2:
            self.__Encryption(text, num, mode = 0)
            self.__Encryption(text, num, mode = 1)
            
        else:
            self.Output("ERROR mode!")
            
    def Decrypt(self, text = "",num=1, mode = 0):#解密
        '''
            对输入字符串进行解密
			args={
				text：用于解密的字符串
                num： 密文段数
				mode：说明解密模式 0 or 1 默认形式 orWWW型  2 两种形式		
			}
		'''
        if mode == 0 or mode == 1:
            self.__Decryption(text, num, mode)
            
        elif mode == 2:
            self.__Decryption(text, num, mode = 0)
            self.__Decryption(text, num, mode = 1)
        
        else:
            self.Output("ERROR mode!")
            
            
    def __Encryption(self, text = "",num=1, mode = 0):#加密方法
        '''
			对输入字符串进行加密
			args={
				text：用于加密的字符串
                num： 密文段数
				mode：说明加密模式			
			}
		'''
        
        self.PlainText = text
        
        #默认形式加密
        if mode == 0:    
            section = []
            i=0
            while i < num:#将字符串分成num段放到section中
                section.append(text[i:len(text):num])
                i = i + 1
            self.CiperText = ""
            i = 0
            while i<num:#把段连接起来
                self.CiperText = self.CiperText + section[i]
                i = i + 1
            self.Output("默认形式加密:" + self.CiperText)
            
        #WWW型加密
        elif mode == 1:
            section = []
            
            for i in range(num):
                section.append('')
            i = 0
            while i < len(text):
                j = 0
                for j in range(num):#先输入W的\
                    if i >= len(text):
                        break
                    section[j] += text[i]
                    i = i + 1
                for j in range(1,num-1):#在输入W的/
                    if i >= len(text):
                        break
                    section[num-1-j] += text[i]
                    i = i + 1
            self.CiperText = ""
            for s in section:
                self.CiperText += s
            self.Output("加密:" + self.CiperText)

    def __Decryption(self, text = "",num=1, mode = 0):
        '''
			对输入字符串进行解密
			args={
				text：用于解密的字符串
                num： 密文段数
				mode：说明解密模式			
			}
		'''
        self.CiperText = text
        
        if mode == 0:     
            section = []
            i = 0
            while i < num:#将字符串分成num段放到section中  得到每段的长度
                section.append(text[i:len(text):num])
                i = i + 1
            re = []
            i = 0
            j = 0
            while i < num:
                re.append(text[j:j+len(section[i])])
                j = j + len(section[i])
                i = i + 1 
            self.PlainText = ""
            i = 0
            while len(re):#把段连接起来
                j = 0
                while j < len(re):
                    if(len(re[j]) != 0):
                        self.PlainText = self.PlainText + re[j][0]
                        re[j] = re[j][1:]
                    else:
                        re.pop(j)
                    j = j + 1
                i = i + 1
            self.Output("默认形式解密:" + self.PlainText)
            
        elif mode == 1:
            section = []
            for i in range(num):
                section.append('')
            i = 0
            while i < len(text):#得到每段的长度
                j = 0
                for j in range(num):#先输入W的\
                    if i >= len(text):
                        break
                    section[j] += text[i]
                    i = i + 1
                for j in range(1,num-1):#在输入W的/
                    if i >=len(text):
                        break
                    section[num-1-j] += text[i]
                    i = i + 1
            re = []
            j = 0
            for i in section:#得到每一段
                re.append(text[j:j+len(i)])
                j = j + len(i)
            self.PlainText = ""
            i = 0
            while num != 0:#按W形式遍历
                for j in range(num):#先输入W的\
                    if len(re) == 0:
                        break
                    if len(re[j]) == 0:
                        re.pop(j)
                        num -=1
                        break
                    self.PlainText += re[j][0]
                    re[j] = re[j][1:]
                for j in range(1,num-1):#在输入W的/
                    if len(re) == 0:
                        break
                    if len(re[j]) == 0:
                        re.pop(j)
                        num -= 1
                        break
                    self.PlainText += re[num-1-j][0]
                    re[num-j-1] = re[num-j-1][1:]
            self.Output("WWW型解密:" + self.PlainText)
            
        else:
            self.Output("ERROR mode!")
            
    def Output(self, strings):
        '''
			作用：输出数据
			args={
				strings：将输出的数据
			}
        '''
        
        print(strings)
        
if __name__ == '__main__':
    c = RailFence()
    c.Encrypt("123456789", 3, mode = 2)
    c.Decrypt("147258369", 3, mode = 2)