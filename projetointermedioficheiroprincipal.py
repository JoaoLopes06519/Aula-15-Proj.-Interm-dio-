import time
import mecanicas
from mecanicas import saldoatualCLIENTE

precodacia = 20000
precopeugeot = 35000

print("BEM-VINDO AO STAND AUTOMÓVEL")
def escolha_menu():
     escolha = int(input("Quais destas opções preferes, 1-DACIA SANDERO, 2- PEUGEOT 3008, 3- STOCK, 4- SAIR"))
     time.sleep(1)
     while escolha != 4:
        time.sleep(1)
        if escolha == 1:
            quantdacias = int(input("Quantos dacias queres?"))
            totalapagardacia = quantdacias * precodacia
            time.sleep(1)
            if quantdacias > mecanicas.stockDACIASANDERO:
                print("Não temos dacias suficientes")
            if totalapagardacia > mecanicas.saldoatualCLIENTE:
                print("Não tens dinheiro suficiente")
            if totalapagardacia <= mecanicas.saldoatualCLIENTE:
                mecanicas.saldoatualCLIENTE= mecanicas.comprarCarro(mecanicas.saldoatualCLIENTE, totalapagardacia)
                print(f"Total a pagar:{totalapagardacia}\nSaldo atual:{mecanicas.saldoatualCLIENTE}")



            mecanicas.saldoatualSTAND += totalapagardacia
            mecanicas.saldoatualCLIENTE -= totalapagardacia

        if escolha == 2:
          quantpeugeot = int(input("Quantos Peugeot queres?"))
          totalapagarpeugeot = quantpeugeot * precopeugeot
          time.sleep(1)
          if quantpeugeot > 30:
              print("Não temos Peugeot suficientes")

          if quantpeugeot <= 30:
              if totalapagarpeugeot > 40000:
                  print("Não tens dinheiro suficiente")
              if totalapagarpeugeot <= 40000:
                  print(f"Total a pagar:{totalapagarpeugeot}")
                  mecanicas.saldoatualCLIENTE = mecanicas.comprarCarro(mecanicas.saldoatualCLIENTE, totalapagardacia)
                  print(f"Total a pagar:{totalapagardacia}\nSaldo atual:{mecanicas.saldoatualCLIENTE}")

              mecanicas.saldoatualSTAND += totalapagarpeugeot
              mecanicas.saldoatualCLIENTE -= totalapagarpeugeot

        if escolha == 3:
           mecanicas.gerir_stock()

        escolha = int(input("Quais destas opções preferes, 1- DACIA SANDERO, 2- PEUGEOT 3008, 3- STOCK, 4- SAIR"))

escolha_menu()

