respostas = [ # Cada lista dessa representa as perguntas sobre um dom, portanto elas terão 3 elementos
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

# Entrada dos elementos na matriz resposta:

numero = 0
# Inicialmente, devemos preencher o primeiro elemento de cada lista, e prosseguir para o segundo, e depois para o terceiro (Modelo do questionário)
for j in range(3):
    for i in range(19):
        if j == 0:
            x = i + 1
        if j == 1:
            x = 19 + i + 1
        if j == 2:
            x = 38 + i + 1
        print(f"Digite a resposta da pergunta {x}", end= ' ')
        numero = int(input())
        respostas[i].append(numero)
        numero = 0

# Agora que temos todas as respostas do teste inseridas, vamos fazer a soma de cada linha horizontal associada a um dom e salvar essas 
# somas na lista "resultados", essa lista terá 19 elementos, e cada elemento(que será uma soma) estará associado a um dom.
resultados = []

for i in range(19):
    y = 0
    for j in range(3):
        y += respostas[i][j]
    resultados.append(y)

nomes_dons = [
    "Administração", "Apostolado", "Artesanato", "Auxílio/serviço", "Conhecimento", "Contribuição", "Discernimento", "Encorajamento/Exortação", "Ensino", "Evangelismo",
    "Expressão artística/criativa", "Fé", "Hospitalidade", "Intercessão(oração)", "Liderança", "Misericórdia", "Pastoreiro", "Profecia", "Sabedoria"
]

# Agora, criando uma lista de pares (dom, resultado) para associar os nomes dos dons às suas pontuações
dons_com_pontuacoes = list(zip(nomes_dons, resultados))

# Ordenando a lista dos dons pelas pontuações em ordem decrescente
dons_ordenados = sorted(dons_com_pontuacoes, key=lambda x: x[1], reverse=True)

# Selecionando os três dons com as maiores pontuações
top_3_dons = dons_ordenados[:3]

print()
print('O resultado da coluna "total" dessa pessoa foi: ', resultados)
print()
print("E os seus 3 principais dons foram:")
for i in range(3):
    print(top_3_dons[i])