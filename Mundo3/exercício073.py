br = (
    "vasco",
    "corinthians",
    "palmeiras",
    "internacional",
    "grêmio",
    "flamengo",
    "são paulo",
    "atlético mineiro",
    "atlético paranaense",
    "cuiaba",
    "chapecoense",
)
print(br[0:5])  # pega 5 posições começando do 0
count = -1
while count != -6:
    print(br[count], end=" ")
    count -= 1
print("\n")
print(sorted(br, reverse=True))
print(f"a chapecoense está na {br.index('chapecoense') + 1}° posição na tabela")
