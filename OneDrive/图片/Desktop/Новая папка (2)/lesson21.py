#№1
# def q(qq):
#     return '*' * (len(qq)-4) + qq[-4:]
# print(q("1234123456785678"))

#№2
# def Palindrome(string):
#     qq= 0
#     q= len(string) - 1
#
#     while q >= qq:
#         if not string[qq] == string[q]:
#             return False
#         qq+= 1
#         q -= 1
#     return True
#
#
# print(Palindrome('qq'))

#№3
class Tomato:
    states = {0: 'sprout', 1: 'flower', 2: 'green tomato', 3: 'red tomato'}
    def __init__(self, index):
        self._index = index
        self._state = 0
    