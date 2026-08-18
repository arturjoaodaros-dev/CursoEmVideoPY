# Extraido de Aula007.py - desafio011
import time

alt = float(input("qual a altura da parede em metros:"))
lar = float(input("qual a largura da parede em metros:"))
ar = alt * lar
print(
    f"sua parede tem {ar} de area e vai precisar de {ar / 2} litros para pinta-la inteira!"
)
time.sleep(1)
