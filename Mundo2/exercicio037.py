num = int(input("digite um numero inteiro: "))
print("Escolha uma base:")
print("1 - binário")
print("2 - octal")
print("3 - hexadecimal")
chs = int(input(">"))
if chs == 1:
    print(bin(num))
elif chs == 2:
    print(oct(num))
elif num == 3:
    print(hex(num))
else:
    print("opção inválida")
