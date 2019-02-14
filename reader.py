from wikidata.client import Client
import matplotlib.pyplot as plt
import numpy as np
import json
import pickle

def load():
	client = Client()
	instance_id = {}	
	instance_count = {}
	subclass_id =  {}
	subclass_count = {}
	with open('data/data.json', 'r') as f:
		data = json.load(f)
		for ent in data:
			ent_type = ent['type']
			ent_id = ent['id']
			ent_labels = ent['labels']
			ent_descriptions = ent['descriptions']
			ent_aliases = ent['aliases']
			ent_claims = ent['claims']
			ent_sitelinks = ent['sitelinks']

			ent_instance_of = []
			if 'P31' in ent['claims'].keys():
				for item in ent['claims']['P31']:
					id = item['mainsnak']['datavalue']['value']['id']
					if id in instance_id.keys():
						instance_id[id] += 1
					else:
						instance_id[id] = 1

			ent_subclass_of = []
			if 'P279' in ent['claims'].keys():
				for item in ent['claims']['P279']:
					id = item['mainsnak']['datavalue']['value']['id']
					if id in subclass_id.keys():
						subclass_id[id] += 1
					else:
						subclass_id[id] = 1

		for key in instance_id.keys():
			entity = client.get(key, load = 'True')
			instance_count[str(entity.label)] = instance_id[key]

		for key in subclass_id.keys():
			entity = client.get(key, load = 'True')
			subclass_count[str(entity.label)] = subclass_id[key]

	return instance_count, subclass_count

		# print(sorted(instance_id.items(), key=lambda d: d[1], reverse = True))
		# print(sorted(subclass_id.items(), key=lambda d: d[1], reverse = True))

def save_obj(obj, name):
	with open('save/'+ name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
	with open('save/' + name + '.pkl', 'rb') as f:
		return pickle.load(f)

def plot(count):
	entity = []
	frequency = []
	count = sorted(count.items(), key=lambda d: d[1], reverse = True)[:20]
	for i in range(20):
		entity.append(count[i][0])
		frequency.append(count[i][1])
	y_pos = np.arange(len(count))
	 
	plt.barh(y_pos, frequency, align='center', alpha=0.5)
	plt.yticks(y_pos, entity, fontsize = 5)
	plt.xlabel('Frequency in first 50,000 entities')
	plt.title('Top 20 frequent entities in in first 50,000 entities')
	plt.show()


if __name__ == '__main__':
	instance_count, subclass_count = load()
	save_obj(instance_count, 'instance')
	save_obj(subclass_count, 'subclass')
	instance_count = load_obj('instance')
	subclass_count = load_obj('subclass')
	plot(instance_count)
	plot(subclass_count)
	