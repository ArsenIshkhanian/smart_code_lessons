# import math
# class CoronaVirus:
#     def __init__(self, temperature):
#         self.temperature = temperature
    
#     def check(self):
#         if math.ceil(self.temperature * math.pi) <= 128 and math.ceil(self.temperature * math.pi) >= 120:
#             return f"You have corona virus with {math.ceil(self.temperature * math.pi)} C."
#         else:
#             return "Everything okay with you: "
    

# temperature = eval(input("Please enter you body temperature: "))
# Arsen = CoronaVirus(temperature).check()
# print(Arsen)
# print(math.ceil(math.pi * 38.1))



# import math
# class MathLetters:
#     def __init__(self, name: str, info: dict):
#         self.name = name
#         self.inf0 = info

#     def check(self):
#         sum = 0
#         for i in self.name:
#             sum += info[i.lower()]
#         if math.sqrt(sum) < 5:
#             return f"{sum}, Yes"
#         else:
#             return f"{sum}, No"    
# info = {
#     'a': 1,
#     'j': 1,
#     's': 1,
#     'b': 2,
#     'k': 2,
#     't': 2,
#     'c': 3,
#     'l': 3,
#     'u': 3,
#     'd': 4,
#     'm': 4,
#     'v': 4,
#     'e': 5,
#     'n': 5,
#     'w': 5,
#     'f': 6,
#     'o': 6,
#     'x': 6,
#     'g': 7,
#     'p': 7,
#     'y': 7,
#     'h': 8,
#     'q': 8,
#     'z': 8,
#     'i': 9,
#     'r': 9,
# }
# student1 = MathLetters('Jon', info)
# print(student1.check())



# import random
# class Fight:
#     def __init__(self, magic1: str, magic2:str, magic3:str ,voldemort_list:list):
#         self.magic1 = magic1
#         self.magic2 = magic2
#         self.magic3 = magic3
#         self.voldemort_list = voldemort_list
#     def result(self):
#         magic_words = [self.magic1.lower(), self.magic2.lower(), self.magic3.lower()]
#         sum = 0
#         for word in range(len(magic_words)):
#             if magic_words[word] == self.voldemort_list[word]:
#                 sum += 1
#         if sum < 2:
#             print(F"Harry potter: \n\t {magic_words} \nVoldemort: \n\t{self.voldemort_list}")
#             return f"You unfortunately lose the fight with {sum}:{3-sum} Score!"
#         else:
#             print(F"Harry potter: \n\t {magic_words} \nVoldemort: \n\t{self.voldemort_list}")
#             return f"You Won with {sum}:{3-sum} Score!"



# words = ['Avada Kedavra', 'Crucio', 'Imperio']
# voldemort_list = []
# for i in range(3):
#     voldemort_list.append(random.choice(words).lower())
# HarryPoter = Fight(input('Enter the first magic word (Avada Kedavra/Crucio/Imperio): '), input('Enter the second magic word (Avada Kedavra/Crucio/Imperio): '), input('Enter and third magic word (Avada Kedavra/Crucio/Imperio): '), voldemort_list)
# print(HarryPoter.result())