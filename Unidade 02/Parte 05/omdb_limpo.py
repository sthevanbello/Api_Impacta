import requests
import math 
from pprint import pprint

'''
A primeira coisa a fazer é ir ao site http://www.omdbapi.com/
e clicar no link API key.

Cadastre-se, abra o e-mail e valide sua chave. Depois, você
poderá acessar o OMDb.
'''

'coloque aqui a sua chave de acesso à api'
api_key = '6868b7ff'

'''
Antes de fazer qualquer função, vamos experimentar
consultar o OMDb pelo navegador.

Digite, por exemplo, a seguinte URL no Firefox:
    http://www.omdbapi.com/?s=star%20wars&apikey=6868b7ff

Observe que vemos uma lista de 10 filmes, mas há mais resultados.

Para ver a página 2, acesse
    http://www.omdbapi.com/?s=star%20wars&page=2&apikey=6868b7ff
'''


'''
Observe que nas URLs acima, estamos passando parâmetros.
Na URL http://www.omdbapi.com/?s=star%20wars&page=2&apikey=6868b7ff
definimos 3 parâmetros:
 * s=star wars
 * page=2
 * apikey={SUA-CHAVE-VEM-AQUI}
'''

'''
QUESTÃO 1
Olhando para os resultados da consulta
http://www.omdbapi.com/?s=star%20wars&apikey={SUA-CHAVE-VEM-AQUI},
quantos itens foram encontrados para o termo "star wars"?


Resposta: 737

QUESTÃO 2
Consultando a documentação em www.omdbapi.com, você
pode aprender a filtrar os resultados da sua busca,
ficando apenas com filmes, eliminando jogos e séries.

Como fazer isso? https://www.omdbapi.com/?s=star%20wars&type=movie&apikey=6868b7ff
type=movie

Se você fizer essa consulta, quantos filmes
existem para a busca star wars? 

Resposta: 537

QUESTÃO 3:
E se ao invés de filmes você quiser só jogos,
quantos existem?

Resposta: 110

'''




'''
Vou te deixar dois exemplos de como acessar a URL. Nesse exemplo,
eu estou retornando o dicionário inteiro.
'''

def busca_por_id(film_id):
    url = f"http://www.omdbapi.com/?apikey={api_key}&i={film_id}"
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    return dicionario_do_pedido

def busca_por_texto(texto_buscar):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={texto_buscar}"
    pedido = requests.get(url) #conectar na URL
    dicionario_do_pedido = pedido.json() #transformo a string que eu recebi num dicionário de python
    return dicionario_do_pedido

def busca_por_tipo(nome, tipo_buscar):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={nome}&type={tipo_buscar}"
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    return dicionario_do_pedido

def __busca(nome='', tipo='', id='', page=''):
    if(id != ''):
        url = f"http://www.omdbapi.com/?apikey={api_key}&i={id}"
    else:
        url = f"http://www.omdbapi.com/?apikey={api_key}&s={nome}&type={tipo}&page={page}"
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    return dicionario_do_pedido

'''
Experimente! chame d1=busca_por_texto('star wars') e examine o
dicionário d1 retornado.
'''

'''
Agora, faça uma função busca_qtd_total que retorna quantos
itens (pode ser filme, jogo, série ou o que for) batem com
uma determinada busca.
'''
def busca_qtd_total(texto_buscar):
    # filmes = busca_por_texto(texto_buscar)
    filmes = __busca(nome = texto_buscar)
    return filmes['totalResults']

# def busca_qtd_total(texto_buscar):
#     url = f"http://www.omdbapi.com/?apikey={api_key}&s={texto_buscar}"
#     pedido = requests.get(url) #conectar na URL
#     filmes = pedido.json()
#     return filmes['totalResults']

'''
Faça uma função busca_qtd_filmes que retorna quantos
filmes batem com uma determinada busca.
'''
def busca_qtd_filmes(nome):
    # filmes = busca_por_tipo(nome, 'movie')
    filmes = __busca(nome = nome, tipo = 'movie')
    return filmes['totalResults']

# def busca_qtd_filmes(texto_buscar):
#     url = f"http://www.omdbapi.com/?apikey={api_key}&s={texto_buscar}&type=movie"
#     pedido = requests.get(url) #conectar na URL
#     filmes = pedido.json()
#     return filmes['totalResults']


