from datetime import date

current_year = date.today().year #  pega o ano atual
nome = input(" Qual o seu nome: ")
idade = int(input(" Qual a sua idade: "))
ano = str((current_year - idade) + 100) # Subtrai o ano atual pela idade e soma com 100
print(nome + ", voce tera 100 anos em "+ ano)
