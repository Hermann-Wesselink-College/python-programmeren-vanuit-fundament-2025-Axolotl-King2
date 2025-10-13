#Opdracht 4
jaar = 0
saldo = 100
while saldo < 400:
    jaar += 1
    saldo *= 1.1
print('jaar is: ' + str(jaar), 'saldo is: ' + str(saldo))

#opdracht 5
jaar2 = 0
saldo2 = 100000
opname = 5000
while ((saldo2 * 1.04) - opname) >0:
    saldo *= 1.04
    saldo -= opname
    jaar += 1
    if jaar2 >= 100:
        print('Je kan dit bedrag je hele leven opnemen')
        break
    else:
        print('dit kan ' + str(jaar2) + ' jaar')
        break