import time

import mecanicas

precodacia = 20000
precopeugeot = 40000
precocontinental = 50


print("BEM-VINDO AO STAND AUTOMÓVEL")
def escolha_menu():
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
                mecanicas.saldoatualSTAND += totalapagardacia
                mecanicas.saldoatualCLIENTE -= totalapagardacia
                print(f"Total a pagar:{totalapagardacia}\nSaldo atual:{mecanicas.saldoatualCLIENTE}")



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


              mecanicas.saldoatualSTAND += totalapagarpneuscontinental
              mecanicas.saldoatualCLIENTE -= totalapagarpneuscontinental

        if escolha == 4:
            mecanicas.saldoatualSTAND, stock, escolha_temporaria = mecanicas.gerir_stock(mecanicas.saldoatualSTAND, mecanicas.stockDACIASANDERO, mecanicas.stockPEUGEOT3008, mecanicas.stockPNEUSCONTINENTAL)
            if escolha_temporaria == 1:
                mecanicas.stockDACIASANDERO = stock
            elif escolha_temporaria == 2:
                mecanicas.stockPEUGEOT3008 = stock
            elif escolha_temporaria == 3:
                mecanicas.stockPNEUSCONTINENTAL = stock


        escolha = int(input("Quais destas opções preferes, 1- DACIA SANDERO, 2- PEUGEOT 3008, 3- PNEUS CONTINENTAL 4- STOCK, 5- SAIR"))

escolha_menu()

