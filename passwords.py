import string
import ast
from secrets import choice
from unidecode import unidecode

class Password:
    f = open('slowa.txt', encoding='utf-8')
    data = f.readlines()
    dict = ast.literal_eval(data[0])

    def __init__(self, lenght: int, specials: int):
        self.lenght = lenght
        self.specials = specials
        self.text = self.generate_password(lenght, specials)

    def __repr__(self):
        return str(self.text)

    def has_digit(self, string):
        return any(char.isdigit() for char in string)

    def has_upper(self, string):
        return any(char.isupper() for char in string)

    def generate_password(self, lenght, specials):
        word = choice(self.dict)
        characters_list = string.digits + string.punctuation
        characters = ''.join(choice(characters_list) for i in range(specials))
        password = word+characters

        if self.has_digit(password) == False:
            s_pos = choice(range(len(password)))
            password = password[:s_pos] + \
                str(choice(string.digits)) + password[s_pos:]
        while len(password) != lenght:
            if len(password) < lenght:
                word = choice(self.dict)
                password = word + choice(string.punctuation) + password
            else:
                dif = len(password)-lenght
                password = password[dif:]
        if self.has_upper(password) == False:
            try:
                s_pos = choice(range(len(password)))
                password = password.replace(
                    password[s_pos], password[s_pos].upper())
            except:
                pass
        password = unidecode(password)
        return password


passwords = [Password(20, 3) for i in range(11)]
for p in passwords:
    print(p)

