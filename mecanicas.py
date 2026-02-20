precostockdacia = 15000
precostockpeugeot = 35000
precostockpneu=10

saldoatualCLIENTE = 40000
saldoatualSTAND = 5000
stockDACIASANDERO = 5
stockPEUGEOT3008 = 5
stockPNEUSCONTINENTAL = 5

def comprarCarro(saldoCliente, custoTotal):
    saldoCliente -= custoTotal
    return saldoCliente
def gerir_stock(saldoAtualStand, stockDACIA, stockPEUGEOT, stockPNEUS):
    escolha = int(input("Queres encher o stock do 1- DACIA SANDERO, do 2- PEUGEOT3008 ou do 3- PNEUS CONTINENTAL?"))
    if escolha == 1:
        verificaçãostockdacia = saldoAtualStand
        if verificaçãostockdacia <15000:
            print("Não podes comprar")
        if verificaçãostockdacia >=15000:
            print("Podes comprar")
            saldoAtualStand -= 15000
            stock = stockDACIA + 1
            return saldoAtualStand, stock, escolha

    if escolha == 2:

         if saldoAtualStand < 35000:
             print("Não tens dinheiro suficiente")
         if saldoAtualStand >= 35000:
             print("Podes comprar")
             saldoAtualStand -= 35000
             stock = stockPEUGEOT + 1
             return saldoAtualStand, stock, escolha


    if escolha == 3:
        if precostockpneu <10:
            print("Não tens dinheiro suficiente")
        if precostockpneu >= 10:
            print("Podes comprar")
            saldoAtualStand -= 10
            stock = stockPNEUS+1
            return saldoAtualStand,stock,escolha




