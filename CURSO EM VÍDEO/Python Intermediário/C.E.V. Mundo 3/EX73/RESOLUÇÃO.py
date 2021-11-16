times = ("PALMEIRAS", "SÃO PAULO", "FLAMENGO", "CHAPECOENSE", "SANTOS", "INTERNACIONAL", "BOTA FOGO",
         "GRÊMIO", "CRUZEIRO", "ATLÉTICO-MG", "ATLÉTICO-GO", "CORINTHIANS", "FLUMINENSE", "AMÉRICA-MG",
         "CALDENSE", "VULCÃO", "ATLÉTICO-GO", "GOIÁS")
print("-="*15)
print(f"Lista de timas :{times}")
print("=-"*15)
"""for t in times:
    print(t)"""
print(f"Os cinco primeiros são: {times[:5]}")
print("-="*15)
print(f"Os quatro últimos são: {times[-4:]}")
print("-="*15)
print(f"Times em ordem alfabética : {sorted(times)}")
print("-="*15)
print(f"O Chapecoense está na {times.index('CHAPECOENSE')+1}ª posição.")
print("-="*15)
