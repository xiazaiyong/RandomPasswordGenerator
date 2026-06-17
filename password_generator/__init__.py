"""
随机密码生成器
默认生成密码长度：12
可选密码长度：12到128位
可选复杂度：大小写、数字、符号
默认复杂度：大小写+数字
"""
from .generator import RandomPasswordGenerator
from .validator import PasswordStength
from .exceptions import (
    PasswordGeneratorError,
    InvalidLengthError,
    NoCharacterSetError
)

__version__ = '0.1.0'
__all__ = [
    'RandomPasswordGenerator',
    'PasswordStength',
    'PasswordGeneratorError'
    'InvalidLengthError',
    'NoCharacterSetError'
]