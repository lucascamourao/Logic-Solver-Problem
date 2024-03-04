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

# DEFINING VARIABLES ==========================================================================================================================

# Color of the houses

C1Red = Bool('C1Red') # the house 1 is red
C1Green = Bool('C1Green') # the house 1 is green
C1Ivory = Bool('C1Ivory') # the house 1 is  ivory
C1Yellow = Bool('C1Yellow') # the house 1 is yellow
C1Blue = Bool('C1Blue') # the house 1 is blue

C2Red = Bool('C2Red') # the house 2 is red
C2Green = Bool('C2Green') # the house 2 is green
C2Ivory = Bool('C2Ivory') # the house 2 is ivory
C2Yellow = Bool('C2Yellow') # the house 2 is yellow
C2Blue = Bool('C2Blue') # the house 2 is blue

C3Red = Bool('C3Red') # the house 3 is red
C3Green = Bool('C3Green') # the house 3 is green
C3Ivory = Bool('C3Ivory') # the house 3 is ivory
C3Yellow = Bool('C3Yellow') # the house 3 is yellow
C3Blue = Bool('C3Blue') # the house 3 is blue

C4Red = Bool('C4Red') # a casa 4 é vermelha
C4Green = Bool('C4Green') # a casa 4 é verde
C4Ivory = Bool('C4Ivory') # a casa 4 é marfim
C4Yellow = Bool('C4Yellow') # a casa 4 é amarela
C4Blue = Bool('C4Blue') # a casa 4 é azul

C5Red = Bool('C5Red') # a casa 5 é vermelha
C5Green = Bool('C5Green') # a casa 5 é verde
C5Ivory = Bool('C5Ivory') # a casa 5 é marfim
C5Yellow = Bool('C5Yellow') # a casa 5 é amarela
C5Blue = Bool('C5Blue') # a casa 5 é azul

# Nationality of the residents of each house

C1Surinames = Bool('C1Surinames') # o surinamês mora na casa 1
C1Espanhol = Bool('C1Espanhol') # o espanhol mora na casa 1
C1Equatoriano = Bool('C1Equatoriano') # o equatoriano mora na casa 1
C1Noruegues = Bool('C1Noruegues') # o noruegues mora na casa 1
C1Japones = Bool('C1Japones') # o japones mora na casa 1

C2Surinames = Bool('C2Surinames') # o surinamês mora na casa 2
C2Espanhol = Bool('C2Espanhol') # o espanhol mora na casa 2
C2Equatoriano = Bool('C2Equatoriano') # o equatoriano mora na casa 2
C2Noruegues = Bool('C2Noruegues') # o noruegues mora na casa 2
C2Japones = Bool('C2Japones') # o japones mora na casa 2

C3Surinames = Bool('C3Surinames') # o surinamês mora na casa 3
C3Espanhol = Bool('C3Espanhol') # o espanhol mora na casa 3
C3Equatoriano = Bool('C3Equatoriano') # o equatoriano mora na casa 3
C3Noruegues = Bool('C3Noruegues') # o noruegues mora na casa 3
C3Japones = Bool('C3Japones') # o japones mora na casa 3

C4Surinames = Bool('C4Surinames') # o surinamês mora na casa 4
C4Espanhol = Bool('C4Espanhol') # o espanhol mora na casa 4
C4Equatoriano = Bool('C4Equatoriano') # o equatoriano mora na casa 4
C4Noruegues = Bool('C4Noruegues') # o noruegues mora na casa 4
C4Japones = Bool('C4Japones') # o japones mora na casa 4

C5Surinames = Bool('C5Surinames') # o surinamês mora na casa 5
C5Espanhol = Bool('C5Espanhol') # o espanhol mora na casa 5
C5Equatoriano = Bool('C5Equatoriano') # o equatoriano mora na casa 5
C5Noruegues = Bool('C5Noruegues') # o noruegues mora na casa 5
C5Japones = Bool('C5Japones') # o japones mora na casa 5

# Animal of each house

C1Dog = Bool('C1Dog') # o animal da casa 1 é o cachorro
C1Squirrel = Bool('C1Squirrel') # o animal da casa 1 é o esquilo
C1Fox = Bool('C1Fox') # o animal da casa 1 é a raposa
C1Toucan = Bool('C1Toucan') # o animal da casa 1 é o tucano
C1Horse = Bool('C1Horse') # o animal da casa 1 é o cavalo

