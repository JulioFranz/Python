print('Determinar seu grau de obesidade')
def pedir_altura():
    altura = float(input('Digite sua altura em metros (por exemplo 1.75 m): '))
    if altura <= 0.50 or altura >= 2.70:
        print('Altura invalida\n')
        pedir_altura()
    else:
        print('Altura registrada com sucesso')
        return altura
    
print('Determinar seu grau de obesidade')
def pedir_peso():
    peso = float(input('Digite seu peso: '))
    if peso <= 0 or peso >= 250:
        print('Peso invalida\n')
        pedir_peso()
    else:
        print('Peso registrado com sucesso')
        return peso

altura = pedir_altura()
peso = pedir_peso()
imc = int(peso / altura**2)
if imc < 26:
    print('Normal')
elif imc < 30:
    print('Obeso')
else:
    print('Obeso morbido')