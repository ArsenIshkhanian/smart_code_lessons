# Exercise 1
# def ask(func):
#     def wrap():
#         input("How it's going? ")
#         print("It's not good to me:")
#         func()
#     return wrap
# @ask
# def test():
#     print("Do something: ")
# test()



# Exercise 2
# import time
# def check(func):
#     def wrap():
#         time.sleep(4)
#         func()
#     return wrap
# @check
# def do_som():
#     print("It was slept several seconds...")
# do_som()



# Exercise 3
# Done at the lesson



# Exercise 4
# def counter(func):
#     def wrapper():
#         wrapper.count += 1
#         print(f"Call numser is {wrapper.count}")
#         func()
#     wrapper.count = 0
#     return wrapper

# @counter
# def something():
#     print('I did something')
# something()
# something()



# Exercise 5
# class ContextManager:
#     def __init__(self, file_name:str, mode:str):
#         self.file_name = file_name
#         self.mode = mode
#         self._file = None
    
#     def get_file(self):
#         return self._file

#     def set_file(self, new_obj):
#         try:
#             self._file = new_obj
#         except Exception:
#             return False
#         return True
#     def __enter__(self):
#         try:
#             self._file = open(self.file_name, self.mode)
#         except FileNotFoundError:
#             self._file = open(self.file_name, 'w')
#         return self._file
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         try:
#             if self._file:
#                 self._file.close()
#         except Exception:
#             pass
#         if exc_type in (FileNotFoundError, IOError, OSError):
#             return True
#         return False
# with ContextManager('Admins.txt', 'r') as file:
#     print(file.read())
    


# Exercise 6 
# import math
# class MyMath:
#     def __init__(self, radius: float = 1.0, side: float = 1.0):
#         self.radius = radius
#         self.side = side

#     @property
#     def side(self):
#         return self.__side
    
    # @side.setter
    # def side(self, value: float):
    #     if value <= 0:
    #         raise ValueError("Side must be positive: ")
    #     self.__side = value

#     @property
#     def radius(self):
#         return self.__radius
    
#     @radius.setter
#     def radius(self, value: float):
#         if value <= 0:
#             raise ValueError("Radius must be positive: ")
#         self.__radius = value
        
#     def circle_length(self):
#         return 2 * math.pi * self.__radius
    
#     def circle_area(self):
#         return math.pi * (self.__radius ** 2)
    
#     def cube_volume(self):
#         return self.__side ** 3
    
#     def sphere_surface_area(self):
#         return 4 * math.pi * self.__radius


# res_1 = MyMath(radius=5)
# print(res_1.circle_length())
# res_2 = MyMath(side=4)
# print(res_2.cube_volume())
# print(res_1.radius)
# print(res_2.side)


# Exercise 7
# class Date:
#     def __init__(self, day, month, year):
#         self.__day = day
#         self.__month = month
#         self.__year = year

#     @classmethod
#     def from_string(cls, date):
#         """Date must be dd-mm-yyyy"""
#         date_info = date.split('-')
#         day, month, year = int(date_info[0]), int(date_info[1]), int(date_info[2])
#         if 1 <= day <= 31 and 1 <= month <= 12:
#             return cls(day, month, year)
#         else:
#             raise ValueError("You entered wrong date! ")
    
#     def __str__(self):
#         return f"{self.__day:02d}-{self.__month:02d}-{self.__year}"
        

    
# first_d = Date.from_string('11-05-2024')
# print(first_d)


# Exercise 8
# user_permissions = ['admin']
# def check_permission(permission):
#     def decorator(main_f):
#         def wrapper():
#             if permission in user_permissions:
#                 main_f()
#             else:
#                 raise PermissionError("You dont have permission for that action! ")
#         return wrapper
#     return decorator

# @check_permission('admin')
# def delete_acc():
#     print("Deleting account...")

# @check_permission('user_1')
# def adding_comment():
#     print("Adding comment...")

# adding_comment()



# Exercise 9
# routes = {}
 
# def callback(path):
#     def decorator(main_f):
#         routes[path] = main_f
#         return main_f
#     return decorator


# @callback('//')
# def call_():
#     print("Something which is till the call: ")
#     return 'OK'



# class App:
#     def get(self, path:str):
#         return routes.get(path, None)


# app = App()
# route = app.get('//')

# if route:
#     answer = route()
#     print(f"Answer: {answer}")
#     pass
# else:
#     print("No such path! ")



# Exercise 10
# def singleton(cls):
#     used_inst = {}
#     def wrapper(*args, **kwargs):
#         if cls not in used_inst:
#             used_inst[cls] = cls(*args, **kwargs)
#         return used_inst[cls]
#     return wrapper

# @singleton
# class Exapmle:
#     pass


# my_obj = Exapmle()
# my_obj_2 = Exapmle()
# my_obj_3 = Exapmle()
# print(my_obj_2 is my_obj_3)

