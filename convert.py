import json
inputfile = input("JSON Filename: ")
print(inputfile)

with open(inputfile) as filedata:
	train = json.load(filedata)

DATA = []
for data in train:
	ent = [tuple(entity[:3]) for entity in data['entities']]
	DATA.append((data['text'],{'entities':ent}))

with open('{}'.format(inputfile.replace('json','txt')),'w') as write:
	write.write(str(DATA))

print("Converted and stored as {}".format(inputfile.replace('json','txt')))
