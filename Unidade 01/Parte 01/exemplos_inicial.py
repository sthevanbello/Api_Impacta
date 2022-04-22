dic = {
    "alimentos": {
        "pizzas":
        ["margueritta", "mussarella", "frango com catupiry", "portuguesa"],
        "bolos": ("floresta negra", "red velvet", "de laranja", "dá vó"),
        "calorias": {
            "leite": 129,
            "fatia pizza": 320,
            "agua": 0,
            "maça": 95
        }
    },
    "linguagens": [
        {
            "nome": "javascript",
            "criacao": 1996,
            "paradigma": ["eventos", "funcional"]
        },
        {
            "nome": "python",
            "criacao": 1991,
            "paradigma": ["orientada a objetos", "estruturada"]
        },
        {
            "nome": "haskell",
            "criacao": 1990,
            # "criacao": 1999,
            "paradigma": ["funcional"]
        }
    ]
}

# Só se aprende fazendo. PAUSE O VIDEO E TENTE RESPONDER!
# Se possível, FAÇA JUNTO NO SEU COMPUTADOR

# 1. quantas chaves tem o dicionario dic?
# print("r1", len(dic))

# # 2. dic['linguagens'] é uma tupla, um dicionário ou uma lista?
# print("r2", type(dic['linguagens']))

# # 3. Como eu faço para mostrar todos os bolos?
# # (escreva o código!)

# # 4. Qual o tipo da lista de todos os bolos?
# print("r4", type(dic['alimentos']['bolos']))

# 5. O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("r5", dic["linguagens"]["javascript"]["criacao"])
# print("r5 corrigido", dic["linguagens"][0]["criacao"])

# 6 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("r6", dic["linguagens"][2] == "haskell")
# print("r6", dic["linguagens"][2]["nome"] == "haskell")

# # 7 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("r7", dic["alimentos"]["pizzas"][2] == "mussarella")
# print("r7", dic["alimentos"]["pizzas"][2] == "frango com catupiry")

# # 8 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("r8", 1996 in dic['linguagens'][0])
# print("r8", 1996 in dic['linguagens'][0].values())

# # 9 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("r9", "criacao" in dic['linguagens'][0])

# # 9 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("ex9b", "pudim" in dic["sobremesas"]["doces"])
# print("ex9b", "pudim" in dic["alimentos"]["bolos"][1])
# print("ex9b", "leite" in dic["alimentos"]["calorias"])

# 10 Escreva uma função "mais velha" que
# recebe um dicionário como dic e
# retorna (isso é diferente de imprimir!) a linguagem de programação mais velha da nossa lista

# 11 Escreva uma função que retorna uma lista (sem repetições) de paradigmas de linguagens de programação


def mais_velha(dic):
    # ling_velha = {"criacao": 2022}
    ling_velha = dic["linguagens"][0]
    for linguagem in dic["linguagens"]:
        if linguagem["criacao"] < ling_velha["criacao"]:
            ling_velha = linguagem
    return ling_velha


print(mais_velha(dic))


def paradigmas(dic):
    set_paradigmas = set()
    list_paradigmas = []

    for linguagem in dic["linguagens"]:
        for paradigma in linguagem["paradigma"]:
            set_paradigmas.add(paradigma)

    list_paradigmas = list(set_paradigmas)
    return list_paradigmas


# print(paradigmas(dic))
print(paradigmas(dic))