#Exercise 1
# import random

# class Fight:
#     power_of_hit = 20
#     def __init__(self, name, health=100):
#         self.name = name
#         self.health = health

#     def attack(self, opponent):
#         opponent.health -= self.power_of_hit
#         print(f"{self.name} attacked {opponent.name}.{opponent.name} has {opponent.health} health left")
    

# player1 = Fight('Arsen')
# player2 = Fight('Paron Albert')
# players = [player1, player2]

# while True:
#     attacker = random.choice(players)
#     opponent = player1 if attacker == player2 else player2

#     attacker.attack(opponent)
#     if opponent.health <= 0:
#         print(f"Congratulation {attacker.name} is winner!!😎🔥")
#         break


#Exercise 2
# class Students:
#     def __init__(self, fn: str, group: str, grade: list):
#         self.fn = fn
#         self.group = group
#         self.grade = grade
    
#     def average(self):
#         average = sum(self.grade)/len(self.grade)
#         return average



# student1 = Students('Arsen Ishkhanian', 'TT221', [90, 85, 87, 88, 86])
# student2 = Students('Hayk Khachatryan', 'TT220', [69, 78, 81, 94, 90])
# student3 = Students('Davit Khachatryan', 'TT221', [82, 40, 89, 61])
# student4 = Students('Misha Sahakyan', 'EE211', [57, 74, 81, 56])
# students = [student1, student2, student3, student4]
# average_list = {student: student.average() for student in students}
# sorted_list = dict(sorted(average_list.items(), key=lambda pair: pair[1], reverse=True))
# for key, value in sorted_list.items():
#     print(f"{key.fn} - {key.group} - {value}")



# Exercise 3
# Already done at the lesson



# Exercise 4
# class Parent:
#     def __init__(self, name:str, age:int, children:list):
#         self.name = name
#         self.age = age
#         self.children = children
    
#     def about(self):
#         print(f"My name is {self.name}.Im {self.age} years old and have {len(self.children)} children.")

#     def calm_children(self):
#         for child in self.children:
#             if not child.calmness:
#                 child.calmness = True
#                 print(f'I make calm {child.name}.')
#             else:
#                 print(f"{child.name} is calm.")

#     def feed_children(self):
#         for child in self.children:
#             if child.hunger:
#                 child.hunger = False
#                 print(f"I feed {child.name}.")
#             else:
#                 print(f"{child.name} is full")


# class Children:
#     def __init__(self, name:str, age:int, calmness=False, hunger=True):
#         self.name = name
#         self.age = age
#         self.calmness = calmness
#         self.hunger = hunger

#     def make_hungry(self):
#         self.hunger = True
    
#     def make_upset(self):
#         self.calmness = False

#     def about_hunger(self):
#         if self.hunger:
#             print(f"I'm are very hungry!!!")
#         else:
#             print(f"I'm are not hungry yet!!")
    
#     def about_calmness(self):
#         if self.calmness:
#             print(f"I'm are very quiet!!!")
#         else:
#             print(f"I'm are very upset!!")


# children1 = Children('Armen', 14)
# children2 = Children('Arsen', 20)
# children3 = Children('Salvik', 25)
# parent1 = Parent('Samvel', 48, [children1, children2, children3])
# children4 = Children('Hayk', 21)
# children5 = Children('Melkon', 23)
# parent2 = Parent('Telman', 45, [children4, children5])
# children6 = Children('Sara', 18)
# children7 = Children('Hrach', 24)
# parent3 = Parent('Artur', 55, [children6, children7])
# parent1.about()
# print(children1.calmness)
# parent1.calm_children()
# print(children1.calmness)
# children1.make_upset()
# parent1.calm_children()
# parent2.about()
# parent2.feed_children()
# parent3.about()
# parent3.feed_children()
# print(children6.hunger)



# Exercise 5
# class Potatoes:
#     def __init__(self, id:int, growth_stage:int):
#         self.id = id
#         self.growth_stage = growth_stage
    
#     def grow(self):
#         if self.growth_stage < 4:
#             self.growth_stage += 1

#     def info(self):
#         print(f"Potatoe[{self.id}] is at the {self.growth_stage}th stage!")


# class Bed:
#     def __init__(self, potatoes:list):
#         self.potatoes = potatoes
    
#     def grow_all(self):
#         for potatoe in self.potatoes:
#             potatoe.grow()
#         print("All potatoes had growth by 1 stage.")
        
