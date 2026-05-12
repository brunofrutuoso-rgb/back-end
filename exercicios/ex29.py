velocidade = float(input("Qual é a velocidade atual do carro em km/h? "))
if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido de 80km/h.")
    km_acima = velocidade - 80
    multa = km_acima * 7
    print(f"O valor da multa é de R${multa:.2f}!")
else:
    print("Tenha um bom dia! Dirija com segurança.")
