def checkSpeed():

    speed = 121

    if speed <= 80:
        print('Você esta dentro da velocidade')
    else:
        tax = 0
        if speed > 80 and speed < 100:
            tax = 5 * (speed - 80)
        elif speed >= 100:
            tax = 5 * 20

        if speed > 100 and speed < 120:
            tax = tax + (10 * (speed - 100))
        elif speed >= 120:
            tax = tax + (10 * 20)

        if speed > 120:
            tax = tax + (20 * (speed - 120))

        print('Você excedeu o limite de velocidade que é 80Km/h')
        print(f"Sua multa é de: {tax} Reais")

def seeCalc():
    option = input('Deseja Iniciar a Calculadora? (S/N)')
    while option != 's' and option != 'n' and option != 'S' and option != 'N':
        option = input('Digite S ou N')
    if option == 's':
        print('Voce Iniciou a calcudora')
        num1 = int(input('Digite um numero para realizar a operação'))
        num2 =  int(input('Digite outro numero para realizar a operação'))
        op = input('Digite o tipo de operação que vc deseja realizar +, -, *, /')
        while op != '+' and op != '-' and op != '*' and op != '/':
             op = input('Digite o tipo de operação que vc deseja realizar +, -, *, /')  
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        else:
            result = num1 / num2
        print(f'O Resultado da sua operação é {result}')
    else:
        print('Você nao quis iniciar a calculadora')
            

seeCalc()