# def reverse_words(text):
#     return ' '.join(word[::-1] for word in text.split(' '))



# def solution(number):
#     return sum([num for num in range(number) if num % 3 == 0 or num % 5 == 0])



# def is_anagram(test, original):
#     if sorted(test.lower()) == sorted(original.lower()):
#         return True
#     else:
#         return False



# from preloaded import MORSE_CODE
# def decode_morse(morse_code):
#     # Remember - you can use the preloaded MORSE_CODE dictionary:
#     # For example: 
#     # MORSE_CODE['.-'] = 'A'
#     # MORSE_CODE['--...'] = '7'
#     # MORSE_CODE['...-..-'] = '$'
#     words = []
#     for word in morse_code.split('   '):
#         if not word.strip():
#             continue
#         words.append(''.join(MORSE_CODE[letter] for letter in word.split()))
#     return ' '.join(words)



# def create_two_sets_of_equal_sum(n): 
#     ## Divide the numbers 1,2,…,n into two sets of equal sum.
#     ## If it's not possible, return [ ] or ( ).
#     sum_of_n = n * (n + 1) // 2
#     if sum_of_n % 2 != 0:
#         return ()
#     else:
#         target = sum_of_n // 2
#         set1 = []
#         set2 = []
#         for num in range(n, 0, -1):
#             if num <= target:
#                 set1.append(num)
#                 target -= num
#             else:
#                 set2.append(num)
#     return set1, set2



# def solution(s):
#     s = ''.join(f" {i}" if i.isupper() and index > 0 else i for index, i in enumerate(s))
#     return s



# def likes(names):
#     # your code here
#     if names == []:
#         return f"no one likes this"
#     elif len(names) == 1:
#         return f"{names[0]} likes this"
#     elif len(names) == 2:
#         return (' and '.join(name for name in names)) + ' like this'
#     elif len(names) == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     else:
#         return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
    


# def delete_nth(order,max_e, new_list = []):
#     if order == []:
#         return new_list
#     if new_list.count(order[0]) == max_e:
#         return delete_nth(order[1:], max_e, new_list)
#     else:
#         new_list.append(order[0])
#         return delete_nth(order[1:], max_e, new_list)
# print(delete_nth([30, 7, 17, 30, 30, 23, 23, 30, 30, 23, 7, 45, 45, 7, 7, 39, 45, 17, 7, 39, 17, 39, 17, 30, 23, 30, 17, 17, 17, 17, 23, 17, 7, 39, 30, 7, 23, 23, 22, 23, 17, 7, 30, 45, 17, 7, 7], 5))