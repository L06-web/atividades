horainicial = int(input("Digite a hora inicial: "))
minutoinicial = int(input("Digite o minuto inicial: "))
segundoinicial = int(input("Digite o segundo inicial: "))
duracaosegundos = int(input("Digite a duração em segundos: "))
totalsegundosinicial = horainicial * 3600 + minutoinicial * 60 + segundoinicial
totalsegundosfinal = totalsegundos_inicial + duracaosegundos
horafinal = totalsegundosfinal // 3600 % 24
minutofinal = (totalsegundosfinal % 3600) // 60
segundofinal = totalsegundosfinal % 60
print(f"O término da experiência será às {horafinal} horas, {minutofinal} minutos e {segundofinal} segundos.")
