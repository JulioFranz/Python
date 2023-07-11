P=float(input('Digite o peso de peixes: '))
E=float
M=float
if(P>50):
    E=P-50
    M=E*4
    print('Sua multa é de: ', M , 'Reais')
else:
    E=0
    M=0
    print('Sua multa é de:' , M , 'Reais')