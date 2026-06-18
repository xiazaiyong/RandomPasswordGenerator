import argparse, sys
from .generator import RandomPasswordGenerator as PasswordGenerator
from .exceptions import InvalidLengthError, NoCharacterSetError
from .validator import PasswordStrength

def main():
    parser = argparse.ArgumentParser(description='生成随机密码')
    parser.add_argument('-l', '--length', type=int, default=12,
                        help='密码长度 (默认: 12)')
    parser.add_argument('-n', '--number', type=int, default=1,
                        help='生成数量 (默认: 1)')
    parser.add_argument('--no-upper', action='store_true', help='排除大写字母')
    parser.add_argument('--no-lower', action='store_true', help='排除小写字母')
    parser.add_argument('--no-digits', action='store_true', help='排除数字')
    parser.add_argument('--symbols', action='store_true', help='包含特殊符号')
    
    args = parser.parse_args()

    gen = PasswordGenerator()
    gen.upper_case = not args.no_upper
    gen.lower_case = not args.no_lower
    gen.use_digits = not args.no_digits
    gen.use_symbols = args.symbols
    
    # 强度等级映射
    strength_text = {
        PasswordStrength.WEAK: '弱',
        PasswordStrength.MEDIUM: '中',
        PasswordStrength.STRONG: '强'
    }
    
    try:
        for _ in range(args.number):
            password = gen.generate(args.length)
            strength ,suggestions = PasswordStrength.check(password)
            print(f"{password} \r\n [强度: {strength_text[strength]}]{suggestions}")
    except InvalidLengthError:
        print(f"错误: 密码长度必须在 {gen.MIN_LENGTH}-{gen.MAX_LENGTH} 之间", file=sys.stderr)
        sys.exit(1)
    except NoCharacterSetError:
        print("错误: 至少需要启用一种字符类型", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()