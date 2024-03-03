#  Logic Solver Problem using Z3 Theorem Prover

''' Assuma que cada habitação é pintada com uma cor diferente e nela mora uma pessoa de nacionalildade
diferente que bebe uma bebida diferente, toca um instrumento musical diferente e possui um animal
diferente. Determine a cor de cada casa, a nacionalidade do seu morador, o instrumento musical que ele
toca, o que bebe e o animal que possui. '''

''' Assume each house is painted a different color and there lives a person of different and unique nationality. 
Each person drinks a different drink, plays a different musical instrument and has a different animal. 
Determine the color of each house, the nationality of its resident, the instrument they play, what they drink
and what animal they own. 
'''

from z3 import *

# Definição das casas
houses = [Int(f"house{i}") for i in range(1, 6)]

# Definição das cores
colors = [Const(f"color{i}", IntSort()) for i in range(1, 6)]

# Definição das nacionalidades
nationalities = [Const(f"nationality{i}", IntSort()) for i in range(1, 6)]

# Definição das bebidas
drinks = [Const(f"drink{i}", IntSort()) for i in range(1, 6)]

# Definição dos instrumentos
instruments = [Const(f"instrument{i}", IntSort()) for i in range(1, 6)]

# Definição dos animais
animals = [Const(f"animal{i}", IntSort()) for i in range(1, 6)]

# Criação do solucionador Z3
solver = Solver()

# Restrições para as cores
for i in range(1, 6):
    solver.add(And(colors[i-1] >= 1, colors[i-1] <= 5))
    solver.add(Distinct(colors))

# Restrições para as nacionalidades
for i in range(1, 6):
    solver.add(And(nationalities[i-1] >= 1, nationalities[i-1] <= 5))
    solver.add(Distinct(nationalities))

# Restrições para as bebidas
for i in range(1, 6):
    solver.add(And(drinks[i-1] >= 1, drinks[i-1] <= 5))
    solver.add(Distinct(drinks))

# Restrições para os instrumentos
for i in range(1, 6):
    solver.add(And(instruments[i-1] >= 1, instruments[i-1] <= 5))
    solver.add(Distinct(instruments))

# Restrições para os animais
for i in range(1, 6):
    solver.add(And(animals[i-1] >= 1, animals[i-1] <= 5))
    solver.add(Distinct(animals))

# Restrições adicionais do problema
solver.add(Distinct(houses))

# O surinamês mora na casa vermelha
solver.add(Nacionalidade(houses.index(1)+1, colors.index("red")+1))

# O espanhol é dono de um cachorro
solver.add(Nacionalidade(houses.index(1)+1, animals.index("dog")+1))

# Café é bebido na casa verde
solver.add(Bebida(houses.index(1)+1, colors.index("green")+1))

# O equatoriano bebe chá
solver.add(Nacionalidade(houses.index(1)+1, drinks.index("tea")+1))

# A casa verde é imediatamente à direita da casa cor de marfim
solver.add(colors.index("green") - colors.index("ivory") == 1)

# O violinista é dono de um esquilo
solver.add(Instrumento(houses.index(1)+1, instruments.index("violin")+1))
solver.add(Animal(houses.index(1)+1, animals.index("squirrel")+1))

# Um piano é tocado na casa amarela
solver.add(Instrumento(houses.index(1)+1, instruments.index("piano")+1))
solver.add(Cor(houses.index(1)+1, colors.index("yellow")+1))

# Leite é bebido na casa do meio
solver.add(Bebida(houses.index(1)+1, drinks.index("milk")+1))

# O norueguês mora na primeira casa
solver.add(Nacionalidade(houses.index(1)+1, nationalities.index("norwegian")+1))

# A pessoa que toca oboé mora na casa vizinha a da pessoa que tem uma raposa
solver.add(Instrumento(houses.index(1)+1, instruments.index("oboe")+1))
solver.add(Animal(houses.index(1)+1, animals.index("fox")+1))
solver.add(Or(houses.index(1) - houses.index(2) == 1, houses.index(1) - houses.index(2) == -1))

# Um piano é tocado na casa vizinha aonde um cavalo é criado
solver.add(Instrumento(houses.index(1)+1, instruments.index("piano")+1))
solver.add(Animal(houses.index(1)+1, animals.index("horse")+1))
solver.add(Or(houses.index(1) - houses.index(2) == 1, houses.index(1) - houses.index(2) == -1))

# O contrabaixista bebe suco de laranja
solver.add(Instrumento(houses.index(1)+1, instruments.index("contrabass")+1))
solver.add(Bebida(houses.index(1)+1, drinks.index("orange juice")+1))

# O japonês toca saxofone
solver.add(Nacionalidade(houses.index(1)+1, nationalities.index("japanese")+1))
solver.add(Instrumento(houses.index(1)+1, instruments.index("saxophone")+1))

# O norueguês mora na casa vizinha à casa azul
solver.add(Nacionalidade(houses.index(1)+1, nationalities.index("norwegian")+1))
solver.add(Cor(houses.index(1)+1, colors.index("blue")+1))
solver.add(Or(houses.index(1) - houses.index(2) == 1, houses.index(1) - houses.index(2) == -1))

# A polícia ambiental foi chamada após o gorjear de um tucano ser ouvido por um desses cinco moradores
solver.add(Animal(houses.index(1)+1, animals.index("toucan")+1))

# Verificação da solução
if solver.check() == sat:
    model = solver.model()
    for house in houses:
        house_num = model[house].as_long()
        print(f"Casa {house_num}:")
        print(f"Cor: {model[colors[house_num - 1]]}")
        print(f"Nacionalidade: {model[nationalities[house_num - 1]]}")
        print(f"Bebida: {model[drinks[house_num - 1]]}")
        print(f"Instrumento: {model[instruments[house_num - 1]]}")
        print(f"Animal: {model[animals[house_num - 1]]}")
        print()
else:
    print("Não foi possível encontrar uma solução.")
