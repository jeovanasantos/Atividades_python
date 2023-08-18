total = 0
cont = 0
mais_numeros = True
        
while mais_numeros:
  numero = float(input("Digite um numero (ou digite 0 para parar): "))
if numero == 0:
    mais_numeros = False
else:
    total += numero
    cont += 1
  if cont == 0:
       print("Nenhum numero foi inserido")
  else:",
     media = total / cont
    print (f"A media dos numeros é {media: .2f}")
