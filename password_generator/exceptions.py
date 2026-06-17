class PasswordGeneratorError(Exception):
    """密码生成器基础异常"""
    pass

class InvalidLengthError(PasswordGeneratorError):
    """长度无效"""
    def __init__(self, length,min_len=4,max_len=128):
        self.length = length
        self.min_len = min_len
        self.max_len = max_len
        message = f"密码长度{length}无效，允许的范围：{min_len} - {max_len}"
        super.__init__(message)

class NoCharacterSetError(PasswordGeneratorError):
    """未启用任何字符集"""
    def __init__(self):
        message = "至少需要启用一种字符类型（大写字母/小写字母/数字/符号）"
        super().__init__(message)