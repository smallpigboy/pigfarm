# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:20:57 2020
#转轮机密码
@author: 焱灬火火火
"""

#慢速轮
SWhell = {24:21, 25:3, 26:15, 1:1, 2:19, 3:10, 4:14, 5:26, 6:20, 7:8, 8:16, 9:7, 10:22,
          11:4, 12:11, 13:5, 14:17, 15:9, 16:12, 17:23, 18:18,19:2, 20:25, 21:6, 22:24, 23:13}

#中速轮
MWhell = {26:20, 1:1, 2:6, 3:4, 4:15, 5:3, 6:14, 7:12, 8:23, 9:5, 10:16,11:2, 12:22, 13:19,
           14:11, 15:18, 16:25, 17:24, 18:13, 19:7, 20:10, 21:8, 22:21, 23:9, 24:26, 25:17}

#快速轮
QWhell = {1:8, 2:18, 3:26, 4:17, 5:20, 6:22, 7:10, 8:3, 9:13, 10:11, 11:4, 12:23, 13:5,
          14:24, 15:9, 16:12, 17:25, 18:16,19:19, 20:6, 21:15, 22:21, 23:2, 24:7, 25:1, 26:14}

class Turbine():    
    '''
        FindIndex：  找到字典中值所对应的关键字
        FindIndexK:  找到字典中关键字的下标
        OutIndex:    找到字典中关键字的下标
        Rotate:      字典循环往后移动1
        Encrypt:     加密方式
        Decrypt:解密方式
    '''
    
    def __init__(self):
        pass
        
    def FindIndex(self,oridict,c):
        '''
            找到字典中值所对应的关键字
            args{
                    oridict:操作字典
                    c:      值
                }
        '''
        b = []
        for k in oridict:
            b.append(oridict[k])
        i = 0
        while i<len(b):
            if(b[i] == c):
                return i
            else:
                i = i + 1
        return -1#字典中没有c
    
    def FindIndexK(self,oridict,c):
        '''
            找到字典中关键字的下标
            args{
                    oridict:操作字典
                    c:      关键字
                }
        '''
        b = []
        for k in oridict:
            b.append(k)
        i = 0
        while i<len(b):
            if(b[i] == c):
                return i
            else:
                i = i + 1
        return -1#字典中没有c
    
    def OutIndex(self,oridict,c):
        '''
            找到字典中下标对应的关键字
            args{
                    oridict:操作字典
                    c:      下标
                }
        '''
        a = []
        for k in oridict:
            a.append(k)
        return a[c]

    def Rotate(self,oridict):
        '''
            字典循环往后移动1
            args{
                    oridict:操作字典
                }
        '''
        a = []
        for k in oridict:#得到字典的key值
            a.append(k)
        a.insert(0,a.pop())#将最后一个元素移到第一个
        slicedict={k:oridict[k] for k in a}
        return slicedict
        
    def Encrypt(self,text = ""):#加密
        '''
            对输入字符串加密
            args{
                    text:用于加密的字符串
                }
        '''
        text = text.lower()
        text = text.replace(' ','')
        a = 0#快速轮的圈数
        b = 0#中速轮的圈数
        self.CiperText = ""
        SSWhell = SWhell
        MMWhell = MWhell
        QQWhell = QWhell
        for i in text:
            n = ord(i) - ord('a')#得到慢速轮下标
            n = self.OutIndex(SSWhell,n)#慢速轮中找到下标为n的key
            n = self.FindIndex(SSWhell,n)#慢速轮中得到值与n相同的下标      
            n = self.OutIndex(MMWhell,n)#中速轮中找到下标为n的key
            n = self.FindIndex(MMWhell,n)#中速轮中得到值与n相同的下标
            n = self.OutIndex(QQWhell,n)#快速轮中找到下标为n的key
            n = self.FindIndex(QQWhell,n)#快速轮中得到值与n相同的下标
            self.CiperText += chr(n + ord('a'))
            self.Rotate(QQWhell)#快速轮转一圈
            a += 1
            if a/26:
                self.Rotate(MMWhell)
                a = 0
                b += 1
                if b/26:
                    self.Rotate(SSWhell)
                    b = 0
        self.Output("加密:" + self.CiperText)

    def Decrypt(self,text = ""):
        '''
            对输入字符串解密
            args{
                    text:用于解密的字符串
                }
        '''
        text = text.lower()
        text = text.replace(' ','')
        a = 0#快速轮的圈数
        b = 0#中速轮的圈数
        self.PlainText = ""
        SSWhell = SWhell
        MMWhell = MWhell
        QQWhell = QWhell
        for i in text:
            n = ord(i) - ord('a')          
            n = self.OutIndex(QQWhell,n)#得到下标对应的关键字
            n = self.FindIndexK(QQWhell,QQWhell[n])#找到关键字的下标
            self.Rotate(QQWhell)
            a += 1
            if a/26:
                self.Rotate(MMWhell)
                a = 0
                b += 1
                if b/26:
                    self.Rotate(SSWhell)
                    b = 0
            n = self.OutIndex(MMWhell,n)#得到下标对应的关键字
            n = self.FindIndexK(MMWhell,MMWhell[n])#找到关键字的下标
            n = self.OutIndex(SSWhell,n)#得到下标对应的关键字
            n = self.FindIndexK(SSWhell,SSWhell[n])#找到关键字的下标
            self.PlainText += chr(n + ord('a'))
        self.Output("解密:" + self.PlainText)
        
    def Output(self, strings):
        '''
			作用：输出数据
			args={
				strings：将输出的数据
			}
        '''       
        print(strings)
        
if __name__ == '__main__':
    c = Turbine()
    c.Encrypt("A bcD")
    c.Decrypt("biet")