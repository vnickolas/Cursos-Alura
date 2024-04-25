import matplotlib.pyplot as plt

estudantes = [ "João", "Maria", "José"]
notas = [8.5, 9, 6.5]

plt.bar(x = estudantes, height= notas)

temp_celsius = [0, 25, 37, 78, 100]
temp_fahrenheit = list(map(lambda x: (x * 9/5) + 32, temp_celsius)) #o lambda é a função em uma linha, o map itera cada item da lista e o list transforma o mapa no ojbeto de lista
temp_fahrenheit

Aquecimento
1.

# Lista gerada
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

# Lendo o tamanho, maior e menor número e soma, respectivamente, utilizando as built-in functions
tam = len(lista)
maior = max(lista)
menor = min(lista)
soma = sum(lista)

# Exibindo o texto
print(f"A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores  presentes nela é igual a {soma}.")
COPIAR CÓDIGO
2.

# Requisitando o número
num = int(input("Digite um número inteiro de 1 a 10:"))

# Gerando a função tabuada()
def tabuada(numero: int):
  print(f'Tabuada do {numero}:')
  for i in range(11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')

# lendo a tabuada do número escolhido
tabuada(num)
COPIAR CÓDIGO
3.

# Lista gerada
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

# declarando a lista de multiplos de 3 
mult_3 = []
# função para gerar uma lista dos múltiplos de 3 a partir de uma lista
def multiplo_3(lista: list) -> list:
  for i in range(len(lista)):
    # condição para um número ser múltiplo de 3
    if lista[i] % 3 == 0:
      mult_3.append(lista[i])
  return mult_3

# retornando a lista gerada para a variável mult_3
mult_3 = multiplo_3(lista)
mult_3
COPIAR CÓDIGO
4.

# Lista dos números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função lambda que eleva um número ao quadrado
quadrado = lambda x: x ** 2

# Utilizando a função map() para aplicar a função lambda em cada número da lista
resultado = list(map(quadrado, numeros))
resultado 
COPIAR CÓDIGO
Aplicando a projetos
5.

# declarando a lista de notas
notas = []
# laço for para pedir as 5 notas e armazená-las na lista notas
for i in range(1,6):
  nota = float(input(f"Digite a {i}ª nota: "))
  notas.append(nota)

# Função para remover a maior e menor nota e retornar a média das notas restantes
def media(lista):
  lista.remove(max(lista))
  lista.remove(min(lista))
  return sum(lista) / len(lista)

# Chamando a função e imprimindo a nota da(o) skatista
media = media(notas)
print(f"Nota da manobra: {round(media, 1)}") 
COPIAR CÓDIGO
6.

# declarando a lista de notas
notas = []
# laço for para pedir as 4 notas e armazená-las na lista notas
for i in range(1,5):
  nota = float(input(f"Digite a {i}ª nota: "))
  notas.append(nota)

def cadastro(lista):
  maior = max(lista)
  menor = min(lista)
  media = sum(lista) / len(lista)
  if media >= 6:
    situacao = "Aprovado(a)"
  else:
    situacao = "Reprovado(a)"
  
  return (media, maior, menor, situacao)

media, maior, menor, situacao = cadastro(notas)

print(f"O(a) estudante obteve uma media de {media}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {situacao}")
COPIAR CÓDIGO
7.

# Nomes dos estudantes
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

# Função lambda que recebe duas listas e itera em cada uma concatenando seu nome e sobrenome
# na forma desejada
nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)

# Leitura do objeto mapa(iterável)
for n in nome_completo:
  print(f'Nome completo: {n}')
COPIAR CÓDIGO
8.

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

def calcula_pontos(gols_marcados, gols_sofridos):
  pontos = 0
  for i in range(len(gols_marcados)):
    if gols_marcados[i] > gols_sofridos[i]:
      pontos += 3
    elif gols_marcados[i] == gols_sofridos[i]:
      pontos += 1
  aprov = 100 * pontos / (len(gols_marcados) * 3)
  return (pontos, aprov)

pontos, aprov = calcula_pontos(gols_marcados, gols_sofridos)
print(f"A pontuação do time foi de {pontos} e seu aproveitamento foi de {round(aprov)}%")
COPIAR CÓDIGO
9.

dias = int(input("Quantas diárias? "))
cidade = input("Qual a cidade? [Salvador, Fortaleza, Natal ou Aracaju]: ")
distancias = [850, 800, 300, 550]
passeio = [200, 400, 250, 300]
km_l = 14
gasolina = 5

def gasto_hotel(dias):
    return 150 * dias

