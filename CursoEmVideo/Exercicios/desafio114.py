from urllib import error
from urllib import request

try:
    site = request.urlopen('http://www.pudim.com.br')
except error.URLError:
    print('O site pudim está fora do ar')
else:
    print('Consegui entrar no site pudim.')
