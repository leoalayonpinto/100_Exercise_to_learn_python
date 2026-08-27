#instrucciones 'if' 'else' 'elif' +
#declarar variable

var=input('Introducir el valor ')
var=int(var)

if isinstance(var,str) == True:
    print('Cadena de Caracteres')
elif isinstance(var,int) == True:
    print('Entero')

#esta es otra forma de determinar el tipo de variable

if type(var)==str:
    print('Cadena de Caracteres')
if type(var)==int:
    print('Entero')