def gasto_gasolina(cidade):
    if cidade == "Salvador":
        return (2 * distancias[0] * gasolina) / km_l 
    elif cidade == "Fortaleza":
        return (2 * distancias[1] * gasolina) / km_l 
    elif cidade == "Natal":
        return (2 * distancias[2] * gasolina) / km_l 
    elif cidade == "Aracaju":
        return (2 * distancias[3] * gasolina) / km_l 

def gasto_passeio(cidade, dias):
    if cidade=="Salvador":
        return passeio[0] * dias
    elif cidade=="Fortaleza":
        return passeio[1] * dias
    elif cidade=="Natal":
        return passeio[2] * dias 
    elif cidade=="Aracaju":
        return passeio[3] * dias 

gastos = gasto_hotel(dias) + gasto_gasolina(cidade) + gasto_passeio(cidade, dias)
print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {round(gastos, 2)} reais")
COPIAR CÓDIGO
10.

# Requisitando uma frase e separando-a pelos espaços. Usando replace para trocar
# pontuações por espaço.
frase = input("Digite uma frase: ")
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split()

# Filtrando a frase no formato de lista, passando para a lista tamanho
# apenas as palavras com 5 ou mais caracteres e imprimindo-a na tela
tamanho = list(filter(lambda x: len(x) >= 5, frase))
print(tamanho)

*****************************************LISTAS DE LISTAS*****************************************

notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

nomes = []
notas_juntas = []
for i in range(len(notas_turma)):
  if i % 4 == 0:
    nomes.append(notas_turma[i])
  else:
    notas_juntas.append(notas_turma[i])
nomes
['João', 'Maria', 'José', 'Cláudia', 'Ana']

notas_juntas
[8.0, 9.0, 10.0, 9.0, 7.0, 6.0, 3.4, 7.0, 7.0, 5.5, 6.6, 8.0, 6.0, 10.0, 9.5]

notas = []
for i in range(0, len(notas_juntas), 3):
  notas.append([notas_juntas[i], notas_juntas[i+1], notas_juntas[i+2]])
notas
[[8.0, 9.0, 10.0],
 [9.0, 7.0, 6.0],
 [3.4, 7.0, 7.0],
 [5.5, 6.6, 8.0],
 [6.0, 10.0, 9.5]]

notas[0][-1]
10.0


*****************************************TUPLAS*****************************************

estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]
estudantes
['João', 'Maria', 'José', 'Cláudia', 'Ana']


from random import randint

def gera_codigo():
  return str(randint(0,999))

codigo_estudantes = []

for i in range(len(estudantes)):
  codigo_estudantes.append((estudantes[i], estudantes[i][0] + gera_codigo()))
codigo_estudantes
[('João', 'J189'),
 ('Maria', 'M624'),
 ('José', 'J797'),
 ('Cláudia', 'C73'),
 ('Ana', 'A75')]



*****************************************LISTA COMPRENHESION*****************************************


notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

def media(lista: list=[0]) -> float:
  ''' Função para calcular a média de notas passadas por uma lista

  lista: list, default [0]
    Lista com as notas para calcular a média
  return = calculo: float 
    Média calculada
  '''
  
  calculo = sum(lista) / len(lista)

  return calculo

medias = [round(media(nota), 1) for nota in notas]
medias
[9.0, 7.3, 5.8, 6.7, 8.5]

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

# Gerando a lista de nomes (extraindo da tupla)
nomes = [nome[0] for nome in nomes]
nomes
['João', 'Maria', 'José', 'Cláudia', 'Ana']


estudantes = list(zip(nomes, medias))
estudantes
[('João', 9.0), ('Maria', 7.3), ('José', 5.8), ('Cláudia', 6.7), ('Ana', 8.5)]

# Gerando a lista de pessoas candidatas a bolsa
canditados  = [estudante[0] for estudante in estudantes if estudante[1] >= 8]
canditados
['João', 'Ana']

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

situacao = ["Aprovado" if media >= 6 else "Reprovado" for media in medias]
['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']

