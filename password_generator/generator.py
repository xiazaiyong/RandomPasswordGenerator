import random
import string
from .exceptions import *

class RandomPasswordGenerator:
    # 随机密码生成类
    
    DEFAUT_LENGTH = 12
    MAX_LENGTH = 128
    MIN_LENGTH = 4

    """
        随机密码长度：默认12位
        默认包含大写、小写和数字
        默认不包含符号
    """

    def __init__(self):
        self.lower_case = True  #大写
        self.upper_case = True  #小写
        self.use_digits = True  #数字
        self.use_symbols = False    #符号
        self.use_readability = False     #可读性，每四个字符之间使用‘-’连接

    def generate(self, length = None):
        '''
        args:
            length 生成密码的长度,为空时使用默认值12
        return:
            str 生成的密码
        raise:
            ValueError  请求的密码长度超出生成范围
        '''

        if length is None:
            length = self.DEFAUT_LENGTH

        if length > 4:
            self.use_readability = True

        if not self.MIN_LENGTH <= length <= self.MAX_LENGTH:
            raise InvalidLengthError(length, self.MIN_LENGTH, self.MAX_LENGTH)

        #构建密码池
        chars_pool = list()
        password_bit = self.DEFAUT_LENGTH
        if self.lower_case:
            chars_pool += string.ascii_lowercase
        if self.upper_case:
            chars_pool += string.ascii_uppercase

        if self.use_digits:
            chars_pool += string.digits

        if self.use_symbols:
            chars_pool += string.punctuation

        if not chars_pool:
            raise NoCharacterSetError()

        password_chars = []
        for i in range(password_bit):
            if i!=0 and i%4==0:
                password_chars.append('-')
            password_chars.append(random.choice(chars_pool))
            
        return ''.join(password_chars)


