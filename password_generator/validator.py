class PasswordStrength:
    #密码强度评估

    WEAK = 1
    MEDIUM = 2
    STRONG = 3

    @classmethod
    def check(cls, password):
        """
        评估密码强度
        returns:
            tuple:(强度等级,建议列表)   
        """

        suggestions = []
        score = 0
        
        #长度检查
        if len(password) >= 12:
            score += 1
        elif len(password) >= 8:
            score += 0
        else:
            suggestions.append("密码长度建议至少8位")

        #字符多样性检查
        has_uppercase = any(c.isupper() for c in password)
        has_lowercase = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        # has_symbol = any(c.() for c in password)

        variety_count = sum([has_uppercase, has_lowercase, has_digit])
        if variety_count >= 3:
            score += 2
        elif variety_count >=2:
            score += 1
        else:
            suggestions.append("建议密码中包含大小写字母和数字")

        if score <=1:
            return cls.WEAK, suggestions
        elif score <=2:
            return cls.MEDIUM, suggestions
        else:
            return cls.STRONG, suggestions