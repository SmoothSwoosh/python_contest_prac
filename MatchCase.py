class Spell:
	LIGTHNING = 'Shreklight'
	FIREBALL = 'FireballZZZ'


	def __init__(self, type=None, strength=0):
		self.type = type
		self.strength = strength


while s := input():
	match s.split():
		case ['move', direction]:
			match direction:
				case 'right':
					print('moved->')
				case 'left':
					print('<-moved')
				case _:
					print('Unknown movement direction')
		case ['about']:
			print('MUD version 0.01')
		case ['credits']:
			print('Copyright (c) developers')
		case ['credits', '--year']:
			print('Copyright (c) developers THIS YEAR')
		case ['quit']:
			break
		case _:
			print('Cannot parse')

