investimentoamigo1 = float(input("Digite o valor investido pelo amigo 1: "))
investimentoamigo2 = float(input("Digite o valor investido pelo amigo 2: "))
investimentoamigo3 = float(input("Digite o valor investido pelo amigo 3: "))
valorpremio = float(input("Digite o valor do prêmio: "))
totalinvestido = investimentoamigo1 + investimentoamigo2 + investimentoamigo3
proporcaoamigo1 = investimentoamigo1 / totalinvestido
proporcaoamigo2 = investimentoamigo2 / totalinvestido
proporcaoamigo3 = investimentoamigo3 / totalinvestido
premioamigo1 = proporcaoamigo1 * valorpremio
premioamigo2 = proporcaoamigo2 * valorpremio
premioamigo3 = proporcaoamigo3 * valorpremio
print(f"O amigo 1 ganharia R${premioamigo1:.2f}")
print(f"O amigo 2 ganharia R${premioamigo2:.2f}")
print(f"O amigo 3 ganharia R${premioamigo3:.2f}")
