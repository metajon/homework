from random import randint
#
yeast = ['English Ale Yeast','American Ale Yeast','Belgian ALe Yeast','California Ale Yeast']
base_malt = ['Maris Otter','Vienna Malt','2-Row']
specialty_malt =['Oats','Flaked Barley','Un-malted wheat']
hops = {'Bittering Hops' : ['Cascade','Chinook','East Kent Golding','Willamette','Mt. Hood','Challenger'], 'Flavoring Hops' : ['Simcoe','East Kent Golding','Amarillo','None'], 'Aroma Hops' : ['Falconer\'s Flight','East Kent Golding','Amarillo','None']}
hop_schedule = ['60 minutes','30 minutes','15 minutes','Flameout']
extract_qty = ['5#','5.5#','6#']
#
# print yeast[(randint(0,(len(yeast)-1)))]
#
#all_ingredients = [yeast,base_malt,specialty_malt,bittering_hops,flavoring_aroma_hops,extract_qty]
ingredients = [yeast,base_malt,specialty_malt,extract_qty]
#
#for i in range(len(all_ingredients)):
#	print all_ingredients[i][(randint(0,(len(all_ingredients[i])-1)))]
#
def make_recipe(ingredients):
	for i in range(len(ingredients)):
		print ingredients[i][(randint(0,(len(ingredients[i])-1)))]
#
def gen_hop_schedule(hops,hop_schedule):
	for i in range(len(hop_schedule)):
		if hop_schedule[i] == '60 minutes':
			print hop_schedule[i] + ': ' + hops['Bittering Hops'][(randint(0,(len( hops['Bittering Hops'] )-1)))]
		elif hop_schedule[i] == 'Flameout':
			print hop_schedule[i] + ': ' + hops['Aroma Hops'][(randint(0,(len( hops['Aroma Hops'] )-1)))]
		else:
			print hop_schedule[i] + ': ' + hops['Flavoring Hops'][(randint(0,(len( hops['Flavoring Hops'] )-1)))]
#	
make_recipe(ingredients)
gen_hop_schedule(hops,hop_schedule)