'''
Faça uma função busca_qtd_jogos que retorna quantos
jogos batem com uma determinada busca.
'''
def busca_qtd_jogos(nome):
    # item = busca_por_tipo(nome, 'game')
    item = __busca(nome = nome, tipo = 'game')
    return item['totalResults']

'''
Agora, vamos aprender a ver os detalhes de um filme.

Por exemplo, na lista de filmes podemos ver que o filme
star wars original (de 1977) tem id 'tt0076759'

Acessando a URL
http://www.omdbapi.com/?i=tt0076759&apikey={SUA-CHAVE-VEM-AQUI}
podemos ver mais detalhes.

Observe que agora não temos mais o parâmetro 's=star%20wars'
mas sim i=tt0076759. Mudou o nome da "variável", não só
o valor.
'''

'''
Faça uma função nome_do_filme_por_id que recebe a id de
um filme e retorna o seu nome.
'''
def nome_do_filme_por_id(id_filme):
    item = __busca(id=id_filme)
    if (item['Response'] == 'False'):
        raise "Id not found"
    return item['Title']

'''
Faça uma função ano_do_filme_por_id que recebe a id de
um filme e retorna o seu ano de lançamento.
'''
def ano_do_filme_por_id(id_filme):
    item = __busca(id=id_filme)
    if (item['Response'] == 'False'):
        raise "Id not found"
    return item['Year']

'''
Peguemos vários dados de um filme de uma vez.

A ideia é receber uma id e retornar 
um dicionário com diversos dados do filme.

O dicionário deve ter as seguintes chaves:
 * ano
 * nome
 * diretor
 * genero

E os dados devem ser preenchidos baseado nos dados do site.
'''
def dicionario_do_filme_por_id(id_filme):
    dic = {}
    item = __busca(id = id_filme)
    dic = {
        'ano': item['Year'],
        'nome': item['Title'],
        'diretor': item['Director'],
        'genero': item['Genre'] 
        }
    return dic

'''
Voltando para a busca...

Faça uma função busca_filmes que, dada uma busca, retorna
os dez primeiros items (filmes, series, jogos ou o que for)
que batem com a busca.

A sua resposta deve ser uma lista, cada filme representado por 
um dicionário. cada dicionario deve conter os campos
'nome' (valor Title da resposta) e 'ano' (valor Year da resposta).
'''
# def busca_filmes(texto_buscar):
#     lista = []
#     filmes = __busca(nome=texto_buscar)
#     for pos in range(0,10):
#         lista.append({
#             'Name': filmes['Search'][pos]['Title'],
#             'Year': filmes['Search'][pos]['Year']
#             }
#         )
#     return lista

def busca_filmes(texto_buscar):
    lista = []
    filmes = __busca(nome=texto_buscar)
    for pos in range(0,10):
        dic = {}
        dic['Name'] = filmes['Search'][pos]['Title']
        dic['Year'] = filmes['Search'][pos]['Year']
        lista.append(dic)
    return lista
'''
Faça uma função busca_filmes_grande que, dada uma busca, retorna
os VINTE primeiros filmes que batem com a busca.
'''
def busca_filmes_grande(texto_buscar):
    lista = list()
    for page in range(1,3):
        filmes = __busca(nome=texto_buscar, page=page)
        for pos in range(0,10):
            lista.append({
                'Name': filmes['Search'][pos]['Title'],
                'Year': filmes['Search'][pos]['Year']
                }
            )
    return lista

def busca_qtd_personalizada(texto_buscar, quantidade):
    lista = list()
    dic = dict()
    pages = 1
    if quantidade > 10:
        pages = math.ceil(quantidade / 10)
    for page in range(1,pages+1):
        filmes = __busca(nome=texto_buscar, page=page)
        for pos in range(0,10):
            if(len(lista) >= quantidade ):
                break
            lista.append({
                'Name': filmes['Search'][pos]['Title'],
                'Year': filmes['Search'][pos]['Year']
                }
            )
    return lista

# print(busca_filmes('star wars'))
# print(busca_qtd_personalizada('star wars', 15))
# print(dicionario_do_filme_por_id('tt3778644'))