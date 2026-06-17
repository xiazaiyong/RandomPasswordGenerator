import argparse
from .generator import RandomPasswordGenerator as PasswordGenerator

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
    gen.use_uppercase = not args.no_upper
    gen.use_lowercase = not args.no_lower
    gen.use_digits = not args.no_digits
    gen.use_symbols = args.symbols
    
    for _ in range(args.number):
        print(gen.generate(args.length))

if __name__ == '__main__':
    main()