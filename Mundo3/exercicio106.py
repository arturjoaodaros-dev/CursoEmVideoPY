print("\033[31m-=\033[m" * 30)
print(f"{'sistema de ajuda do ARTUR':^60}")
print("\033[31m-=\033[m" * 30)
while True:
    i = str(input("\033[36m>>>\033[m"))
    if i == "quit":
        print("\033[31mAté logo\033[m")
        break
    print("\033[31m-=\033[m" * 30)
    print(f"{f'Procurando por:{i}':^60}")
    print("\033[31m-=\033[m" * 30)
    print("\033[0;39;40m")
    print(help(i), "\033[m")
