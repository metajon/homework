from random import randint
#
yeast = ['English Ale Yeast','American Ale Yeast','Belgian ALe Yeast','California Ale Yeast']
base_malt = ['Maris Otter','Vienna Malt','2-Row']
specialty_malt =['Oats','Flaked Barley','Un-malted wheat']
hops = {'Bittering Hops' : ['Cascade','Chinook','East Kent Golding','Willamette','Mt. Hood','Challenger'], 'Flavoring Hops' : ['Simcoe','East Kent Golding','Amarillo','None'], 'Aroma Hops' : ['Falconer\'s Flight','East Kent Golding','Amarillo','None']}
hops_qty = ['1/2 oz.','1 oz.']
hop_schedule = ['60 minutes','30 minutes','15 minutes','Flameout']
extract_qty = ['5#','5.5#','6#']
#
def specialty_grains(specialty_malt):
	my_specialty_grains = []
	for i in range(randint(0,2)):
		my_specialty_grains.append(specialty_malt[(randint(0,(len(specialty_malt)-1)))])
	if len(my_specialty_grains) > len(set(my_specialty_grains)):
		print '1 pound ' + my_specialty_grains[0]
	else:
		for i in range(len(my_specialty_grains)):
			print '1/2 pound ' + my_specialty_grains[i]
#
ingredients = [yeast,base_malt,extract_qty]
#
def make_recipe(ingredients):
	for i in range(len(ingredients)):
		print ingredients[i][(randint(0,(len(ingredients[i])-1)))]
#
def gen_hop_schedule(hops,hop_schedule):
	for i in range(len(hop_schedule)):
		if hop_schedule[i] == '60 minutes':
			print hop_schedule[i] + ': ' + hops_qty[(randint(0,(len(hops_qty)-1)))] + ' ' + hops['Bittering Hops'][(randint(0,(len( hops['Bittering Hops'] )-1)))]
		elif hop_schedule[i] == 'Flameout':
			this_hop = hops['Aroma Hops'][(randint(0,(len( hops['Aroma Hops'] )-1)))]
			if this_hop != 'None':
				this_qty = hops_qty[(randint(0,(len(hops_qty)-1)))]
			else:
				this_qty = ''
			print hop_schedule[i] + ': ' + this_qty + ' ' + this_hop
		else:
			this_hop = hops['Aroma Hops'][(randint(0,(len( hops['Aroma Hops'] )-1)))]
			if this_hop != 'None':
				this_qty = hops_qty[(randint(0,(len(hops_qty)-1)))]
			else:
				this_qty = ''
			print hop_schedule[i] + ': ' + this_qty + ' ' + this_hop
#	
make_recipe(ingredients)
specialty_grains(specialty_malt)
gen_hop_schedule(hops,hop_schedule)