C2Dog = Bool('C2Dog') # o animal da casa 2 é o cachorro
C2Squirrel = Bool('C2Squirrel') # o animal da casa 2 é o esquilo
C2Fox = Bool('C2Fox') # o animal da casa 2 é a raposa
C2Toucan = Bool('C2Toucan') # o animal da casa 2 é o tucano
C2Horse = Bool('C2Horse') # o animal da casa 2 é o cavalo

C3Dog = Bool('C3Dog') # o animal da casa 3 é o cachorro
C3Squirrel = Bool('C3Squirrel') # o animal da casa 3 é o esquilo
C3Fox = Bool('C3Fox') # o animal da casa 3 é a raposa
C3Toucan = Bool('C3Toucan') # o animal da casa 3 é o tucano
C3Horse = Bool('C3Horse') # o animal da casa 3 é o cavalo

C4Dog = Bool('C4Dog') # o animal da casa 4 é o cachorro
C4Squirrel = Bool('C4Squirrel') # o animal da casa 4 é o esquilo
C4Fox = Bool('C4Fox') # o animal da casa 4 é a raposa
C4Toucan = Bool('C4Toucan') # o animal da casa 4 é o tucano
C4Horse = Bool('C4Horse') # o animal da casa 4 é o cavalo

C5Dog = Bool('C5Dog') # o animal da casa 5 é o cachorro
C5Squirrel = Bool('C5Squirrel') # o animal da casa 5 é o esquilo
C5Fox = Bool('C5Fox') # o animal da casa 5 é a raposa
C5Toucan = Bool('C5Toucan') # o animal da casa 5 é o tucano
C5Horse = Bool('C5Horse') # o animal da casa 5 é o cavalo

# Drink of each house

C1Coffee = Bool('C1Coffee') # café é servido na casa 1
C1Milk = Bool('C1Milk') # leite é servido na casa 1
C1Orange = Bool('C1Orange') # suco de laranja é servido na casa 1
C1Tea = Bool('C1Tea') # chá é servido na casa 1
C1Water = Bool('C1Water') # água é servido na casa 1

C2Coffee = Bool('C2Coffee') # café é servido na casa 2
C2Milk = Bool('C2Milk') # leite é servido na casa 2
C2Orange = Bool('C2Orange') # suco de laranja é servido na casa 2
C2Tea = Bool('C2Tea') # chá é servido na casa 2
C2Water = Bool('C2Water') # água é servido na casa 2

C3Coffee = Bool('C3Coffee') # café é servido na casa 3
C3Milk = Bool('C3Milk') # leite é servido na casa 3
C3Orange = Bool('C3Orange') # suco de laranja é servido na casa 3
C3Tea = Bool('C3Tea') # chá é servido na casa 3
C3Water = Bool('C3Water') # água é servido na casa 3

C4Coffee = Bool('C4Coffee') # café é servido na casa 4
C4Milk = Bool('C4Milk') # leite é servido na casa 4
C4Orange = Bool('C4Orange') # suco de laranja é servido na casa 4
C4Tea = Bool('C4Tea') # chá é servido na casa 4
C4Water = Bool('C4Water') # água é servido na casa 4

C5Coffee = Bool('C5Coffee') # café é servido na casa 5
C5Milk = Bool('C5Milk') # leite é servido na casa 5
C5Orange = Bool('C5Orange') # suco de laranja é servido na casa 5
C5Tea = Bool('C5Tea') # chá é servido na casa 5
C5Water = Bool('C5Water') # água é servido na casa 5

# Musical instrument of each house

C1Saxo = Bool('C1Saxo') # saxofone é tocado na casa 1
C1Violin = Bool('C1Violin') # violino é tocado na casa 1
C1Piano = Bool('C1Piano') # piano é tocado na casa 1
C1Oboe = Bool('C1Oboe') # oboé é tocado na casa 1
C1Atab = Bool('C1Atab') # atabaques é tocado na casa 1

C2Saxo = Bool('C2Saxo') # saxofone é tocado na casa 2
C2Violin = Bool('C2Violin') # violino é tocado na casa 2
C2Piano = Bool('C2Piano') # piano é tocado na casa 2
C2Oboe = Bool('C2Oboe') # oboé é tocado na casa 2
C2Atab = Bool('C2Atab') # atabaques é tocado na casa 2

