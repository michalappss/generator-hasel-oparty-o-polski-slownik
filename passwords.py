import string
from secrets import choice
from unidecode import unidecode
import pickle

class Password:
    with open('slowa.pkl', 'rb') as f:
        dict = pickle.load(f)
    
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
        if self.has_digit(password) == False:
            s_pos = choice(range(len(password)))
            password = password.replace(password[s_pos], str(choice(string.digits)))
        password = unidecode(password)
        return password


lista_hasel = [Password(9, 3) for i in range(30)]
for p in lista_hasel:
    print(p)