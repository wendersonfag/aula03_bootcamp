### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# quantidade = -20
# preco = 50

# if quantidade > 0 and preco > 0:
#     print("valores positivo")
# else:
#     print("Valores de quantidade ou preço invalido")


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:


# temperatura = 4

# if temperatura < 5:
#     print("baixa")
# elif temperatura >=5 and temperatura <=30:
#     print("normal")
# else:
#     print("Alta")


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'ERROR':
#     for i in log.keys():
#         print(log[i])



### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# email = "wenderson_fagundes@hotmail.com"
# idade = 34

# if (idade < 18 or  idade > 65):
#     print("Idade fora do intervalo permitido")
# elif "@" not in email or "." not in email:
#     print("Email inválido")
# else:
#     print("Dados de usuário válidos")



### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# transacao = {'valor': 12000, 'hora': 20}

# if transacao['hora'] < 9 or transacao['hora'] > 18:
#     print("Transação suspeita")
# else:
#     print("Transação realizada com sucesso")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# frase = "hoje é quinta, e hoje vai ser mas bonito do que vai ser amanhã que vai ser sexta"
# frase_ajuste  = frase.replace(",", "")
# frase_list  = frase_ajuste.split(" ")
# frase_dic  = {}


# for i in frase_list:
#     if i in frase_dic:
#         frase_dic[i] +=1
#     else:
#         frase_dic[i] =1

# print(frase_dic)



### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

# print(usuarios_validos)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# numeros = range(1, 11)
# pares  = []

# for i in numeros:
#     if i % 2 == 0:
#         pares.append(i)

# print(pares)

# numeros = range(1, 11)
# pares = [x for x in numeros if x % 2 == 0]

# print(pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# vendas_categoria = {}

# for i in vendas:
#     categoria = i["categoria"]
#     valor  = i["valor"]
#     if categoria in vendas_categoria:
#         vendas_categoria[categoria] += valor
#     else:
#         vendas_categoria[categoria]  = valor
# print(vendas_categoria)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# check = 'ficar'

# while check  == 'ficar':
#     print("continuar")
#     desejo = input("Digite sair se deseja sair: ")
#     if desejo == 'sair':
#         check = 'sair'

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
# numero = int(input("Digite um número entre 1 e 10: "))
# while numero < 1 or numero > 10:
#     print("Número fora do intervalo!")
#     numero = int(input("Por favor, digite um número entre 1 e 10: "))

# print("Número válido!")


### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# numero = 1
# total_pagina = 5

# while numero <= total_pagina:
#     print(f"Processando página {numero} de {total_pagina}")

#     numero += 1


### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# tentativas_maximas = 5
# tentativa = 1

# while tentativa <= tentativas_maximas:
#     print(f"Tentativa {tentativa} de {tentativas_maximas}")
#     # Simulação de uma tentativa de conexão
#     # Aqui iria o código para tentar conectar
#     if False:  # Suponha que a conexão foi bem-sucedida
#         print("Conexão bem-sucedida!")
#         break
#     tentativa += 1
# else:
#     print("Falha ao conectar após várias tentativas.")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.


lista = [1,2,3,4,5,'parar',6,7,8,10]

check = 0

while check <= len(lista): 
    if lista[check] == 'parar':
        print("valor encontrado")
        break
    else:
        print(f"Valor não encontrado, item processado: {lista[check]}")
        check += 1
        