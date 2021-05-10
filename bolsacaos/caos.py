from random import randrange

def draw_caos (ctx):
  number = randrange (16)
  resultado = switch_demo(number)
  return resultado

def switch_demo(argument):
  switcher = {
    0: "<:SIMBOLOARCANO:678056537452707850>",
    1: "<:PULPOS:678056537016631317>",
    2: "<:SECTARIO:678056537725468672>",
    3: "<:PULMONES:678056537629130782>",
    4: "<:CALAVERA:678056538774044691>",
    5: "<:CALAMAR:678056538778370058>",
    6: "<:K1:835402649062080512>",
    7: "<:K0:835403217995169802>",
    8: "<:K_8:835405526409019402>",
    9: "<:K_7:835405511021035530>",
    10: "<:K_6:835405214176903178>",
    11: "<:K_5:835405151112003584>",
    12: "<:K_4:835404738543353896>",
    13: "<:K_3:835404433742364692>",
    14: "<:K_2:835403469794836508>",
    15: "<:K_1:835403235804184586>"
  }
  return switcher.get(argument)