C3Saxo = Bool('C3Saxo') # saxofone é tocado na casa 3
C3Violin = Bool('C3Violin') # violino é tocado na casa 3
C3Piano = Bool('C3Piano') # piano é tocado na casa 3
C3Oboe = Bool('C3Oboe') # oboé é tocado na casa 3
C3Atab = Bool('C3Atab') # atabaques é tocado na casa 3

C4Saxo = Bool('C4Saxo') # saxofone é tocado na casa 4
C4Violin = Bool('C4Violin') # violino é tocado na casa 4
C4Piano = Bool('C4Piano') # piano é tocado na casa 4
C4Oboe = Bool('C4Oboe') # oboé é tocado na casa 4
C4Atab = Bool('C4Atab') # atabaques é tocado na casa 4

C5Saxo = Bool('C5Saxo') # saxofone é tocado na casa 5
C5Violin = Bool('C5Violin') # violino é tocado na casa 5
C5Piano = Bool('C5Piano') # piano é tocado na casa 5
C5Oboe = Bool('C5Oboe') # oboé é tocado na casa 5
C5Atab = Bool('C5Atab') # atabaques é tocado na casa 5

# Each house has only ONE color

f1 = Or([And([C1Red, Not(C1Green), Not(C1Ivory), Not(C1Yellow), Not(C1Blue)]), And([Not(C1Red), C1Green, Not(C1Ivory), Not(C1Yellow), Not(C1Blue)]), And([Not(C1Red), Not(C1Green), C1Ivory, Not(C1Yellow),
Not(C1Blue)]), And([Not(C1Red), Not(C1Green), Not(C1Ivory), C1Yellow, Not(C1Blue)]), And([Not(C1Red), Not(C1Green), Not(C1Ivory), Not(C1Yellow), C1Blue])])

f2 = Or([And([C2Red, Not(C2Green), Not(C2Ivory), Not(C2Yellow), Not(C2Blue)]), And([Not(C2Red), C2Green, Not(C2Ivory), Not(C2Yellow), Not(C2Blue)]), And([Not(C2Red), Not(C2Green), C2Ivory, Not(C2Yellow),
Not(C2Blue)]), And([Not(C2Red), Not(C2Green), Not(C2Ivory), C2Yellow, Not(C2Blue)]), And([Not(C2Red), Not(C2Green), Not(C2Ivory), Not(C2Yellow), C2Blue])])

f3 = Or([And([C3Red, Not(C3Green), Not(C3Ivory), Not(C3Yellow), Not(C3Blue)]), And([Not(C3Red), C3Green, Not(C3Ivory), Not(C3Yellow), Not(C3Blue)]), And([Not(C3Red), Not(C3Green), C3Ivory, Not(C3Yellow),
Not(C3Blue)]), And([Not(C3Red), Not(C3Green), Not(C3Ivory), C3Yellow, Not(C3Blue)]), And([Not(C3Red), Not(C3Green), Not(C3Ivory), Not(C3Yellow), C3Blue])])

f4 = Or([And([C4Red, Not(C4Green), Not(C4Ivory), Not(C4Yellow), Not(C4Blue)]), And([Not(C4Red), C4Green, Not(C4Ivory), Not(C4Yellow), Not(C4Blue)]), And([Not(C4Red), Not(C4Green), C4Ivory, Not(C4Yellow),
Not(C4Blue)]), And([Not(C4Red), Not(C4Green), Not(C4Ivory), C4Yellow, Not(C4Blue)]), And([Not(C4Red), Not(C4Green), Not(C4Ivory), Not(C4Yellow), C4Blue])])

f5 = Or([And([C5Red, Not(C5Green), Not(C5Ivory), Not(C5Yellow), Not(C5Blue)]), And([Not(C5Red), C5Green, Not(C5Ivory), Not(C5Yellow), Not(C5Blue)]), And([Not(C5Red), Not(C5Green), C5Ivory, Not(C5Yellow),
Not(C5Blue)]), And([Not(C5Red), Not(C5Green), Not(C5Ivory), C5Yellow, Not(C5Blue)]), And([Not(C5Red), Not(C5Green), Not(C5Ivory), Not(C5Yellow), C5Blue])])

# Cada casa tem só um morador de UMA nacionalidade
# Each house has only one resident of ONE nationality

