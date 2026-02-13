import time
import mecanicas
from mecanicas import saldoatualCLIENTE, saldoatualSTAND

precodacia = 20000
precopeugeot = 35000
precocontinental = 50
listaitens = []

print("BEM-VINDO AO STAND AUTOMÓVEL")
def escolha_menu(saldoatualSTAND):
     escolha = int(input("Quais destas opções preferes, 1-DACIA SANDERO, 2- PEUGEOT 3008, 3- PNEUS CONTINENTAL, 4- STOCK, 5- SAIR"))
     time.sleep(0.5)
     while escolha != 5:
        time.sleep(0.5)
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
                listaitens.add("Dacia Sandero")


            mecanicas.saldoatualSTAND += totalapagardacia
            mecanicas.saldoatualCLIENTE -= totalapagardacia

        if escolha == 2:
          quantpeugeot = int(input("Quantos Peugeot queres?"))
          totalapagarpeugeot = quantpeugeot * precopeugeot
          time.sleep(0.5)
          if quantpeugeot > 30:
              print("Não temos Peugeot suficientes")

          if quantpeugeot <= 30:
              if totalapagarpeugeot > 40000:
                  print("Não tens dinheiro suficiente")
              if totalapagarpeugeot <= 40000:
                  print(f"Total a pagar:{totalapagarpeugeot}")
                  mecanicas.saldoatualCLIENTE = mecanicas.comprarCarro(mecanicas.saldoatualCLIENTE, totalapagarpeugeot)
                  print(f"Total a pagar:{totalapagarpeugeot}\nSaldo atual:{mecanicas.saldoatualCLIENTE}")
                  listaitens.add("Peugeot 3008")

              mecanicas.saldoatualSTAND += totalapagarpeugeot
              mecanicas.saldoatualCLIENTE -= totalapagarpeugeot

        if escolha == 3:
          quantpneuscontinental = int(input("Quantos pneus Continental queres?"))
          totalapagarpneuscontinental = quantpneuscontinental * precocontinental
          time.sleep(0.5)
          if quantpneuscontinental > 30:
              print("Não temos pneus suficientes")

          if quantpneuscontinental <= 30:
              if totalapagarpneuscontinental > 40000:
                  print("Não tens dinheiro suficiente")
              if totalapagarpneuscontinental <= 40000:
                  print(f"Total a pagar:{totalapagarpneuscontinental}")
                  mecanicas.saldoatualCLIENTE = mecanicas.comprarCarro(mecanicas.saldoatualCLIENTE, totalapagarpneuscontinental)
                  print(f"Total a pagar:{totalapagarpneuscontinental}\nSaldo atual:{mecanicas.saldoatualCLIENTE}")
                  listaitens.add("Pneu Continental")

              mecanicas.saldoatualSTAND += totalapagarpneuscontinental
              mecanicas.saldoatualCLIENTE -= totalapagarpneuscontinental

        if escolha == 4:
           mecanicas.gerir_stock(saldoatualSTAND)

        escolha = int(input("Quais destas opções preferes, 1- DACIA SANDERO, 2- PEUGEOT 3008, 3- PNEUS CONTINENTAL 4- STOCK, 5- SAIR"))

escolha_menu(saldoatualSTAND)

