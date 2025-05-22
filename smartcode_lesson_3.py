# exercise 149
# def first_ten_lines(filename):
#     try:
#         with open(filename, 'r') as f:
#             content = f.readlines()[:9]
#             return ''.join(content).strip()
#     except FileNotFoundError:
#         print("No such file")




# file_name = input("Enter the name of file: ")
# print(first_ten_lines(file_name))


"""--------------------------------------------"""


# exercise 150
# def last_ten_lines(filename):
#     try:
#         with open(filename, 'r') as f:
#             content = f.readlines()[-10:]
#             return ''.join(content).strip()

#     except FileNotFoundError:
#         print("There is no such file")

# file_name = input("Enter the name of file: ")
# print(last_ten_lines(file_name))


"""--------------------------------------------"""


# exercise 151
# import sys
# def read_files(filename):
#     try:
#         with open(filename, 'r') as f:
#             content = f.read()
#             return ''.join(content).strip()
#     except FileNotFoundError:
#         print(f"Sorry but there is no one file with name of {filename}")



# list_of_files = sys.argv[1:]
# for filename in list_of_files:
#     print(read_files(filename))


"""--------------------------------------------"""


# exercise 152
# def creating_file(src_file, dst_file):
#     try:
#         with open(src_file, 'r') as f:
#             content = f.readlines()
#             for index, i in enumerate(content):
#                 print(f"[{index}]: {i}")
        
#         with open(dst_file, 'w') as f:
#             for index, i in enumerate(content):
#                 f.write(f"[{index}]: {i}")

#     except FileNotFoundError:
#         print("There is no such file")



# src_file = input("Enter the file name where you want to take information from: ")
# dst_file = input("Enter the file name where you want to send information: ")
# creating_file(src_file, dst_file)


"""--------------------------------------------"""


# exercise 153

# def longest_word(filename):
#     try:
#         with open(filename, 'r') as f:
#             content = f.read().split()
#             dict_of_words = {i: len(i) for i in content}
#             max_length = max(dict_of_words.values())
#             list_of_longest_words = [word for word in dict_of_words.keys() if len(word) == max_length]
#             return f"There is {len(list_of_longest_words)} word which are longest in the file and they are: {': '.join(list_of_longest_words).strip()}"
        
#     except FileNotFoundError:
#         print("There is no such file")


# print(longest_word(input("Enter the file name: ")))


"""--------------------------------------------"""


# exercise 154

# def common_letters(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#             list_of_letter = [i.lower() for i in content if i.isalpha()]
#             dict_for_letters = {i: list_of_letter.count(i) for i in list_of_letter}
#             return f"Most common used letter is '{sorted(dict_for_letters, key=dict_for_letters.get)[-1]}' which used sharp {max(dict_for_letters.values())} times."
#     except FileNotFoundError:
#         print('There is no such file')

# print(common_letters(input("Enter the file name: ")))


"""--------------------------------------------"""


# exercise 155

# import string

# def common_word(filename):
#     try:
#         with open(filename, 'r') as f:
#             content = f.read().split()
#             list_of_words = [word.strip(string.punctuation).lower() for word in content]
#             dict_for_letters = {i: list_of_words.count(i) for i in list_of_words}
#             return f"Most common word is '{sorted(dict_for_letters, key=dict_for_letters.get)[-1]}' which is repeated sharp {max(dict_for_letters.values())} times"
#     except FileNotFoundError:
#         print("There is no such file")


# print(common_word(input("Enter the name of file ")))


"""--------------------------------------------"""


# exercise 156 
# # For being beautiful I don't print every time Total!!


# def sum(number=0):
#     number = input("Enter the number: ")
#     if number == '':
#         return 0
#     try:
#         number = float(number)
#         return number + sum(number)
#     except ValueError:
#         print("You have to write only numbers: ")
#         return sum()

# print(f"Total is: {sum()}")


"""--------------------------------------------"""


# exercise 158

# def removing_com(src_filename, dst_filename):
#     try: 
#         with open(src_filename, 'r') as file:
#             content = file.read().split('\n')
#             text_without_com = [line for line in content if '#' not in line]
        
#         with open(dst_filename, 'w') as file:
#             for line in text_without_com:
#                 file.write(line + '\n')
            
#     except FileNotFoundError:
#         print(F"Sorry but there is no such file: ")



# removing_com(input("Enter the source of info: "), input("Enter where it will be saved: "))


"""--------------------------------------------"""


# exercise 159

# import random
# def making_password(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read().split('\n')
#             password_words = random.sample(content, 2)
#             password = password_words[0].capitalize() + password_words[1].capitalize()
#             if len(password) >= 8:
#                 return password
#             else:
#                 return making_password(filename)
#     except FileNotFoundError:
#         print("Sorry no such file: ") 



# filename = input("Enter the file name: ")
# print(making_password(filename))


"""--------------------------------------------"""


# exercise 161

# def data_structure(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read().split('\n')
#             dict_of_chemical = {}
#             for line in content:
#                 list_of_line = line.split(',')
#                 dict_of_chemical[list_of_line[0]] = {list_of_line[1], list_of_line[2]}
#             return dict_of_chemical
#     except FileNotFoundError:
#         print("There is no such file: ")


