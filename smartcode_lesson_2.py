# exercise 1

# def till_num(num, main_num):
#     if num == 1:
#         return main_num - (num - 1)
#     else:
#         print(main_num - (num - 1))
#         return till_num(num - 1, main_num)
        

# num = int(input("Enter the number: "))
# print(till_num(num, num))


"""--------------------------------------------"""


# exercise 2

# def zip(iter1, iter2, iter3):
#     if iter1 == []:
#         return []
#     else:
#         return [(iter1[0], iter2[0], iter3[0])] + zip(iter1[1: ], iter2[1: ], iter3[1: ])
    

# print(zip([1, 2, 3], 'abc', ('True', 'False', 'True')))


"""--------------------------------------------"""


# exercise 3

# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)


# num = int(input("Enter the number: "))
# print(fibonacci(num))


"""--------------------------------------------"""


#exercise 5

# def recursion(num, memory = {}):
#     if num in memory:
#         return memory[num]
    
#     if num == 1:
#         memory[1] = 1
#         return 1
#     else:
#         result =  num * recursion(num - 1)
#         memory[num] = result
#         return result

# def calculating_math_func(num):
#     factorial = recursion(num)
#     result = factorial / num ** 3
#     result = result ** 10
#     return result



# num = int(input("Enter the number: "))
# print(calculating_math_func(num))


"""--------------------------------------------"""


# exercise 7

# def sum(list_of_args, list_of_list=[], list_of_list_2 = [], sum_of_args=0):
#     print(f"list_of_list = {list_of_list}")
#     print(f"list_of_list_2 = {list_of_list_2}")
#     print(f"sum = {sum_of_args}")
#     if list_of_args == []:
#         return sum_of_args
    
#     if list_of_list == []:
#         pass
#     elif type(list_of_list[0]) == list and len(list_of_list) == 1:
#         sum_of_args += list_of_list[0][0]
#         return sum(list_of_args, list_of_list[0][1:], list_of_list_2, sum_of_args)
#     elif type(list_of_list[0]) == list:
#         return sum(list_of_args, list_of_list[0], list_of_list[1:], sum_of_args)
#     else:
#         sum_of_args += list_of_list[0]
#         return sum(list_of_args, list_of_list[1:], list_of_list_2, sum_of_args)
    
#     if list_of_list_2 == []:
#         pass
#     elif type(list_of_list_2[0]) == list:
#         return sum(list_of_args, list_of_list_2[0], list_of_list_2[1:], sum_of_args)
#     else:
#         sum_of_args += list_of_list_2[0]
#         return sum(list_of_args, list_of_list_2[1:], [], sum_of_args)
    
#     if type(list_of_args[0]) == list or type(list_of_args[0]) == tuple:
#         print(f"list_of_args[0] = {list_of_args[0]}")
#         return sum(list_of_args[1:], list_of_args[0], [], sum_of_args)
#     else:
#         sum_of_args += list_of_args[0] 
#         return sum(list_of_args[1:], [], [], sum_of_args)

# # print(sum([[1, [2,3]], [4], 5]))

# print(sum([[[[1, [2, [3]]]], [4]], 5]))


"""--------------------------------------------"""


# exercise 8

# def prime_list(list_for_prime):
#     if list_for_prime == []:
#         return []
#     elif type(list_for_prime[0]) == list:
#         return prime_list(list_for_prime[0]) + prime_list(list_for_prime[1:])
#     else:
#         return [list_for_prime[0]] + prime_list(list_for_prime[1:])


# print(prime_list([1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]))






