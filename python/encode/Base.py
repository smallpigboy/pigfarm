'''
    Base系列编码
        2020 1 21 15:27 
    @焱灬火火火 
'''

class Base():
    '''
        Decode:解码
        Encode:编码
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
    
    def Mhex(self, a):
        '''
            将字符转换为2位16进制数
            args{
                a: 要转换的字符
            }
        '''
        a = hex(ord(a))

        return a[-2:]
        
    def Encode(self, text = "", blank = ' ', mode = 1):
        '''
            对输入的字符串编码
            args{
                text:要编码的字符串
                blank:分隔符
                mode:模式
            }
        '''

        self.code = ''

        for i in text:
            self.code += self.Mhex(i) + blank
        
        self.Output("BASE16编码:" + self.code)

    def MBin(self, a):
        '''
            将输入的数字转换为二进制
            args{
                a: 要转换的字符
            }
        '''
        a = ord(a)
        if (a >= ord('a')) and (a <= ord('f')): 
            return 10 + a - ord('a')
        elif (a >= ord('0')) and (a <= ord('9')): 
            return a - ord('0')
        else : 
            return -1
        
    def Decode(self, text = "",blank = ' ', mode = 1):
        '''
            对输入的字符串解码
            args{
                text:要解码的字符串
                mode:模式
            }
        '''
        section = []
        section = text.split(blank)
        self.mcode = ''

        for i in section:
            num = 0
            j = 0
            while j < len(i):
                num += pow(16,j) * self.MBin(i[len(i) - j - 1])
                j += 1
            self.mcode += chr(num)

        self.Output("BASE16解码:" + self.mcode)

if __name__ == '__main__':
    c = Base()
    c.Encode('abcdefghijkl;')
    c.Decode('61 62 63 64 65 66 67 68 69 6a 6b 6c 3b ')