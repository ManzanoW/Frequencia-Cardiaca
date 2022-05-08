'''Esse programa pede os batimentos cardíacos por minuto e a idade do usuário, e indica se eles
 se encontram dentro da faixa adequada'''
#pedido da idade e a frequencia cardiaca
batimentos = int(input("Digite seus batimentos por minuto (BPM): "))
idade = int(input("Digite sua idade: "))
#verificacao das condicoes ate 2 anos com o if encadeado
if (idade <= 2) and ((batimentos >= 120) and (batimentos <= 140)):
    print("Seus batimentos se encontram dentro da faixa adequada!")
elif (idade <= 2) and (batimentos < 120):
    print("Seus batimentos se encontram abaixo da faixa adequada.")
elif (idade <= 2) and (batimentos > 120):
    print ("Seus batimentos cardiacos se encontram acima da faixa adequada.")
#verificacao das condicoes de 8 ate 17 anos
elif ((idade >= 8) and (idade <= 17)) and ((batimentos >= 80) and (batimentos <= 100)):
    print ("Seus batimentos cardiacos se encontram dentro da faixa adequada!")
elif ((idade >= 8) and (idade <= 17)) and (batimentos < 80):
    print("Seus batimentos cardiacos se encontram abaixo da faixa adequada.")
elif ((idade >= 8) and (idade <= 17)) and (batimentos > 80):
    print("Seus batimentos cardiacos se encontram acima da faixa adequada.")
#verificacao das condicoes para adultos
elif ((idade >= 18) and (idade <= 59)):
    #verificacao se o usuario pratica exercicios fisicos ou nao
    condicao = input("Voce faz exercicios fisicos com regularidade? S-SIM e N-NAO: ")
    #verificacao das condicoes para adultos que praticam exercicios fisicos
    if (condicao.replace("s","S") == "S") and ((batimentos >= 50) and (batimentos <= 60)):
        print("Seus batimentos cardiacos se encontram dentro da faixa adequada!")
    elif (condicao.replace("s","S") == "S") and (batimentos < 50):
        print("Seus batimentos se encontram abaixo da faixa adequada.")
    elif (condicao.replace("s","S") == "S") and (batimentos > 60):
        print("Seus batimentos se encontram acima da faixa adequada.")
        #verificacao das condicoes para adultos sedentarios
    if (condicao.replace("n","N") == "N") and ((batimentos >= 70) and (batimentos <= 80)):
        print("Seus batimentos se encontram dentro da faixa adequada!")
    elif (condicao.replace("n","N") == "N") and (batimentos < 70):
        print("Seus batimentos se encontram abaixo da faixa adequada.")
    elif (condicao.replace("n","N") == "N") and (batimentos > 80):
        print("Seus batimentos se encontram acima da faixa adequada.")
#verificacao das condicoes para idosos
elif (idade >= 60) and ((batimentos >= 50) and (batimentos <= 60)):
    print("Seus batimentos se encontram dentro da faixa adequada!")
elif batimentos < 50:
    print("Seus batimentos se encontram abaixo da faixa adequada.")
else:
    print("Seus batimentos se encontram acima da faixa adequada.")




