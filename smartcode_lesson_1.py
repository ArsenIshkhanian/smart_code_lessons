# Exercise 175
# number = int(input("Enter positive decimal number: "))
# if number < 0:
#     raise ImportError("You have to write positive number: ")

# def converter(decimal, binary):
#     integer_part = decimal // 2
#     remainder_part = decimal % 2
#     if integer_part == 0:
#         binary += '1'
#         binary = binary[::-1]
#         return binary
#     else:
#         binary += str(remainder_part)
#         return converter(integer_part, binary)
        
# binary = ''
# print(converter(number, binary))
"""------------------------------------------------------------"""
# Exercise 176
# nato = {
#     'A': 'Alpha',
#     'B': 'Bravo',
#     'C': 'Charlie',
#     'D': 'Delta',
#     'E': 'Echo',
#     'F': 'Foxtrot',
#     'G': 'Golf',
#     'H': 'Hotel',
#     'I': 'India',
#     'J': 'Juliett',
#     'K': 'Kilo',
#     'L': 'Lima',
#     'M': 'Mike',
#     'N': 'November',
#     'O': 'Oscar',
#     'P': 'Papa',
#     'Q': 'Quebec',
#     'R': 'Romeo',
#     'S': 'Sierra',
#     'T': 'Tango',
#     'U': 'Uniform',
#     'V': 'Victor',
#     'W': 'Whiskey',
#     'X': 'X-ray',
#     'Y': 'Yankee',
#     'Z': 'Zulu'
# }

# def spelling(nato, word):
#     if word == '':
#         return ''
#     else:
#         letter = word[0]
#         return nato[letter.upper()] + ' ' + spelling(nato, word[1:])

# word = input("Enter the word for spellig: ")
# print(spelling(nato, word))
"""------------------------------------------------------------"""
# Exercise 181
# coins = [1, 5, 10, 25]
# amount_coins = float(input("Enter the amount of coins: ")) #68
# count_coins = int(input("Enter how many coins you have: ")) #7
# def solver(coins, amount_coins, count_coins, count):
#     print(f"\ncoins = {coins}",
#           f"\namount = {amount_coins}",
#           f"\ncount = {count}")
    
#     if count == count_coins:
#         return True
#     elif coins == []:
#         return False
#     else:
#         reminder = amount_coins % coins[-1]
#         count += amount_coins // coins[-1]
#         print(f"Reminder != 0")
#         return solver(coins[:-1], reminder, count_coins, count)
#     # elif reminder == 0:
#     #     count += amount_coins / coins[-1]
#     #     print(f"Reminder == 0")
#     #     return solver(coins[:-1], reminder, count_coins, count)
# 
# 
# count = 0
# if amount_coins / max(coins) > count_coins:
#     print(f"False")
# else:
#     print(solver(coins, amount_coins, count_coins, count))
"""------------------------------------------------------------"""
#Exercise 182
# def finder(word, symbol, each_symbol=''):
#     if word == '':
#         return ''
#     each_symbol += word[0]
#     if each_symbol.title() in symbol:
#         print(f"{each_symbol.title()} in symbol")
#         return each_symbol.title() + finder(word[1:], symbol)
#     else:
#         print(f"{each_symbol.title()} not in symbol")
#         return finder(word[1:], symbol, each_symbol)



# element_symbols = [
#     "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
#     "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
#     "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
#     "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
#     "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
#     "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
#     "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
#     "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
#     "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
#     "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
#     "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
#     "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
# ]
# word = input("Input the word: ")
# each_symbol = ''
# print(f"{word.title} can be spelled as {finder(word, element_symbols, each_symbol)}")