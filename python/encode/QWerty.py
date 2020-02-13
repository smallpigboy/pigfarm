# -*- coding: utf-8 -*-
"""
2020 1 19 15:57
#键盘加密
@author: 焱灬火火火
"""
d = {
    'q':'a', 'w':'b', 'e':'c', 'r':'d', 't':'e', 'y':'f', 'u':'g', 'i':'h', 'o':'i', 'p':'j',
    'a':'k', 's':'l', 'd':'m', 'f':'n', 'g':'o', 'h':'p', 'j':'q', 'k':'r', 'l':'s',
    'z':'t', 'x':'u', 'c':'v', 'v':'w', 'b':'x', 'n':'y', 'm':'z',
    'Q':'A', 'W':'B', 'E':'C', 'R':'D', 'T':'E', 'Y':'F', 'U':'G', 'I':'H', 'O':'I', 'P':'J', 
    'A':'K', 'S':'L', 'D':'M', 'F':'N', 'G':'O', 'H':'P', 'J':'Q', 'K':'R', 'L':'S', 
    'Z':'T', 'X':'U', 'C':'V', 'V':'W', 'B':'X', 'N':'Y', 'M':'Z', 
    }

class QWerty():
    '''
        Encrypt:加密
        Decrypt:解密
        FindKey:找到值在字典中对应的key
    '''

    def __init__(self): 
        pass 

    def FindKey(self, odict, c):
        '''
            找到值c在字典odict中对应的key 若没找到则返回None
            {
                odict:需要查找的字典
                c:    需要查找的值
            }
        '''
        for k in odict:
            if odict[k] == c: 
                return k
        return None

    def Encrypt(self, text = ""):
        '''
            对输入字符串加密
            args{
                text: 需要加密的字符串
            }
        '''

        self.CiperText = ''
        for i in text:
            self.CiperText += d[i]

        self.Output("键盘加密:" + self.CiperText)
        
    def Decrypt(self, text = ""):
        '''
            对输入字符串解密
            args{
                text: 需要解密的字符串
            }
        '''

        self.PlainText = ''
        for i in text:
            self.PlainText += self.FindKey(d, i)

        self.Output("键盘解密:" + self.PlainText)

    def Output(self, strings):
        '''
			作用：输出数据
			args={
				strings：将输出的数据
			}
        '''
        
        print(strings)

if __name__ =='__main__':
    q = QWerty()
    q.Encrypt('qwertyu')
    q.Decrypt('abcd')