import mecanicas

precodacia = 20000
precopeugeot = 35000

def escolha_menu():
  menu = int(input("Quais destas opções preferes, 1-DACIA SANDERO, 2- PEUGEOT 3008, 3- STOCK, 4- SAIR"))
  while menu != 4:
      escolha = int(input("Quais destas opções preferes, 1- DACIA SANDERO, 2- PEUGEOT 3008, 3- STOCK"))
      if escolha == 1:
              quantdacias = int(input("Quantos dacias queres?"))
              if quantdacias > 30:
                  return quantdacias
              if quantdacias <= 30:
                  totalapagardacia = quantdacias * precodacia
                  if totalapagardacia >40000:
                      print("Não tens dinheiro suficiente")
                  if totalapagardacia <=40000:
                      print(f"Total a pagar:{totalapagardacia}")
                  saldoatualSTAND1 = 5000 + totalapagardacia
                  saldoatualCLIENTE2 = 40000 - totalapagarpeugeot
              
      if escolha == 2:
          quantpeugeot = int(input("Quantos dacias queres?"))
          if quantpeugeot > 30:
              return quantpeugeot
          if quantpeugeot <= 30:
              totalapagarpeugeot = quantpeugeot * precopeugeot
              if totalapagardacia > 40000:
                  print("Não tens dinheiro suficiente")
              if totalapagardacia <= 40000:
                  print(f"Total a pagar:{totalapagarpeugeot}")
              saldoatualSTAND2 = 5000 + totalapagarpeugeot
              saldoatualCLIENTE2 = 40000 - totalapagarpeugeot

