# import random
# class House:
#     def __init__(self, money, food, cat_food, dust):
#         self.money = money
#         self.food = food
#         self.cat_food = cat_food
#         self.dust = dust


# class Husband(House):
#     def __init__(self, house: House, name, satiety, mood):
#         super().__init__(house.money, house.food, house.cat_food, house.dust)
#         self.name = name
#         self.satiety = satiety
#         self.mood = mood
#         self.house = house
    
#     def decide_what_to_do(self):
#         if self.satiety <= 15 and self.house.food:
#             self.eat()
#         elif self.mood <= 20:
#             self.play()
#         elif self.house.money <= 250:
#             self.work()
#         else:
#             random.choice([self.eat, self.play, self.work])()

#     def eat(self):
#         can_eat = min(self.house.food, 30)
#         self.satiety += can_eat
#         self.house.food -= can_eat
#         print(f"Husband: ate {can_eat} point food(🍛), and has {self.satiety} satiety, {self.mood} mood.")

#     def play(self):
#         self.satiety -= 10
#         self.mood += 20
#         print(f"Husband: played PS4(🎮), and has {self.satiety} satiety, {self.mood} mood.")


#     def work(self):
#         self.satiety -= 10
#         self.house.money += 150
#         print(f"Husband: worked(🧑🏻‍💻), and has {self.satiety} satiety, {self.mood} mood.")

# class Wife(House):
#     def __init__(self,house: House, name, satiety, mood):
#         super().__init__(house.money, house.food, house.cat_food, house.dust)
#         self.name = name
#         self.satiety = satiety
#         self.mood = mood
#         self.house = house
    
#     def decide_what_to_do(self):
#         if self.satiety <= 15 and self.house.food:
#             self.eat()
#         elif self.mood <= 50 and self.house.money >= 350:
#             self.buy_coat()
#         elif self.house.food < 60 and self.house.money > 2:
#             self.shopping()
#         else:
#             if self.house.money >= 350:
#                 random.choice([self.eat, self.buy_coat, self.shopping, self.clean_the_house])()
#             else:
#                 random.choice([self.eat, self.shopping, self.clean_the_house])()

#     def eat(self):
#         can_eat = min(self.house.food, 30)
#         self.satiety += can_eat
#         self.house.food -= can_eat
#         print(f"Wife: ate {can_eat} point food(🍛), and has {self.satiety} satiety, {self.mood} mood.")

#     def shopping(self):
#         money = min(self.house.money, 100)
#         if money == 100:
#             food_amount = 70
#             cat_food = 30
#         else:
#             food_amount = 2 * (money // 3)
#             cat_food = money - food_amount
#         self.satiety -= 10
#         self.house.money -= (food_amount + cat_food)
#         self.house.food += food_amount
#         self.house.cat_food += cat_food
#         print(f"Wife: went to shopping(🛍️) and bought {food_amount} point food, {cat_food} point cat food, and has {self.satiety} satiety, {self.mood} mood.")
            

#     def buy_coat(self):
#         self.satiety -= 10
#         self.mood += 60
#         self.house.money -= 350
#         print(f"Wife: bought the coat(🧥), and has {self.satiety} satiety, {self.mood} mood.")

#     def clean_the_house(self):
#         self.satiety -= 10
#         can_clean = min(self.house.dust, 100)
#         self.house.dust -= can_clean
#         print(f"Wife: cleaned the house(🧹), and has {self.satiety} satiety, {self.mood} mood.")

# class Cat(House):
#     def __init__(self, house, name, satiety=30):
#         super().__init__(house.money, house.food, house.cat_food, house.dust)
#         self.name = name
#         self.satiety = satiety
#         self.house = house
    
#     def decide_what_to_do(self):
#         if self.satiety <= 15 and self.house.cat_food:
#             self.eat()
#         elif self.house.dust < 80:
#             self.tear_wallpaper()
#         else:
#             random.choice([self.tear_wallpaper, self.sleep])()

#     def eat(self):
#         can_eat = min(self.house.cat_food, 10)
#         self.satiety += 2 * can_eat
#         self.house.cat_food -= can_eat
#         print(f"Cat: ate {can_eat} point food(🌮), and has {self.satiety} satiety.")

#     def sleep(self):
#         self.satiety -= 10
#         print(f"Cat: slept(💤), and has {self.satiety} satiety.")

#     def tear_wallpaper(self):
#         self.satiety -= 10
#         self.house.dust += 20
#         print(f"Cat: teared wallpapers(😼), and has {self.satiety} satiety.")


# house = House(100, 50, 30, 0)
# husband = Husband(house, 'Arsen', 30, 100)
# wife = Wife(house, 'Maretik', 30, 100)
# cat = Cat(house, 'Jecki', 30)
# one_of_family_alive = True
# husband_alive = True
# wife_alive = True
# cat_alive = True

# for i in range(120):
#     if one_of_family_alive:
#         house.dust += 20
#         print(f"\nDay {i + 1} - House: {house.money} money - {house.food} food - {house.cat_food} cat food - {house.dust} dust:\n")
#         if husband_alive:
#             if husband.satiety < 0 or husband.mood < 10:
#                 print(f"The husband(🧔🏻‍♂️) died on the {i}th day!!☠️🪦\n")
#                 husband_alive = False
#         if wife_alive:
#             if wife.satiety < 0 or wife.mood < 10:
#                 print(f"The wife(👱🏼‍♀️) died on the {i}th day!!☠️🪦\n")
#                 wife_alive = False
#         if cat_alive:
#             if cat.satiety < 0:
#                 print(f"The cat(🐈‍⬛) died on the {i}th day!!☠️🪦\n")
#                 cat_alive = False
                
#         if house.dust > 90:
#             husband.mood -= 10
#             wife.mood -= 10

#         if husband_alive:
#             husband.decide_what_to_do()
#         if wife_alive:
#             wife.decide_what_to_do()
#         if cat_alive:
#             cat.decide_what_to_do()
        
        
#         if husband_alive == False and wife_alive == False and cat_alive == False:
#             print(f"The family died on the {i}th day!!☠️🪦")
#             one_of_family_alive = False
#     else:

#         break



    

