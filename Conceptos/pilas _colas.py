# NO EXISTEN LAS PILAS COMO TAL EN PYTHON. PERO SE PUEDEN SIMULAR.
# UNA PILA ES UNA COLECCIÓN DE ELEMENTOS ORDENADOS
# SE PUEDE AÑADIR UN ELEMENTO A LA PILA O SE PUEDE SACAR UN ELEMENTO DE LA PILA
# LIFO -Last In First Out | El ultimo en entrar, es el primero en salir

# SIMULAR UNA PILA EN PYTHON
pila = [3, 4, 5]
pila.append(6)
pila.append(7)
pila.append(8)
print(pila)

print(pila.pop())

n = pila.pop()
print(pila)

# NO SE PUEDE USAR EL METODO POP SI LA LISTA O PILA ESTA VACIA.

# COLAS, NO EXISTEN EN PYTHON PERO SE PUEDEN SIMULAR.
# FIFO(FIRST IN FIRST OUT)PRIMERO EN ENTRAR, ES EL PRIMERO EN SALIR
# PARA SIMULAR LA COLA DEBEMOS IMPORTAR UNA LIBRERIA
from collections import deque

cola = deque()
print(cola)

cola = deque(['Javier', 'Claudia', 'Yanina'])
print(cola)

cola.append('Maria')
cola.append('Bruce')
print(cola)
# SACAR UN ELEMENTO
cola.popleft()
print(cola)