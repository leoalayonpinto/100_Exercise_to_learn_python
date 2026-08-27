# Work with dictionaries https://docs.python.org/3/tutorial/datastructures.html
dic={'Manzana':15, 'Pera':20, 'Naranja':10,'Kiwi':10,'Melon':10}
# method 1
total=0
for value in dic.values():
    total=total+value
print(total)

# method 2

print(int(sum(dic.values())))