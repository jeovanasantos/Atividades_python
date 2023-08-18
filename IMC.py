nome = input('Qual o seu nome? ')
peso = float (input('Qual o seu peso? '))
altura = float(input('Qual a sua altura '))
imc = peso/altura ** 2
if imc < 18.5:
     print(f'{nome} voce esta abaixo do peso ideal')
else:
   if imc > 24.5:
     print(f'{nome} voce esta acima do peso ideal ')
   else:
        print(f'{nome} voce esta com peso ideal ')
 
