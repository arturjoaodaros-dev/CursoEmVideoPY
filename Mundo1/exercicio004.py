def main():
    txt = input("digite algo:")
    bol = txt.lower() == "true" or txt.lower() == "false"
    string = txt.isalpha()

    if string is True and bol is True:
        print("É o booleano True ou False")
        print("é um numero?", txt.isnumeric())
        print("é um texto?", txt.isalpha())
        print("é um numero flutuante?", txt.replace(".", "", 1).isnumeric())
        print("é um booleano?", bol)
        print("possui espaços?", txt.isspace())
        print("está em maiúsculo?", txt.isupper())
        print("está em minúsculo?", txt.islower())
        print("está capitalizada?", txt.istitle())
        print("é alfanumérico?", txt.isalnum())
        print("é decimal?", txt.isdecimal())
        print("é um identificador?", txt.isidentifier())
        print("é um dígito?", txt.isdigit())
        print("é um ASCII?", txt.isascii())
    else:
        print("seu tipo é", type(txt))
        print("é um numero?", txt.isnumeric())
        print("é um texto?", txt.isalpha())
        print("é um numero flutuante?", txt.replace(".", "", 1).isnumeric())
        print("é um booleano?", bol)
        print("possui espaços?", txt.isspace())
        print("está em maiúsculo?", txt.isupper())
        print("está em minúsculo?", txt.islower())
        print("está capitalizada?", txt.istitle())
        print("é alfanumérico?", txt.isalnum())
        print("é decimal?", txt.isdecimal())
        print("é um identificador?", txt.isidentifier())
        print("é um dígito?", txt.isdigit())
        print("é um ASCII?", txt.isascii())

    n = input("vamos dnv?:")
    if n.lower() in {"sim", "s", "yes", "y"}:
        main()
    else:
        print("ok, tchau")


main()