f6 = Or([And([C1Surinames, Not(C1Espanhol), Not(C1Equatoriano), Not(C1Noruegues), Not(C1Japones)]), And([Not(C1Surinames), C1Espanhol, Not(C1Equatoriano), Not(C1Noruegues), Not(C1Japones)]), And([Not(C1Surinames), Not(C1Espanhol),
C1Equatoriano, Not(C1Noruegues), Not(C1Japones)]), And([Not(C1Surinames), Not(C1Espanhol), Not(C1Equatoriano), C1Noruegues, Not(C1Japones)]), And([Not(C1Surinames), Not(C1Espanhol), Not(C1Equatoriano), Not(C1Noruegues), C1Japones])])

f7 = Or([And([C2Surinames, Not(C2Espanhol), Not(C2Equatoriano), Not(C2Noruegues), Not(C2Japones)]), And([Not(C2Surinames), C2Espanhol, Not(C2Equatoriano), Not(C2Noruegues), Not(C2Japones)]), And([Not(C2Surinames), Not(C2Espanhol),
C2Equatoriano, Not(C2Noruegues), Not(C2Japones)]), And([Not(C2Surinames), Not(C2Espanhol), Not(C2Equatoriano), C2Noruegues, Not(C2Japones)]), And([Not(C2Surinames), Not(C2Espanhol), Not(C2Equatoriano), Not(C2Noruegues), C2Japones])])

f8 = Or([And([C3Surinames, Not(C3Espanhol), Not(C3Equatoriano), Not(C3Noruegues), Not(C3Japones)]), And([Not(C3Surinames), C3Espanhol, Not(C3Equatoriano), Not(C3Noruegues), Not(C3Japones)]), And([Not(C3Surinames), Not(C3Espanhol),
C3Equatoriano, Not(C3Noruegues), Not(C3Japones)]), And([Not(C3Surinames), Not(C3Espanhol), Not(C3Equatoriano), C3Noruegues, Not(C3Japones)]), And([Not(C3Surinames), Not(C3Espanhol), Not(C3Equatoriano), Not(C3Noruegues), C3Japones])])

f9 = Or([And([C4Surinames, Not(C4Espanhol), Not(C4Equatoriano), Not(C4Noruegues), Not(C4Japones)]), And([Not(C4Surinames), C4Espanhol, Not(C4Equatoriano), Not(C4Noruegues), Not(C4Japones)]), And([Not(C4Surinames), Not(C4Espanhol),
C4Equatoriano, Not(C4Noruegues), Not(C4Japones)]), And([Not(C4Surinames), Not(C4Espanhol), Not(C4Equatoriano), C4Noruegues, Not(C4Japones)]), And([Not(C4Surinames), Not(C4Espanhol), Not(C4Equatoriano), Not(C4Noruegues), C4Japones])])

f10 = Or([And([C5Surinames, Not(C5Espanhol), Not(C5Equatoriano), Not(C5Noruegues), Not(C5Japones)]), And([Not(C5Surinames), C5Espanhol, Not(C5Equatoriano), Not(C5Noruegues), Not(C5Japones)]), And([Not(C5Surinames), Not(C5Espanhol),
C5Equatoriano, Not(C5Noruegues), Not(C5Japones)]), And([Not(C5Surinames), Not(C5Espanhol), Not(C5Equatoriano), C5Noruegues, Not(C5Japones)]), And([Not(C5Surinames), Not(C5Espanhol), Not(C5Equatoriano), Not(C5Noruegues), C5Japones])])

# Each house has only ONE animal

f11 = Or([And([C1Dog, Not(C1Squirrel), Not(C1Fox), Not(C1Toucan), Not(C1Horse)]), And([Not(C1Dog), C1Squirrel, Not(C1Fox), Not(C1Toucan), Not(C1Horse)]), And([Not(C1Dog), Not(C1Squirrel),
C1Fox, Not(C1Toucan), Not(C1Horse)]), And([Not(C1Dog), Not(C1Squirrel), Not(C1Fox), C1Toucan, Not(C1Horse)]), And([Not(C1Dog), Not(C1Squirrel), Not(C1Fox), Not(C1Toucan), C1Horse])])

f12 = Or([And([C2Dog, Not(C2Squirrel), Not(C2Fox), Not(C2Toucan), Not(C2Horse)]), And([Not(C2Dog), C2Squirrel, Not(C2Fox), Not(C2Toucan), Not(C2Horse)]), And([Not(C2Dog), Not(C2Squirrel),
C2Fox, Not(C2Toucan), Not(C2Horse)]), And([Not(C2Dog), Not(C2Squirrel), Not(C2Fox), C2Toucan, Not(C2Horse)]), And([Not(C2Dog), Not(C2Squirrel), Not(C2Fox), Not(C2Toucan), C2Horse])])

