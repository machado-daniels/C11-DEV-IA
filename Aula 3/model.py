from sklearn.linear_model import LinearRegression
import numpy as np

# Dados de treino
horas_estudo = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
notas = np.array([40, 50, 60, 70, 80])

# Modelo treinado
modelo = LinearRegression()
modelo.fit(horas_estudo, notas)

# Pergunta ao usuário o número de horas estudadas
horas = float(input("Digite o número de horas estudadas: "))

# Previsão - convertendo `horas` para um array 2D
nota_prevista = modelo.predict(np.array([[horas]]))

# Exibe o resultado
print(f"Com {horas} horas de estudo, a nota prevista é {nota_prevista[0]:.2f}")