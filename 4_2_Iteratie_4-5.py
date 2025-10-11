#Opdracht 4
jaar = 0
saldo = 100
while saldo < 400:
    jaar = jaar + 1
    saldo = saldo * 1.1
print('jaar is: ' + str(jaar))
print('saldo is: ' + str(saldo))

#opdracht 5
jaar2 = 0
saldo2 = 100000
opname = 5000
while saldo2 <1000000:
    if jaar2 >= 100:
        print('Je kan dit bedrag je hele leven opnemen')
        break
    else:
        saldo2 = saldo2 * 1.04 - opname
        jaar2 = jaar2 + 1
        print('dit kan ' + str(jaar2) + ' jaar')