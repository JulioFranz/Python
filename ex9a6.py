print('Determinar seu grau de obesidade!')
A=float(input('Digite sua Altura: '))
P=float(input('Digite seu Peso: '))
M=float
if(A<0.50) or (A>2.70):
    print('Altura Invalida')
elif(P<0) or (P>250):
    print('Peso Invalido')
else:
    M=P/(A**2)
    if(M<26):
        print('Normal')
    elif(M>=26) and (M<30):
        print('Obeso')
    elif(M>30):
        print('Obeso Morbido')

    


    