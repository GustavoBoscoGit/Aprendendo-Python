from conta import Conta

conta1 = Conta(321, "Gustavo", 2000, 2700.0)

resposta = input("O que deseja realizar: (1) extrato - (2) deposito - (3) saque\n")



if resposta == "1":
    conta1.extrato()
elif resposta == "2":
    valor = input("Informe o valor para deposito\n")
    conta1.deposito(float (valor))
elif resposta == "3":
    valor = input("Informe o valor para saque\n")
    conta1.saque(float (valor))
a = 2