# def choosing_element(dict_of_chemical):
#     element = input("Enter the info about element: ")
#     if element == '':
#         return 0
#     if element.isdecimal():
#         try:
#             print(f"{dict_of_chemical[element]} element has {element} protons: ")
#         except KeyError:
#             print(" No element found with that number of protons: ")
#         return choosing_element(dict_of_chemical)
#     else:
#         for proton, value in dict_of_chemical.items():
#             if element.capitalize() in value:
#                 print(f"{element} has {proton} protons: ")
#                 return choosing_element(dict_of_chemical)
#         print(" No element found with that symbol or name: ")
#         return choosing_element(dict_of_chemical)
            
        
# filename = input("Enter the name of file: ")
# dict_of_chemical = data_structure(filename)
# for key, value in dict_of_chemical.items():
#     print(f'{key} - {value}')
# choosing_element(dict_of_chemical)


"""--------------------------------------------"""


# exercise 162

# import string

# alphabet = string.ascii_lowercase

# def counting(filename, alphabet, dict_for_letter={}, sum_letter=0):
#     if alphabet == '':
#         return dict_for_letter
#     try:
#         with open(filename, 'r') as file:
#             content = file.readline().split(' ')
#             clear_words = []
#             for word in content:
#                 clear_words.append(word.strip(string.punctuation).lower())
#             for word in clear_words:
#                 sum_letter += word.count(alphabet[0])
#             dict_for_letter[alphabet[0]] = sum_letter
#             return counting(filename, alphabet[1:], dict_for_letter, 0)
#     except FileNotFoundError:
#         print("Sorry no such file or directory: ")

# filename = input("Enter file name: ")
# dict_ = counting(filename, alphabet)
# print(dict_)
# min_value = min(dict_.values())
# for key, value in dict_.items():
#     if value == min_value:
#         print(f"the letter {key} used in the smallest proportion of the words({value} times): ")


"""--------------------------------------------"""


# exercise 163

# import os

# boys_pop_name =[]
# girls_pop_name = []
# count = 0
# for i in sorted(os.listdir('BabyNames')):
#     with open(f'BabyNames/{i}', 'r') as file:
#         name = file.readline().split(' ')[0]
#         if 'Boys' in i:
#             if name in boys_pop_name:
#                 continue
#             else:
#                 boys_pop_name.append(name)
#         else:
#             if name in girls_pop_name:
#                 continue
#             else:
#                 girls_pop_name.append(name)


# print(f"Most common boys name from 1900 to 2012 are-{boys_pop_name}")
# print(f"Most common girls name from 1900 to 2012 are-{girls_pop_name}")


"""--------------------------------------------"""


# exercise 164


"""--------------------------------------------"""


# exercise 165

# import os

# def storing_in_dict(boy_dict, girl_dict, from_year, to_year):
#     for i in sorted(os.listdir("BabyNames")):
#         file_year = int(i.split('_')[0])
#         if file_year >= from_year and file_year <= to_year:
#             try:
#                 with open(f'BabyNames/{i}', 'r') as file:
#                     content = file.read().split('\n')
#                     for person in content:
#                         if person == '':
#                             continue
#                         name = person.split(' ')[0]
#                         count = int(person.split(' ')[1])
#                         if 'Boys' in i:
#                             if name in boy_dict:
#                                 boy_dict[name] += count
#                             else:
#                                 boy_dict[name] = count
#                         else:
#                             if name in girl_dict:
#                                 girl_dict[name] += count
#                             else:
#                                 girl_dict[name] = count
#             except FileNotFoundError:
#                 print('Sorry no such file or directory: ')
#         else:
#             continue
    
#     most_pop_boy_name = max(boy_dict, key=boy_dict.get)
#     most_pop_girl_name = max(girl_dict, key=girl_dict.get)
#     return (most_pop_boy_name, boy_dict[most_pop_boy_name]), (most_pop_girl_name, girl_dict[most_pop_girl_name])
    
    


# boy_dict = dict()
# girl_dict = dict()
# from_year = int(input("Enter the year(from): "))
# to_year = int(input("Enter the year(to): "))
# pop_boy, pop_girl = storing_in_dict(boy_dict, girl_dict, from_year, to_year)
# print(f"Most popular boy is {pop_boy}")
# print(f"Most popular girl is {pop_girl}")


"""--------------------------------------------"""



# exercise 166
# import os

# def unique_names(boy_sets, girl_sets):
#     for i in sorted(os.listdir("BabyNames")):
#         try: 
#             with open(f'BabyNames/{i}', 'r') as file:
#                 content = file.read().split('\n')
#                 for person in content:
#                     if person == '':
#                         continue
#                     name = person.split(' ')[0]
#                     if 'Boys' in i:
#                         boy_sets.add(name)
#                     else:
#                         girl_sets.add(name)
#         except FileNotFoundError:
#             print('There is no such file')
    
#     return f"\nUnique boys' name are:\n{boy_sets} \n\n\n\nUnique girls' name are:\n{girl_sets}"



# boy_names = set()
# girl_names = set()

# print(unique_names(boy_names, girl_names))


"""--------------------------------------------"""


# exercise 172

# vowels = 'aeiouy'
# word = 'tyheiauniaejnhiysjojjhaeuny'

# def info_sending(vowels, filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read().split(' ')
#             for word in content:
#                 print(checking(vowels, word))
#     except FileNotFoundError:
#         print("No such file: ")

    
# def checking(vowels, word, i=0, j=0):
#     if i != len(vowels) and j == len(word):
#         return f"{word} can not represent in order of vowels: "
#     elif i == len(vowels):
#         return f"{word} can represent in order of vowels: "

#     if vowels[i] == word[j]:
#         i += 1
#         j += 1
#         return checking(vowels, word, i, j)
#     else:
#         j += 1
#         return checking(vowels, word, i, j)
     


# filename = input("Enter the file name: ")
# info_sending(vowels, filename)




