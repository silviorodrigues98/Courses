""" CRIAR UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS NO CAMPEONADO
 BRASILEIRO DE FUTEBOL. APONTAR OS 5 PRIMEIROS COLOCADOS;
  OS ÚLTIMOS 4 COLOCADOS;
  LISTA COM OS TIMES EM ORDEM ALFABÉTICA;
  EM QUE POSIÇÃO ESTA A CHAPECOECE. """


times_brasileirao = ("PALMEIRAS", "SÃO PAULO", "FLAMENGO", "CHAPECOENSE", "SANTOS", "INTERNACIONAL", "BOTA FOGO",
                     "GRÊMIO", "CRUZEIRO", "ATLÉTICO-MG", "ATLÉTICO-GO", "CORINTHIANS", "FLUMINENSE", "AMÉRICA-MG",
                     "CALDENSE", "VULCÃO", "ATLÉTICO-GO", "GOIÁS")

primeiros_5 = times_brasileirao[0:5]
ultimos_4 = times_brasileirao[-4:]
alfabetica = sorted(times_brasileirao)
posicao = times_brasileirao.index('CHAPECOENSE') + 1

print(f"""Os cinco primeiros colocados foram:
{primeiros_5}
Já os últimos 4 foram: 
{ultimos_4}
A lista em ordem alfabética fica dessa forma:
{alfabetica}
O time do CHAPECOENSE se encontra na {posicao}ª posição. """)
