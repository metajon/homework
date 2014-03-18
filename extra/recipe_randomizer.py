from random import randint
#
yeast = ['English Ale Yeast','Americal Ale Yeast','Belgian ALe Yeast']
base_malt = ['Maris Otter','Vienna Malt','2-Row']
specialty_malt =['Oats']
bittering_hops = ['Cascade']
flavoring_aroma_hops = ['Falconer\'s Flight']
hop_schedule = ['60 minutes','30 minutes','15 minutes','Flameout']
extract_qty = ['5#','5.5#','6#']
#
# print yeast[(randint(0,(len(yeast)-1)))]
#
all_ingredients = [yeast,base_malt,specialty_malt,bittering_hops,flavoring_aroma_hops,extract_qty]
#
for i in range(len(all_ingredients)):
	print all_ingredients[i][(randint(0,(len(all_ingredients[i])-1)))]
#
def gen_recipe(ingredient_list):
	return ingredient_list[(randint(0,(len(ingredient_list)-1)))]
#
def gen_hop_schedule(bittering_hops,flavoring_aroma_hops,hop_schedule):
	pass