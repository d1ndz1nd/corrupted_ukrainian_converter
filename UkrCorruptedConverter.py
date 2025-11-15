user_text = input("Введіть ваш пошкоджений український текст: ")
user_text_lower = user_text.lower()
user_text_tuple = tuple(user_text_lower)
converted_text_list = []
ukr_symbols = {
    'q':'й',
    'w':'ц',
    'e':'у',
    'r':'к',
    't':'е',
    'y':'н',
    'u':'г',
    'i':'ш',
    'o':'щ',
    'p':'з',
    '[':'х',
    ']':'ї',
    'a':'ф',
    's':'і',
    'd':'в',
    'f':'а',
    'g':'п',
    'h':'р',
    'j':'о',
    'k':'л',
    'l':'д',
    ';':'ж',
    "'":"є",
    'z':'я',
    'x':'ч',
    'c':'с',
    'v':'м',
    'b':'и',
    'n':'т',
    'm':'ь',
    ',':'б',
    '.':'ю',
    '/':'.',
    ' ':' ',
    }
for i in user_text_tuple:
    if i in ukr_symbols:
        converted_text_list.append(ukr_symbols[i])
    else:
        converted_text_list.append(i)
converted_text = "".join(converted_text_list)
print(f"Ваш виправлений текст: {converted_text}")