f13 = Or([And([C3Dog, Not(C3Squirrel), Not(C3Fox), Not(C3Toucan), Not(C3Horse)]), And([Not(C3Dog), C3Squirrel, Not(C3Fox), Not(C3Toucan), Not(C3Horse)]), And([Not(C3Dog), Not(C3Squirrel),
C3Fox, Not(C3Toucan), Not(C3Horse)]), And([Not(C3Dog), Not(C3Squirrel), Not(C3Fox), C3Toucan, Not(C3Horse)]), And([Not(C3Dog), Not(C3Squirrel), Not(C3Fox), Not(C3Toucan), C3Horse])])

f14 = Or([And([C4Dog, Not(C4Squirrel), Not(C4Fox), Not(C4Toucan), Not(C4Horse)]), And([Not(C4Dog), C4Squirrel, Not(C4Fox), Not(C4Toucan), Not(C4Horse)]), And([Not(C4Dog), Not(C4Squirrel),
C4Fox, Not(C4Toucan), Not(C4Horse)]), And([Not(C4Dog), Not(C4Squirrel), Not(C4Fox), C4Toucan, Not(C4Horse)]), And([Not(C4Dog), Not(C4Squirrel), Not(C4Fox), Not(C4Toucan), C4Horse])])

f15 = Or([And([C5Dog, Not(C5Squirrel), Not(C5Fox), Not(C5Toucan), Not(C5Horse)]), And([Not(C5Dog), C5Squirrel, Not(C5Fox), Not(C5Toucan), Not(C5Horse)]), And([Not(C5Dog), Not(C5Squirrel),
C5Fox, Not(C5Toucan), Not(C5Horse)]), And([Not(C5Dog), Not(C5Squirrel), Not(C5Fox), C5Toucan, Not(C5Horse)]), And([Not(C5Dog), Not(C5Squirrel), Not(C5Fox), Not(C5Toucan), C5Horse])])

# Each house only serves ONE drink

f16 = Or([And([C1Coffee, Not(C1Milk), Not(C1Orange), Not(C1Tea), Not(C1Water)]), And([Not(C1Coffee), C1Milk, Not(C1Orange), Not(C1Tea), Not(C1Water)]), And([Not(C1Coffee), Not(C1Milk), C1Orange,
Not(C1Tea), Not(C1Water)]), And([Not(C1Coffee), Not(C1Milk), Not(C1Orange), C1Tea, Not(C1Water)]), And([Not(C1Coffee), Not(C1Milk), Not(C1Orange), Not(C1Tea), C1Water])])

f17 = Or([And([C2Coffee, Not(C2Milk), Not(C2Orange), Not(C2Tea), Not(C2Water)]), And([Not(C2Coffee), C2Milk, Not(C2Orange), Not(C2Tea), Not(C2Water)]), And([Not(C2Coffee), Not(C2Milk), C2Orange,
Not(C2Tea), Not(C2Water)]), And([Not(C2Coffee), Not(C2Milk), Not(C2Orange), C2Tea, Not(C2Water)]), And([Not(C2Coffee), Not(C2Milk), Not(C2Orange), Not(C2Tea), C2Water])])

f18 = Or([And([C3Coffee, Not(C3Milk), Not(C3Orange), Not(C3Tea), Not(C3Water)]), And([Not(C3Coffee), C3Milk, Not(C3Orange), Not(C3Tea), Not(C3Water)]), And([Not(C3Coffee), Not(C3Milk), C3Orange,
Not(C3Tea), Not(C3Water)]), And([Not(C3Coffee), Not(C3Milk), Not(C3Orange), C3Tea, Not(C3Water)]), And([Not(C3Coffee), Not(C3Milk), Not(C3Orange), Not(C3Tea), C3Water])])

f19 = Or([And([C4Coffee, Not(C4Milk), Not(C4Orange), Not(C4Tea), Not(C4Water)]), And([Not(C4Coffee), C4Milk, Not(C4Orange), Not(C4Tea), Not(C4Water)]), And([Not(C4Coffee), Not(C4Milk), C4Orange,
Not(C4Tea), Not(C4Water)]), And([Not(C4Coffee), Not(C4Milk), Not(C4Orange), C4Tea, Not(C4Water)]), And([Not(C4Coffee), Not(C4Milk), Not(C4Orange), Not(C4Tea), C4Water])])

