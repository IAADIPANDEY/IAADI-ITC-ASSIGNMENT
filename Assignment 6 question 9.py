class ParenthesesValidator:
    def isValid(self, str):
        mapping = {'(': ')', '[': ']', '{': '}'}
        lis = []
        for idx in str:
            if idx in '([{':
                lis.append(idx)
            elif len(lis) == 0 or idx != mapping[lis.pop()]:
                return False
        return len(lis) == 0
obj = ParenthesesValidator()
print(obj.isValid("([}])"))