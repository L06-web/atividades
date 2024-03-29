comprimento = float(input("Digite o comprimento do terreno em metros: "))
largura = float(input("Digite a largura do terreno em metros: "))
precometrotela = float(input("Digite o preço do metro de tela em reais: "))
perimetro = 2 * (comprimento + largura)
custotela = perimetro * precometrotela
print(f"O custo para cercar o terreno com tela é de R${custotela:.2f}")
