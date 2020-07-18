def resta(a, b):
    return a - b

print(resta(4,2))

print(resta(b=2, a=5))


def resta(a=None, b=None):
    if (a == None or b == None):
        print("Error debes enviar dos numeros a la función")
    else:
        return a - b


print(resta(1, 7))

# ARGUMENTOS POR VALOR Y REFERENCIA.
def doblar_valor(numero):
    numero *= 2

n = 10
doblar_valor(n)
print(n)

# LAS LISTAS SE PASAN POR REFERENCIA(AFECTA O MODIFICAN SU VALOR EXTERNO)
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [1, 10, 20, 30]
doblar_valores(ns)
print(ns)


# OTRO EJEMPLO PASO POR Valor
def doblar_valor(numero):
    return numero * 2
n = 10

print(doblar_valor(n))