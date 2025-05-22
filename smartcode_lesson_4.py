# exercise slot

# def solver(slot1, slot2, duration):
#     for i in range(len(slot1)):
#         print(f"Slot1 = {slot1[i]}")
#         for j in range(len(slot2)):
#             if slot2[j][0] >= slot1[i][1]:
#                 continue
#             elif slot2[j][1] <= slot1[i][0]:
#                 continue
#             else:
#                 print(f"Slot2 = {slot2[j]} for Slot1 - {slot1[i]}")
#                 max_l_value = max(slot1[i][0], slot2[j][0])
#                 min_r_value = min(slot1[i][1], slot2[j][1])
#                 duration_for_check = min_r_value - max_l_value
#                 if duration_for_check >= duration:
#                     print(f"They can have their meeting in duration: {slot1[i]} for slot1: {slot2[j]} for slot2: ")


# slot1 = [[5, 17],[20, 31],[40, 45],[51, 63],[70, 80],[93, 97]]
# slot2 = [[1, 13],[14, 25],[27, 40],[50, 59],[61, 67],[71, 82],[85, 91],[97,100]]
# duration = 8
# solver(slot1, slot2, duration)




# exercise progress

# def find_long_progress(mylist, second_list):
#     if len(mylist) < 2:
#         return []
#     new_arr = [mylist[0]]
#     for index, number in enumerate(second_list):

#         if number > new_arr[-1]:
#             new_arr.append(number)
#             current_index = index

#     if len(new_arr) < 2:
#         return find_long_progress(mylist[1:], mylist[1:])
#     else:
#         return [new_arr] + find_long_progress(mylist, second_list[current_index + 1:])
    
    
# mylist = [4, 7, 3, 8, -1, 1, 2, 5 ,6, 0]
# second_list = mylist.copy()
# lists_of_progress = find_long_progress(mylist, second_list)

# for progress in lists_of_progress:
#     print(progress)

# max_len = lists_of_progress[0]

# for progress in lists_of_progress[1:]:
#     if len(progress) > len(max_len):
#         max_len = progress

# print(f"Progress which has max len is: {max_len}.")




# exercise surface

# def max_surface(x_y_list, dict_surface={}):
#     for index_current, x_y in enumerate(x_y_list):
#         for index_other, other_x_y in enumerate(x_y_list[index_current:]):
#             if x_y[0] == other_x_y[0]:
#                 continue
#             elif x_y[1] <= other_x_y[1]:
#                 surface = abs((other_x_y[0] - x_y[0]) * x_y[1])
#                 dict_surface[surface] = {index_current: (index_other + index_current)}
#             else:
#                 surface = abs((other_x_y[0] - x_y[0]) * other_x_y[1])
#                 dict_surface[surface] = {index_current: (index_other + index_current)}

#     return dict_surface



# x_y_list = [[0, 2],[2, 3],[4, 2],[5, 5],[8, 3],[9, 2],[10, 4]]
# dict_surfaces = max_surface(x_y_list)
# print(f"Surfaces (surface: indexes):\n{dict_surfaces}\n")
# maximum_surface = max(dict_surfaces)
# print(f"There is {len(dict_surfaces)} different surfaces and maximum one is {maximum_surface} with: {dict_surfaces[maximum_surface]} lines(indexes of lines):")