from random import randint

yeast = ['English Ale Yeast','Americal Ale Yeast','Belgian ALe Yeast']
base_malt = ['Maris Otter','Vienna Malt','2-Row']
specialty_malt =['Oats']
bittering_hops = []
flavoring_aroma_hops = []
extract_qty = ['5#','5.5#','6#']

print yeast[(randint(0,(len(yeast)-1)))]
