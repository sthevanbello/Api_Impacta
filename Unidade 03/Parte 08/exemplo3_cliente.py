import requests

nome = input("Digite o nome: ")
sexo = input("Digite o sexo: ")
cabelo = input("Digite a cor do cabelo: ")

dados = {"nome": nome, "sexo": sexo, "cabelo": cabelo}

url = "http://localhost:5002"

def pessoa_ok(dic):
    return type(dic) == dict \
        and len(dic) == 3 \
        and "nome" in dic \
        and "sexo" in dic \
        and "cabelo" in dic \
        and type(dic["nome"]) == str \
        and dic["sexo"] in ["M", "F"] \
        and type(dic["cabelo"]) == str


def verifica_status(request):
    if request.status_code != 200:
        print(f"[{request.status_code}] {request.text}")
    else:
        print(request.text)

def insere_pessoa(dados):
    url_post = f"{url}/pessoa"
    if pessoa_ok(dados):
        pedido = requests.post(url_post, json = dados)
        verifica_status(pedido)

def atualiza_pessoa_id(id, dados):
    if pessoa_ok(dados):
        url_put = f"{url}/pessoa/{id}"
        pedido = requests.put(url_put, json = dados)
        verifica_status(pedido)
    else:
        return f"The data: {dados} are not compatible. Verify the data"

def mostra_pessoa_id(id):
    url_get = f"{url}/pessoa/{id}"
    pedido = requests.get(url_get)
    verifica_status(pedido)

def apaga_pessoa_id(id):
    url_delete = f"{url}/pessoa/{id}"
    pedido = requests.delete(url_delete)
    verifica_status(pedido)

def mostra_todos():
    url_todos = f"{url}/pessoas"
    pedido = requests.get(url_todos)
    verifica_status(pedido)