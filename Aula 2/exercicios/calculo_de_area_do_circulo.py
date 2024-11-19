import math  # Importo o módulo math para acessar o valor de pi

# Peço ao usuário para digitar o valor do raio
raio = float(input("Escreva o raio a ser calculado: "))

# Calculo a área do círculo usando a fórmula: área = pi * raio^2
area = math.pi * (raio ** 2)

# Exibo o resultado formatado com 4 casas decimais, conforme solicitado
print(f"A={area:.4f}")