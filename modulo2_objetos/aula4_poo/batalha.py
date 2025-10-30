from cavaleiro import Cavaleiro


if __name__ == "__main__":

    # Criando cavaleiros
    arthur = Cavaleiro("Arthur", "Camelot")
    lancelot = Cavaleiro("Lancelot", "Britânia")

    print("=== BATALHA ÉPICA ===")
    print(arthur.status())
    print(lancelot.status())

    # Batalha simples
    rodada = 1
    while arthur.esta_vivo() and lancelot.esta_vivo():
        print(f"\n--- Rodada {rodada} ---")
        
        arthur.atacar(lancelot)
        print(lancelot.status())
        
        if lancelot.esta_vivo():
            lancelot.atacar(arthur)
            print(arthur.status())
        
        rodada += 1

    # Resultado
    if arthur.esta_vivo():
        print(f"\n {arthur.nome} venceu!")
    else:
        print(f"\n {lancelot.nome} venceu!")