import pymongo
import unicodecsv

if __name__ == "__main__":
	client = pymongo.MongoClient()

	with open("data/verb_database.csv", 'rb') as csvfile:
		reader = unicodecsv.DictReader(csvfile, )
		for row in reader:
			verb_dict = {}
			for key, value in row.items():
				if key == '\ufeff"infinitive"':
					key = 'infinitive'
				verb_dict[key] = value
			print(verb_dict)
			client["verbs"]["conjugation"].insert(verb_dict)
