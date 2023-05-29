import random

# definimos las estadísticas iniciales de los personajes
ataque_A = 10
defensa_A = 5
vida_A = 100

ataque_B = 8
defensa_B = 6
vida_B = 10000

# decidimos aleatoriamente quién empieza
turno = random.choice(['A', 'B'])


while vida_A > 0 and vida_B > 0:
    # turno del personaje A
    if turno == 'A':
        # el personaje A ataca al personaje B
        dano = ataque_A - defensa_B
        if dano > 0:
            vida_B -= dano
        print("A ataca a B y causa", dano, "puntos de daño. Vida de B:", vida_B)
        # cambiamos de turno
        turno = 'B'
    
    # turno del personaje B
    else:
        # el personaje B ataca al personaje A
        dano = ataque_B - defensa_A
        if dano > 0:
            vida_A -= dano
        print("B ataca a A y causa", dano, "puntos de daño. Vida de A:", vida_A)
        # cambiamos de turno
        turno = 'A'

# mensaje de fin del combate
if vida_A <= 0:
    print("B ha ganado el combate!")
else:
    print("A ha ganado el combate!")
