print('Calculadora de Peso Ideal!')
h=float(input('Insira sua altura: '))
S=str(input('Insira seu Sexo: '))
PI=float
if(h<=0) or (h>200):
    print('Peso Invalido')
if(S!='Feminino') and (S!='Masculino'):
    print('Sexo Invalido')
elif(S=='Masculino'):
    PI=72.7*h-58
    print(PI)
elif(S=='Feminino'):
    PI=62.1*h-44.7
    print(PI)

