#inicio do programa

#titulo para ficar bonitinho
print("**************************************")
print("*Bem Vindo(a) a calculadora em python*")
print("**************************************")

#variaveis dos numeros que a pessoa escolhe para fazer as operações
num1 = int(input("Digite o valor do primeiro numero aqui: "))
num2 = int(input("Digite o valor do segundo numero aqui: "))

#variáveis das operações matemáticas

#operação de soma
soma = num1 + num2
#operação de subtração
subtracao = num1 - num2
#operação de divisão
divisao = num1 / num2
#operação de multiplicação
multiplicacao = num1 * num2

#função que executa a operacao matematica determinada pelo usuário
def executar_operacao ():
    #inicio loop
    #estrutura de repetição while(1) -> significa que é um loop infinito até que algo pare ele
    while(1):
    
        #imprimir as opções de operações matemáticas na tela
        print("Escolha qual operação matemática voce deseja fazer com os números: (1/soma),(2/subtração),(3/divisão),(4/mulriplicação)")
        #variável que recebe o numero designado para cada operação matemática
        operacao = int(input())

        #condição para que se a pessoa digitar um numero que não condiz com os designados para cada operação não continuar
        if(operacao < 1 or operacao > 4):
            print("Voce deve escolher um numero entre 1 e 4")
            continue

        #condição para que cada operação possa funcionar caso selecionada
        if(operacao == 1):
            print("A soma de ",num1, "+",num2,"é de ",soma,)
            #para encerrar a repetição assim que esse bloco de condição seja executado
            break
        elif(operacao == 2):
            print("A subtração de ",num1, "-",num2, "é de ",subtracao,)
            #para encerrar a repetição assim que esse bloco de condição seja executado
            break
        elif(operacao == 3):
            print("A divisão de ",num1, "/",num2, "é de ", divisao,)
            #para encerrar a repetição assim que esse bloco de condição seja executado
            break
        else:
            print("A mmultiplicação de ",num1, "*",num2, "é de ", multiplicacao,)
            #para encerrar a repetição assim que esse bloco de condição seja executado
            break
        #fim loop

#executar a função
executar_operacao()

#fim do programa