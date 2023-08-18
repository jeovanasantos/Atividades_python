num1 = int (input('Digite um numero? '))
num2 = int (input('Digite um numero? '))
num3 = int (input('Digite um numero? '))
      
if (num1 > num2) and (num1 > num3):
     maior = num1
elif (num2 > num1) and (num2 > num3):
      maior = num2
elif (num3 > num1) and (num3 > num2):
       maior = num3
else:
    print("Todos os valores sao iguais!")
        print(f"O maior numero entre {num1}, {num2} e {num3} é {maior}")
 