#     def bed_info(self):
#         about_bed = {potatoe.id: potatoe.growth_stage for potatoe in self.potatoes}
#         for id, stage in about_bed.items():
#             print(f"Potatoe[{id}] is at the {stage}th stage.")


# class Gardener:
#     def __init__(self, name:str, bed, harvested_potatoes={}):
#         self.name = name
#         self.bed = bed
#         self.harvested_potatoes = harvested_potatoes
    
#     def take_care_of_potatoes(self):
#         for potatoe in self.bed.potatoes:
#             potatoe.grow()
#         print(f"All potatoes had growth by 1 stage(by {self.name})")

#     def harvest(self):
#         for potatoe in self.bed.potatoes:
#             if potatoe.growth_stage == 4:
#                 self.harvested_potatoes[potatoe.id] = potatoe.growth_stage
            
#     def info_harvested_potatoes(self):
#         for id, value in self.harvested_potatoes.items():
#             print(f"Potatoe[{id}] has been harvested")

        
# potatoe1 = Potatoes(0, 0)
# potatoe2 = Potatoes(1, 2)
# potatoe3 = Potatoes(2, 3)
# list_of_potatoes = [potatoe1, potatoe2, potatoe3]
# bed = Bed(list_of_potatoes)
# bed.bed_info()
# bed.grow_all()
# bed.bed_info()
# bed.grow_all()
# bed.bed_info()
# gardener = Gardener('Argisht', bed)
# gardener.harvest()
# gardener.info_harvested_potatoes()
# gardener.take_care_of_potatoes()
# potatoe1.info()
# potatoe1.grow()
# bed.bed_info()


# Exercise 6
# class Element:
#     def __init__(self, value:str, dict_table:dict):
#         self.value = value
#         self.dict_table = dict_table

    
#     def __add__(self, other):
#         combo = self.value + other.value
#         reverse_combo = other.value + self.value
#         if combo in self.dict_table.keys():
#             return f"Two classes were added and the result is {Result(self.dict_table[combo])}."
#         elif reverse_combo in self.dict_table.keys():
#             return f"Two classes were added and the result is {Result(self.dict_table[reverse_combo])}."
#         else:
#             return f"There is no such combination with {self.value} and {other.value}."
    
# class Result:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"{self.name}"


# dict_combo = {
#     'WaterAir': 'Storm',
#     'WaterFire': 'Steam',
#     'WaterEarth': 'Mud',
#     'AirFire': 'Lightning',
#     'AirEarth': 'Dust',
#     'FireEarth': 'Lava'
# }

# water = Element('Water', dict_combo)
# air = Element('Air', dict_combo)
# fire = Element('Fire', dict_combo)
# earth = Element('Earth', dict_combo)
# result = water + fire
# print(result)


# Exercise 7
# import random
# class Person:
#     def __init__(self, name:str, house, satiety=50):
#         self.name = name
#         self.house = house
#         self.satiety = satiety
    
#     def roll(self):
#         dice = random.randint(1, 6)
#         if self.satiety < 20 and self.house.food >= 10:
#             self.eat()
#         elif self.house.food < 10 and self.house.money >= 10:
#             self.shopping()
#         elif self.house.money < 50:
#             self.work()
#         elif dice == 1:
#             self.work()
#         elif dice == 2:
#             self.eat()
#         else:
#             self.play()
        
#         if self.satiety <= 0:
#             print(f"{self.name} died.")
#             return

#     def info(self):
#         print(f"\t{self.name} with {self.satiety} satiety", end= ' ')

#     def eat(self):
#         self.satiety += 20
#         self.house.food -= 10
#         print(f"is eating.")
    
#     def work(self):
#         self.satiety -= 10
#         self.house.money += 20
#         print(f"is working.")

#     def play(self):
#         self.satiety -= 5
#         print(f"is playing PS4.")
    
#     def shopping(self):
#         self.house.food += 20
#         self.house.money -= 10
#         print(f"is going to shopping.")

# class House:
#     def __init__(self, food:int, money:int):
#         self.food = food
#         self.money = money

#     def info(self):
#         print(f"\tThere are {self.money} money$ and {self.food} food at home.\n")

# house = House(50, 0)
# person1 = Person('Arsen', house)
# person2 = Person('Karen', house)

# for day in range(50):
#     print(f"It is day number {day + 1}!!")
#     person1.info()
#     person1.roll()
#     person2.info()
#     person2.roll()
#     print("House(after day):")
#     house.info()