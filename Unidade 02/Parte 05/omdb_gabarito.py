import requests 
from pprint import pprint

'''
A primeira coisa a fazer é ir ao site http://www.omdbapi.com/
e clicar no link API key.

Cadastre-se, abra o e-mail e valide sua chave. Depois, você
poderá acessar o OMDb.
'''

'coloque aqui a sua chave de acesso à api'
api_key = 'e51a115c'

'''
Antes de fazer qualquer função, vamos experimentar
consultar o OMDb pelo navegador.

Digite, por exemplo, a seguinte URL no Firefox:
    http://www.omdbapi.com/?s=star%20wars&apikey={SUA-CHAVE-VEM-AQUI}

Observe que vemos uma lista de 10 filmes, mas há mais resultados.

Para ver a página 2, acesse
    http://www.omdbapi.com/?s=star%20wars&page=2&apikey={SUA-CHAVE-VEM-AQUI}
'''


'''
Observe que nas URLs acima, estamos passando parâmetros.
Na URL http://www.omdbapi.com/?s=star%20wars&page=2&apikey={SUA-CHAVE-VEM-AQUI}
definimos 3 parâmetros:
 * s=star wars
 * page=2
 * apikey={SUA-CHAVE-VEM-AQUI}
'''

'''
QUESTÃO 1
Olhando para os resultados da consulta
http://www.omdbapi.com/?s=star%20wars&apikey={SUA-CHAVE-VEM-AQUI},
quantos filmes foram encontrados para o termo "star wars"?

Resposta:

QUESTÃO 2
Consultando a documentação em www.omdbapi.com, você
pode aprender a filtrar os resultados da sua busca,
ficando apenas com filmes, eliminando jogos e séries.

Como fazer isso?

Se você fizer essa consulta, quantos filmes
existem para a busca star wars?

Resposta:

QUESTÃO 3:
E se ao invés de filmes você quiser só jogos,
quantos existem?

Resposta:

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
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={texto_buscar}"
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    return int(dicionario_do_pedido['totalResults'])

'''
Faça uma função busca_qtd_filmes que retorna quantos
filmes batem com uma determinada busca.
'''
def busca_qtd_filmes(texto_buscar):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={texto_buscar}&type=movie"
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    return int(dicionario_do_pedido['totalResults'])

'''
Faça uma função busca_qtd_jogos que retorna quantos
jogos batem com uma determinada busca.
'''
def busca_qtd_jogos(texto_buscar):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={texto_buscar}&type=game"
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    return int(dicionario_do_pedido['totalResults'])

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
    filme = busca_por_id(id_filme)
    return filme['Title']

'''
Faça uma função ano_do_filme_por_id que recebe a id de
um filme e retorna o seu ano de lançamento.
'''
def ano_do_filme_por_id(id_filme):
    filme = busca_por_id(id_filme)
    return filme['Year']

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
    dic_filme = {}
    dic_filme_ingles = busca_por_id(id_filme)
    dic_filme['ano'] = dic_filme_ingles['Year']
    dic_filme['nome'] = dic_filme_ingles['Title']
    dic_filme['genero'] = dic_filme_ingles['Genre']
    dic_filme['diretor'] = dic_filme_ingles['Director']
    return dic_filme

'''
Voltando para a busca...

Faça uma função busca_filmes que, dada uma busca, retorna
os dez primeiros items (filmes, series, jogos ou o que for)
que batem com a busca.

A sua resposta deve ser uma lista, cada filme representado por 
um dicionário. cada dicionario deve conter os campos
'nome' (valor Title da resposta) e 'ano' (valor Year da resposta).
'''
def busca_filmes(texto_buscar,pagina=1):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={texto_buscar}&page={pagina}"
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    resposta = []
    for filme in dicionario_do_pedido['Search']:
        dic = {}
        dic['nome'] = filme['Title']
        dic['ano']  = filme['Year']
        resposta.append(dic)
    return resposta

'''
Faça uma função busca_filmes_grande que, dada uma busca, retorna
os VINTE primeiros filmes que batem com a busca.
'''
def busca_filmes_grande(texto_buscar):
    pagina1 = busca_filmes(texto_buscar,1)
    pagina2 = busca_filmes(texto_buscar,2)

    return pagina1+pagina2




import unittest

porbaixo = 0.5
porcima = 2
class TestStringMethods(unittest.TestCase):
    
    def test_000_qdt_total(self):
        self.assertTrue(439 * porbaixo < int(busca_qtd_total('star wars')) < 439 * porcima)
        self.assertTrue(283 * porbaixo < int(busca_qtd_total('star trek')) < 283 * porcima)

    def test_001_qdt_filmes(self):
        self.assertTrue(305 * porbaixo < int(busca_qtd_filmes('star wars')) < 305 * porcima)
        self.assertTrue(186 * porbaixo < int(busca_qtd_filmes('star trek')) < 186 * porcima)
        self.assertTrue(111 * porbaixo < int(busca_qtd_filmes('menace')) < porcima * 111)
        self.assertTrue(964 * porbaixo < int(busca_qtd_filmes('future')) < 964 * porcima)

    def test_002_qdt_jogos(self):
        self.assertTrue(96 * porbaixo < int(busca_qtd_jogos('star wars')) < porcima * 96)
        self.assertTrue(55 * porbaixo < int(busca_qtd_jogos('star trek')) < porcima * 55)
        self.assertTrue( 8 * porbaixo < int(busca_qtd_jogos('menace')) < porcima *  8)
        self.assertTrue(34 * porbaixo < int(busca_qtd_jogos('future')) < porcima * 34)

    def test_003_nome_do_filme_por_id(self):
        self.assertEqual(nome_do_filme_por_id('tt0796366'), 'Star Trek')
        self.assertEqual(nome_do_filme_por_id('tt0861739'), 'Tropa de Elite')

    def test_004_ano_do_filme_por_id(self):
        self.assertEqual(ano_do_filme_por_id('tt0076759'), '1977')
        self.assertEqual(ano_do_filme_por_id('tt1211837'), '2016')

    def test_005_dicionario_filme_por_id(self):
        d1 = dicionario_do_filme_por_id('tt0076759')
        self.assertTrue(type(d1) is dict)
        self.assertEqual(d1['ano'], '1977')
        self.assertEqual(d1['diretor'], 'George Lucas')
        self.assertTrue('Action' in d1['genero'])
        d2 = dicionario_do_filme_por_id('tt1211837')
        self.assertTrue(type(d2) is dict)
        self.assertEqual(d2['ano'], '2016')
        self.assertEqual(d2['nome'], 'Doctor Strange')
        self.assertTrue('Fantasy' in d2['genero'])
    
    def test_006_busca(self):
        resposta = busca_filmes('star wars')
        self.assertEqual(len(resposta),10)
        achei = False
        for filme in resposta:
            try:
                if int(filme['ano']) == 1977:
                    achei = True
            except:
                pass
            if 'ano' not in filme:
                self.fail('Ano não encontrado')
            if 'nome' not in filme:
                self.fail('Nome não encontrado')
        if not achei:
            self.fail('Filme "A New Hope" não encontrado')
    
    def test_007_busca_grande(self):
        resposta = busca_filmes_grande('star wars')
        self.assertEqual(len(resposta), 20)
        achei = False
        for filme in resposta:
            try:
                if int(filme['ano']) == 1977:
                    achei = True
            except:
                pass
            if 'ano' not in filme:
                self.fail('Ano não encontrado.')
            if 'nome' not in filme:
                self.fail('Nome não encontrado.')
        if not achei:
            self.fail('Filme "A New Hope" não encontrado.')
    

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)



#runTests()