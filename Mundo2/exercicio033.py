c = int(input("quntos numeros voce vai colocar na lista? "))
nums = []
for i in range(c):
    v = int(input("digite um numero: "))
    nums.append(v)
print(max(nums))
