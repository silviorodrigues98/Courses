import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("O site pudim não está acessível no momento")
else:
    print("Acessei o site Pudim com sucesso.")
    print(site.read())
