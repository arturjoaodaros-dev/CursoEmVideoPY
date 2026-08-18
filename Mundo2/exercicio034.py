s = float(input("\033[1;32;40mqual o seu salário: \033[m"))
if s >= 1250:
    print(f"seu salario com aumento é {s * 1.10}")
else:
    print(f"seu salario com aumento é {s * 1.15}")
