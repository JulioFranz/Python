print('Calculo de Multa da pesca!')
def pedir_valor():
    peso=float(input('Digite o peso em Kg (Ex. 55.0): '))
    if(peso<0):
        print('Peso Invalido\n')
        pedir_valor()
    else:
        print('Peso Coletado com Sucesso')
        return peso
    
pt=pedir_valor()
if(pt<50):
    print('Sua multa é de R$0,00')
else:
    E=float(pt-50)
    M=float(E*4)
    print('Sua multa é de R$',M,'reais')