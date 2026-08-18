# nessa aula a gnt aprendeu a criar pacotes, se quiser ver eles
# 1.vai em Mundo3/Utilidades
# 2.veja as funções que cada um dos modulos tem
# 3. se quiser testar, pode usar import Utilidades
# 4.OU import Utilidades.Moeda/Dados exemplo:
import CursoEmVideo.Mundo3.Utilidades.Dados
from CursoEmVideo.Mundo3.Utilidades import Moeda

print(Moeda.moeda(9))
print(CursoEmVideo.Mundo3.Utilidades.Dados.sumarize(9.9))
