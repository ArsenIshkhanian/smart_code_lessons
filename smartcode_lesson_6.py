# def solver(list_char, combination):
#     if list_char == []:
#         return True
#     for i in range(len(list_char) - 1):
#         comb = f'{list_char[i]}{list_char[i + 1]}'
#         if comb in combination:
#             list_char.pop(i + 1)
#             list_char.pop(i)
#             return solver(list_char, combination)
#         else:
#             continue
#     return False


# # text = '((()))'
# text = '([])[{[]}]'
# # text = '({])'
# # text = ')({[)})'
# # text = '()({({)})}'
# # text = '({{)}}'
# combination = ['[]', '()', '{}']
# list_char = [i for i in text]
# print(solver(list_char, combination))