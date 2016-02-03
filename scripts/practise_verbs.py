import pymongo
import random
import time

third_person_singular = ("el", "ella", "usted")
third_person_plural = ("los", "las", "ustedes")
def rand_3ps():
	return third_person_singular[random.randint(0,2)]

def rand_3pp():
	return third_person_plural[random.randint(0,2)]


if __name__ == "__main__":
	client = pymongo.MongoClient()
	conjugations = client["verbs"]["conjugation"]
	conjugation_count = conjugations.count()
	print(conjugation_count)
	random.seed(int(time.time()))
	while(True):
		audit_record = {}
		conjugation_id = random.randint(0, conjugation_count-1	)
		audit_record["conjugation_id"] = conjugation_id
		conjugation = conjugations.find().skip(conjugation_id).limit(1)[0]
		print("+---------------------------------------------------------------------------------------------+")
		k = input("| Do you know the meaning of the verb {} (y/n) : ".format(conjugation["infinitive"]))
		audit_record["verb_known"] = (k != 'n')
		print("|                                                                                             |")
		print("|    {:89}|".format(conjugation.get("infinitive_english", "Error, english meaning unknown.")))
		print("|                                                                                             |")
		k = input("| Were you correct (y/n):                                                                     |")
		audit_record["verb_known_correct"] = (k != 'n')
		k = input("| Do you know the '{}' conjugation of this verb?".format(conjugation["tense"]))
		audit_record["conjugation_known"] = (k != 'n')
		print("|                                                                                             |")
		print("|   yo {:30} nos {}".format(conjugation.get("form_1s"), conjugation.get("form_2s")))
		print("|                                                                                             |")
		print("|   tu {}".format(conjugation.get("form_1p")))
		print("|                                                                                             |")
		print("|   {} {:30} {} {}".format(rand_3ps(), conjugation.get("form_1s"), rand_3pp(), conjugation.get("form_2s")))
		print("|                                                                                             |")
		k = input("| Were you correct (y/n):                                                                     |")
		audit_record["conjugation_known_correct"] = (k != 'n')
		client["user_results"]["verbs"].insert(audit_record)
