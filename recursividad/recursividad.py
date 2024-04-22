# def sumatoria(value):
#     if value > 0:
#         resultado = value + sumatoria(value-1)
#         return resultado
#     else:
#         return 0
    
# resultado = sumatoria(8)

# print(sumatoria)


# def sumatoria(value):
#     #condicion de corte
#     if value == 0:
#         return 0
#     #proceso recursivo
#     return value + sumatoria(value-1)
    
# resultado = sumatoria(8)

# print(sumatoria)

#factorial while (no recursivo)

# def factorial(value):
#     resultado = value
#     while value > 2:
#         value = value - 1
#         resultado = resultado * value
#     return resultado

# resultado = factorial(5)
# print(resultado)

#factorial recursivo

# def factorial(value):
#     #condicion de corte
#     if value in (0,1):
#         return 1
#     #llamada recursiva
#     return value * factorial(value-1)

# resultado = factorial(5)
# print(resultado)

#fibonacci con while


# def fibonacci(value):
#     values = [0,1]

#     for _ in range(value-1):
#         values.append(values[-1]+values[-2])
  
#     return values[value]

# resultado = fibonacci(13)
# print(resultado)

# def fibonacci(value):
#     anterior,resultado = 0,1 #asignacion multiple de variables, solo en python
#     for _ in range(value-1):
#         anterior,resultado=resultado,anterior+resultado
#     return resultado

# resultado = fibonacci(13)
# print(resultado)

# def fibonacci(value):
#     #condicion de corte
#     if value == 0:
#         return 0
#     if value == 1:
#         return 1
#     #llamada recursiva
#     return fibonacci(value-1) + fibonacci(value-2)
# resultado = fibonacci(130)
# print(resultado)


