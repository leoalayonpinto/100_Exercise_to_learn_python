#handle tuples, sort tuples using the key=lambda to access to the second item of the tuples there are other ways to do that.

L=[('Manzana',15),('Banana',8),('Fresa',12),('kiwi',9),('Melocotón',2)]
L.sort(key=lambda value:value[1],reverse=False)

print(L)


