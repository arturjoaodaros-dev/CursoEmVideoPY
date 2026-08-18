import requests as rq

try:
    rq.request("GET", "https://pudim.com.br")
    print("pudim está acessivel")
except:
    print("pudim n está acessivel")