lista_completa = [nomes, notas, medias, situacao]
lista_completa
[[('João', 'J720'),
  ('Maria', 'M205'),
  ('José', 'J371'),
  ('Cláudia', 'C546'),
  ('Ana', 'A347')],
 [[8.0, 9.0, 10.0],
  [9.0, 7.0, 6.0],
  [3.4, 7.0, 7.0],
  [5.5, 6.6, 8.0],
  [6.0, 10.0, 9.5]],
 [9.0, 7.3, 5.8, 6.7, 8.5],
 ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

Situação 11:
Agora, a nossa demanda consiste em gerar um dicionário a partir da lista de listas que criamos na Situação 10 para passar para a pessoa responsável por construir as tabelas para a análise dos dados.

As chaves do nosso dicionário serão as colunas identificando o tipo de dado
Os valores serão as listas com os dados correspondentes àquela chave.
Vamos resolver esse desafio?

Para facilitar o nosso entendimento do processo vamos trabalhar com uma turma fictícia de 5 estudantes.

Dica: Utilize o formato

lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

# Colunas com os tipos dos dados (exceto nome)
coluna = ["Notas", "Média Final", "Situação"]
cadastro = {coluna[i]: lista_completa[i] for i in range(len(coluna))}
cadastro
{'Notas': [('João', 'J720'),
  ('Maria', 'M205'),
  ('José', 'J371'),
  ('Cláudia', 'C546'),
  ('Ana', 'A347')],
 'Média Final': [[8.0, 9.0, 10.0],
  [9.0, 7.0, 6.0],
  [3.4, 7.0, 7.0],
  [5.5, 6.6, 8.0],
  [6.0, 10.0, 9.5]],
 'Situação': [9.0, 7.3, 5.8, 6.7, 8.5]}

cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))] # o ["Estudante"] é eu criando outra coluna
cadastro
{'Notas': [('João', 'J720'),
  ('Maria', 'M205'),
  ('José', 'J371'),
  ('Cláudia', 'C546'),
  ('Ana', 'A347')],
 'Média Final': [[8.0, 9.0, 10.0],
  [9.0, 7.0, 6.0],
  [3.4, 7.0, 7.0],
  [5.5, 6.6, 8.0],
  [6.0, 10.0, 9.5]],
 'Situação': [9.0, 7.3, 5.8, 6.7, 8.5],
 'Estudante': ['João', 'Maria', 'José', 'Cláudia', 'Ana']}




*****************************************EXERCICIOS*****************************************



1. Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
COPIAR CÓDIGO
2. Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
COPIAR CÓDIGO
3. A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.

4. Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
COPIAR CÓDIGO
5. Crie um dicionário usando o dict comprehension em que as chaves estão na lista meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] e os valores estão em despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360].

Aplicando a projetos
6. Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa filtrar somente os dados do ano 2022 com venda maior do que 6000. A loja forneceu uma amostra contendo apenas as colunas com os anos e os valores de venda para que você ajude a realizar a filtragem dos dados a partir de um código:

vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
COPIAR CÓDIGO
Crie uma lista usando list comprehension para filtrar os valores de 2022 e que sejam maiores que 6000.

7. Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose em um banco de dados e gostaria de rotular os dados da seguinte maneira:

Glicose igual ou inferior a 70: 'Hipoglicemia'
Glicose entre 70 a 99: 'Normal'
Glicose entre 100 e 125: 'Alterada'
Glicose superior a 125: 'Diabetes'
A clínica disponibilizou parte dos valores e sua tarefa é criar uma lista de tuplas usando list comprehension contendo o rótulo e o valor da glicemia em cada tupla.

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
COPIAR CÓDIGO
8. Um e-commerce possui as informações de id de venda, quantidade vendida e preço do produto divididos nas seguintes listas:

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]
COPIAR CÓDIGO
O e-commerce precisa estruturar esses dados em uma tabela contendo o valor total da venda, que é obtida multiplicando a quantidade pelo preço unitário. Além disso, a tabela precisa conter um cabeçalho indicando as colunas: 'id', 'quantidade', 'preco' e 'total'.

Crie uma lista de tuplas em que cada tupla tenha id, quantidade, preço e valor total, na qual a primeira tupla é o cabeçalho da tabela.

9. Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil. Em uma das tabelas de cadastro das filiais há uma coluna contendo a informação de qual é o Estado a que pertence: estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG'].

A empresa sempre está abrindo novas filiais, de modo que a tabela está constantemente recebendo novos registros e o gestor gostaria de possuir a informação atualizada da quantidade de filiais em cada Estado.

A partir da coluna com a informação dos Estados, crie um dicionário usando dict comprehension com a chave sendo o nome de um Estado e o valor sendo a contagem de vezes em que o Estado aparece na lista.

Dica: Você pode fazer um passo intermediário para gerar uma lista de listas em que cada uma das listas possui o nome de apenas um Estado com valores repetidos.

10. Nessa mesma tabela de cadastro de filiais, há uma coluna com as informações da quantidade de pessoas colaboradoras e o(a) gestor(a) gostaria de ter um agrupamento da soma dessas pessoas para cada estado. As informações contidas na tabela são:

funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]
COPIAR CÓDIGO
A partir da lista de tuplas, crie um dicionário em que as chaves são os nomes dos Estados únicos e os valores são as listas com o número de colaboradores(as) referentes ao Estado. Crie também um dicionário em que as chaves são os nomes dos Estados e os valores são a soma de colaboradores(as) por Estado.

Dica: Você pode fazer um passo intermediário para gerar uma lista de listas em que cada uma das listas possui apenas os valores numéricos de funcionários(as) de cada Estado.

VER OPINIÃO DO INSTRUTOR
Opinião do instrutor

Podem existir diversas formas de solucionar os problemas propostos e algumas delas são apresentadas a seguir.

Aquecimento
1.

for lista in lista_de_listas:
    print(sum(lista))
COPIAR CÓDIGO
2.

lista = []
for tupla in lista_de_tuplas:
    lista.append(tupla[2])
print(lista)
COPIAR CÓDIGO
3.

lista_de_tuplas = []
for i in range(len(lista)):
    lista_de_tuplas.append((i, lista[i]))
print(lista_de_tuplas)
COPIAR CÓDIGO
4.

lista = [tupla[1] for tupla in aluguel if tupla[0]== 'Apartamento']
print(lista)
COPIAR CÓDIGO
5.

dicionario = {meses[i]: despesa[i] for i in range(len(meses))}
print(dicionario)
COPIAR CÓDIGO
Aplicando a projetos
6.

filtro = [tupla[1] for tupla in vendas if tupla[0] == '2022' and tupla[1] > 6000]
print(filtro)
COPIAR CÓDIGO
7.

rotulos = [('Hipoglicemia', glicose) if glicose <= 70 else ('Normal', glicose) if glicose < 100 else ('Alterada', glicose) if glicose < 125 else ('Diabetes', glicose) for glicose in glicemia]
print(rotulos)
COPIAR CÓDIGO
8.

tabela = [('id', 'quantidade', 'preco', 'total')]
tabela += [(id[i], quantidade[i], preco[i], quantidade[i]*preco[i]) for i in range(len(id))]
COPIAR CÓDIGO
9.

# Armazenando os estados sem repetição de valor
estados_unicos = list(set(estados))

# Criando uma lista de listas com valores repetidos de cada estado
lista_de_listas = []
for estado in estados_unicos:
    lista = [uf for uf in estados if uf == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)

# Criando um dicionário em que a chave é o nome de cada estado único e o valor é a contagem de elementos
contagem_valores = {estados_unicos[i]: len(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(contagem_valores)
COPIAR CÓDIGO
10.

# Armazenando os estados sem repetição de valor
estados_unicos = list(set([tupla[0] for tupla in funcionarios]))

# Criando uma lista de listas com valores de funcionários de cada estado
lista_de_listas = []
for estado in estados_unicos:
    lista = [tupla[1] for tupla in funcionarios if tupla[0] == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)

# Criando um dicionário com dados agrupados de funcionário por estado
agrupamento_por_estado = {estados_unicos[i]: lista_de_listas[i] for i in range(len(estados_unicos))}
print(agrupamento_por_estado)

# Criando um dicionário com a soma de funcionários por estado
soma_por_estado = {estados_unicos[i]: sum(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(soma_por_estado)




*****************************************TRATANDO EXCEÇÃO*****************************************

try:
  nome = input('Digite o nome: ')
  resultado = notas[nome] 
except KeyError:
  print("Estudante não matriculado(a) na turma")
  
try:
  nome = input('Digite o nome: ')
  resultado = notas[nome] 
except KeyError:
  print("Estudante não matriculado(a) na turma")
else:
  print(resultado)
  
try:
  nome = input('Digite o nome: ')
  resultado = notas[nome] 
except KeyError:
  print("Estudante não matriculado(a) na turma")
else:
  print(resultado)
finally:
  print("A consulta foi encerrada!")



def media(lista: list=[0]) -> float:
  ''' Função para calcular a média de notas passadas por uma lista

  lista: list, default [0]
    Lista com as notas para calcular a média
  return = calculo: float
    Média calculada
  '''
  
  calculo = sum(lista) / len(lista)

  if len(lista) > 4:
    raise ValueError("A lista não pode possuir mais de 4 notas.")

  return calculo

try:
  notas = [6, 7, 8, 9]
  resultado = media(notas)
except TypeError: 
  print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!")
except ValueError as e:
  print(e)
else:
  print(resultado)
finally
  print("A consulta foi encerrada")