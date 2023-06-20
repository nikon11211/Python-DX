import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
pass_c = int(input('Сколько нужно создать паролей?'))
pas_len = int(input('Какая должна быть длина пароля?'))
dig_char = input('Пароль должен содержать цифры?')
alfa_upp_char = input('Пароль должен содержать прописные буквы?')
alfa_low_char = input('Пароль должен содержать строчные буквы?')
punc_char = input('Пароль должен содержать знаки пунктуации?')
non_sim_char = input('Исключить из пароля символы, которые легко перепутать?')
if dig_char.lower() == 'да':
    chars += digits
if alfa_upp_char.lower() == 'да':
    chars += uppercase_letters
if alfa_low_char.lower() == 'да':
    chars += lowercase_letters
if punc_char.lower() == 'да':
    chars += punctuation
if non_sim_char.lower() == 'да':
    for i in 'il1Lo0O':
        chars = chars.replace(i,'')
def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    print(password)
for _ in range(pass_c):
    generate_password(pas_len, chars)