# Recebe os dados do funcionário
cargo = input("Digite o cargo do funcionário (gerente, analista, estagiário): ").strip().lower()
dia = input("Digite o dia da semana (ex: segunda-feira): ").strip().lower()

# Define os dias úteis
dias_uteis = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

# Verifica acesso conforme o cargo
if cargo == "gerente":
    print("Acesso permitido.")
elif cargo in ["analista", "estagiário"]:
    if dia in dias_uteis:
        print("Acesso permitido.")
    else:
        print("Acesso negado.")
else:
    print("Cargo não reconhecido. Acesso negado.")