f20 = Or([And([C5Coffee, Not(C5Milk), Not(C5Orange), Not(C5Tea), Not(C5Water)]), And([Not(C5Coffee), C5Milk, Not(C5Orange), Not(C5Tea), Not(C5Water)]), And([Not(C5Coffee), Not(C5Milk), C5Orange,
Not(C5Tea), Not(C5Water)]), And([Not(C5Coffee), Not(C5Milk), Not(C5Orange), C5Tea, Not(C5Water)]), And([Not(C5Coffee), Not(C5Milk), Not(C5Orange), Not(C5Tea), C5Water])])

# Each resident of each house only plays ONE musical instrument

f21 = Or([And([C1Saxo, Not(C1Violin), Not(C1Piano), Not(C1Oboe), Not(C1Atab)]), And([Not(C1Saxo), C1Violin, Not(C1Piano), Not(C1Oboe), Not(C1Atab)]), And([Not(C1Saxo), Not(C1Violin), C1Piano, Not(C1Oboe), Not(C1Atab)]),
And([Not(C1Saxo), Not(C1Violin), Not(C1Piano), C1Oboe, Not(C1Atab)]), And([Not(C1Saxo), Not(C1Violin), Not(C1Piano), Not(C1Oboe), C1Atab])])

f22 = Or([And([C2Saxo, Not(C2Violin), Not(C2Piano), Not(C2Oboe), Not(C2Atab)]), And([Not(C2Saxo), C2Violin, Not(C2Piano), Not(C2Oboe), Not(C2Atab)]), And([Not(C2Saxo), Not(C2Violin), C2Piano, Not(C2Oboe), Not(C2Atab)]),
And([Not(C2Saxo), Not(C2Violin), Not(C2Piano), C2Oboe, Not(C2Atab)]), And([Not(C2Saxo), Not(C2Violin), Not(C2Piano), Not(C2Oboe), C2Atab])])

f23 = Or([And([C3Saxo, Not(C3Violin), Not(C3Piano), Not(C3Oboe), Not(C3Atab)]), And([Not(C3Saxo), C3Violin, Not(C3Piano), Not(C3Oboe), Not(C3Atab)]), And([Not(C3Saxo), Not(C3Violin), C3Piano, Not(C3Oboe), Not(C3Atab)]),
And([Not(C3Saxo), Not(C3Violin), Not(C3Piano), C3Oboe, Not(C3Atab)]), And([Not(C3Saxo), Not(C3Violin), Not(C3Piano), Not(C3Oboe), C3Atab])])

f24 = Or([And([C4Saxo, Not(C4Violin), Not(C4Piano), Not(C4Oboe), Not(C4Atab)]), And([Not(C4Saxo), C4Violin, Not(C4Piano), Not(C4Oboe), Not(C4Atab)]), And([Not(C4Saxo), Not(C4Violin), C4Piano, Not(C4Oboe), Not(C4Atab)]),
And([Not(C4Saxo), Not(C4Violin), Not(C4Piano), C4Oboe, Not(C4Atab)]), And([Not(C4Saxo), Not(C4Violin), Not(C4Piano), Not(C4Oboe), C4Atab])])

f25 = Or([And([C5Saxo, Not(C5Violin), Not(C5Piano), Not(C5Oboe), Not(C5Atab)]), And([Not(C5Saxo), C5Violin, Not(C5Piano), Not(C5Oboe), Not(C5Atab)]), And([Not(C5Saxo), Not(C5Violin), C5Piano, Not(C5Oboe), Not(C5Atab)]),
And([Not(C5Saxo), Not(C5Violin), Not(C5Piano), C5Oboe, Not(C5Atab)]), And([Not(C5Saxo), Not(C5Violin), Not(C5Piano), Not(C5Oboe), C5Atab])])


# O surinamês mora na casa vermelha
f26 = Or([And([C1Red, C1Surinames]), And([C2Red, C2Surinames]), And([C3Red, C3Surinames]), And([C4Red, C4Surinames]), And([C5Red, C5Surinames])])

