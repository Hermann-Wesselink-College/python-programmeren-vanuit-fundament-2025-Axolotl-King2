# Opgave 3
# deel A
for i in range(1,11):
    print(i * 3)

# deel B
tafel = int(input('wat is de tafel die je gebruikt?'))
for i in range(1,11):
    print(tafel, ' x ', i, ' = ', i * tafel)

# deel C
tafel = int(input('wat is de tafel die je gebruikt?'))
if tafel <= 10 or tafel >= 0:
    for i in range(1,11):
        print(tafel, ' x ', i, ' = ', i * tafel)
else:
    print('De tafel hoeft niet weergeven te worden')

 # opdracht 4
print('een \t tab')
miles = 1.609
print('km \t miles')
for i in range(1,11):
    print(i ,'\t', i*miles)

#opdracht 5
getal = int(input('van welk getal wil je de faculteit?'))
faculteit = 1
for i in range(1,getal + 1):
    faculteit *= i
print('de faculteit van', getal, 'is', faculteit)

# opdracht 6
for i in range(0,51,2):
    print(i)

# opdracht 7
aantal = int(input('tot welk oneven getal wil je pi bereiken?'))
pi = 0.0
teken = 1
for i in range(1, aantal + 1, 2):
    pi += teken *(1/i)
    teken *= -1
pi *= 4
print("Benaderde waarde van π is:", pi)

# extra
klaar = ['ik', 'ben', 'klaar']
for i in klaar:
    print(i)