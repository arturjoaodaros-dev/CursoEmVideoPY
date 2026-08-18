frase = "o artur é legal ele é legal"
print(frase[9:21:2])
print(frase[:5])  # print (frase[0:5])
print(frase[15:])
print(frase[9::2])
print(frase.count("e", 0, 13))
print(frase.find("art"))
frase = frase.replace("legal", "thiago")
print(frase)
frase = frase.upper()
print(frase)
frase = frase.split()
print(frase)
print("""1.732.542 visualizações  31 de jul. de 2017  Curso de Python 3 - Mundo 1: Fundamentos
Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().
Gostou da aula? Então torne-se um Gafanhoto APOIADOR do CursoemVídeo acessando o site cursoemvideo.com/apoie
Aula do Curso de Python criado pelo professor Gustavo Guanabara para o portal CursoemVideo.com.
Curso em Vídeo
Seja um apoiador: http://cursoemvideo.com/apoie
Site: http://www.cursoemvideo.com
YouTube:    / cursoemvideo  
Facebook:   / cursosemvideo  
Twitter:   / cursosemvideo  
Google+: http://plus.google.com/11266655883741...
Patrocínio
HOSTNET: http://www.hostnet.com.br
GAFANHOTOS: http://apoie.me/cursoemvideo""")
print(len(frase))