#  O espanhol é dono de um cachorro
f27 = Or([And([C1Dog, C1Espanhol]), And([C2Dog, C2Espanhol]), And([C3Dog, C3Espanhol]), And([C4Dog, C4Espanhol]), And([C5Dog, C5Espanhol])])

# Café é bebido na casa verde
f28 = Or([And([C1Coffee, C1Green]), And([C2Coffee, C2Green]), And([C3Coffee, C3Green]), And([C4Coffee, C4Green]), And([C5Coffee, C5Green])])

# O equatoriano bebe chá
f29 = Or([And([C1Tea, C1Equatoriano]), And([C2Tea, C2Equatoriano]), And([C3Tea, C3Equatoriano]), And([C4Tea, C4Equatoriano]), And([C5Tea, C5Equatoriano])])

# A casa verde é imediatamente à direita da casa cor de marfim
f30 = Or([And([C1Green, C2Ivory]), And([C2Green, C3Ivory]), And([C3Green, C4Ivory]), And([C4Green, C5Ivory])]) # depende do referencial
# 1  2  3  4  5 --> C2 está a direita de C3

# O violinista é dono de um esquilo
f31 = Or([And([C1Squirrel, C1Violin]), And([C2Squirrel, C2Violin]), And([C3Squirrel, C3Violin]), And([C4Squirrel, C4Violin]), And([C5Squirrel, C5Violin])])

# Um piano é tocado na casa amarela
f32 = Or([And([C1Piano, C1Yellow]), And([C2Piano, C2Yellow]), And([C3Piano, C3Yellow]), And([C4Piano, C4Yellow]), And([C5Piano, C5Yellow])])

# Leite é bebido na casa do meio
f33 = And([C3Milk]) # pode ser Or([C3Milk])

# O norueguês mora na primeira casa
f34 = And([C1Noruegues])

# A pessoa que toca oboé mora na casa vizinha a da pessoa que tem uma raposa
f35 = Or([And([C1Oboe, C2Fox]), And([C2Oboe, C3Fox]), And([C2Oboe, C1Fox]), And([C3Oboe, C4Fox]), And([C3Oboe, C2Fox]), And([C4Oboe, C5Fox]), And([C4Oboe, C3Fox]), And([C5Oboe, C4Fox])])

# Um piano é tocado na casa vizinha aonde um cavalo é criado
f36 = Or([And([C1Piano, C2Horse]), And([C2Piano, C3Horse]), And([C2Piano, C1Horse]), And([C3Piano, C4Horse]), And([C3Piano, C2Horse]), And([C4Piano, C5Horse]), And([C4Piano, C3Horse]), And([C5Piano, C4Horse])])

# O contrabaixista bebe suco de laranja
f37 = Or([And([C1Orange, C1Violin]), And([C2Orange, C2Violin]), And([C3Orange, C3Violin]), And([C4Orange, C4Violin]), And([C5Orange, C5Violin])])

# O japonês toca saxofone
f38 = Or([And([C1Saxo, C1Japones]), And([C2Saxo, C2Japones]), And([C3Saxo, C3Japones]), And([C4Saxo, C4Japones]), And([C5Saxo, C5Japones])])

# O norueguês mora na casa vizinha à casa azul
f39 = Or([And([C1Noruegues, C2Blue]), And([C2Noruegues, C3Blue]), And([C2Noruegues, C1Blue]), And([C3Noruegues, C4Blue]), And([C3Noruegues, C2Blue]), And([C4Noruegues, C5Blue]), And([C4Noruegues, C3Blue]), And([C5Noruegues, C4Blue])])

''' INFORMAÇÕES ADICIONAIS:
A polícia ambiental foi chamada após o gorjear de um tucano ser ouvido por um desses cinco moradores
Um garrafão de água é pontualmente entregue toda terça-feira às 13:13 
'''
''' ADICIONAL INFORMATION:
The environmental police were called after the chirping of a toucan was heard by one of these five residents
A water carboy is delivered punctually every Tuesday at 1:13 pm.
'''

f40 = And([f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36, f37, f38, f39])

s = Solver()
s.add(f40)

print(s.check())

if s.check() == sat:
# O próximo comando obtém um modelo satisfatível, SE existe
# The next command gets a satisfiable model, IF it exists
  m = s.model()

# Imprimindo apenas os símbolos proposicionais verdadeiros
# Printing only the true propositional symbols 
  for prop in m: # for each element in the 'm' model
    if m[prop] == True:
      print(prop)
