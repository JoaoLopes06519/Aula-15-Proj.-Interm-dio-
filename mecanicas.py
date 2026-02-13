precovendadacia = 20000
precovendapeugeot = 35000
precostockdacia = 15000
precostockpeugeot = 40000
saldoatualCLIENTE = 40000
saldoatualSTAND = 5000
stockDACIASANDERO = 30
stockPEUGEOT3008 = 15


def comprarCarro(saldoCliente, custoTotal):
    saldoCliente -= custoTotal
    return saldoCliente
def gerir_stock(saldoatualSTAND):
    escolha = int(input("Queres encher o stock do 1- DACIA SANDERO ou do 2- PEUGEOT3008?"))
    if escolha == 1:
        verificaçãostockdacia = int(input("Quanto dinheiro é que tu tens?"))
        if verificaçãostockdacia <15000:
            print("Não podes comprar")
            return escolha
        if verificaçãostockdacia >=15000:
            print("Podes comprar")
            saldoatualSTAND = saldoatualSTAND - 15000
            print(saldoatualSTAND)

    if escolha == 2:
         verificaçãostockpeugeot = int(input("Quanto dinheiro é que tu tens?"))
         if verificaçãostockpeugeot == "Não":
             print("Não tens dinheiro suficiente")
             return escolha
         if verificaçãostockpeugeot >= 15000:
             print("Podes comprar")
             saldoatualSTAND = saldoatualSTAND - 15000
             print(saldoatualSTAND)
