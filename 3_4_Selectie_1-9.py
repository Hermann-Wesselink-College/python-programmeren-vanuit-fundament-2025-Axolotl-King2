# Opdrachten 1 tot en met 9 van paragraaf 3.4
artikelen = int(input('how veel artikelen heeft u?'))
oldprijs = int(input('wat is de prijs per artikel?'))
prijs = artikelen*oldprijs
if prijs > 150:
	newprijs = prijs*1.19
else:
    newprijs = prijs*1.16
print('de nieuwe prijs is = €', newprijs)
