def teste_site(url):
    import urllib.request
    try:
        page = urllib.request.urlopen(url)
    except:
        print(f"\033[0;31mA url {url} não está acessível no momento.\033[m")
    else:
        print(f"\033[0;32mA ulr {url} foi acessada com sucesso. \033[m")


teste_site("http://pudim.com.br/")
