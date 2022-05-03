import requests

url_base = "http://127.0.0.1:5000/corredores"

def pedido_request(tipo=''):
    tipo_pedido = f'/{tipo}' if tipo != '' else ''
    url = f"{url_base}{tipo_pedido}"
    pedido = requests.get(url)
    return pedido


def todos_os_corredores():
    return pedido_request().json()

def adiciona_corredor(nome_novo, tempo_novo, id_novo):
    corredor = {
        'nome': nome_novo, 
        'tempo': tempo_novo, 
        'id': id_novo
        }
    requests.post(url_base, json=corredor)
    return True

def mais_lento():
    pedido = pedido_request('maior_tempo')
    if pedido.status_code == 200:
        corredor = pedido.json()
        return corredor['nome']
    elif pedido.status_code == 500:
        return f"Erro na busca por corredores - Erro {pedido.status_code}"

def apaga_mais_lento():
    url = f"{url_base}/maior_tempo"
    corredor = requests.delete(url)
    if corredor.status_code == 200:
        return "Corredor mais lento foi deletado"
    return f"Não foi possível apagar o corredor - Erro {corredor.status_code}"

def busca_por_id(id):
    pedido = pedido_request(id)
    if pedido.status_code != 200 :
        return f"{id} - {pedido.status_code} - {pedido.reason}"
    corredor = pedido.json()
    tupla_corredor = (corredor['corredor']['nome'], corredor['corredor']['tempo'])
    return tupla_corredor

# método idempotente
# Só apaga uma vez
def apaga_por_id(id):
    url = f"{url_base}/{id}"
    corredor = requests.delete(url)
    if corredor.status_code == 200:
        return "Corredor foi deletado"
    return f"Não foi possível apagar o corredor - Erro {corredor.status_code} - {corredor.reason}"

def atualiza_corredor(id, tempo):
    tempo_novo = {"tempo": tempo} 
    url = f"{url_base}/{id}"
    pedido = requests.put(url, json = tempo_novo)
    if pedido.status_code == 400:
        return f"{pedido.reason} - {tempo} é maior do que o record atual - {pedido.status_code}"
    if pedido.status_code == 404:
        return f"Corredor não encontrado com esse id: {id}"
