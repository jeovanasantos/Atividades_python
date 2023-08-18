import random

num = random.randint(1,9)
jog = 0
while True:
player = int(input(\"Chute um numero: "))
jog += 1
if player < num:
  print('errou, tente um numero maior')
elif player > num:\n",
  print('errou, tente um numero menor')
else:
  print(f'acertou com {jog} tentativas')
 break
      
  
  
