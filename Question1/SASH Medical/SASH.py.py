from experta import *

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("diseases.txt")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n")
	diseases.close()
	for disease in diseases_list:
		disease_s_file = open("Disease symptoms/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		diseases_symptoms.append(s_list)
		symptom_map[str(s_list)] = disease
		disease_s_file.close()
		disease_s_file = open("Disease descriptions/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_desc_map[disease] = disease_s_data
		disease_s_file.close()
		disease_s_file = open("Disease treatments/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_treatment_map[disease] = disease_s_data
		disease_s_file.close()
	

def identify_disease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptom_map[str(symptom_list)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("The most probable disease that you have is %s\n" %(id_disease))
		print("Some information about the disease is given as follows: \n")
		print(disease_details+"\n")
		print("The modus operandi for curing is: \n")
		print(treatments+"\n")

# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
#headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever,sunken_eyes) 11 symtomes:
class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("This is an expert knowledge system named SASH designed to give you diagnoses of your symptoms.")
		print("I will ask after certain symptoms and you will have to reply with severety from 0 to 10")
		print("Following are your symptoms: ")
		print("")
		yield Fact(action="find_disease")


	@Rule(Fact(action='find_disease'), NOT(Fact(headache=W())),salience = 1)
	def symptom_0(self):
		while True:
			take = input("headache: ")
			if(not take.isnumeric()):
				print("type a number")
				continue
			if(int(take)<0 or int(take)>10):
				print("type a number between 0 and 10")
				continue
			break
		if(int(take)>=5):
			take = "yes"
		else:
			take="no"
		self.declare(Fact(headache=take))

	@Rule(Fact(action='find_disease'), NOT(Fact(back_pain=W())),salience = 1)
	def symptom_1(self):
		while True:
			take = input("Back pain: ")
			if(not take.isnumeric()):
				print("type a number")
				continue
			if(int(take)<0 or int(take)>10):
				print("type a number between 0 and 10")
				continue
			break
		if(int(take)>=5):
			take = "yes"
		else:
			take="no"
		self.declare(Fact(back_pain=take))

	@Rule(Fact(action='find_disease'), NOT(Fact(chest_pain=W())),salience = 1)
	def symptom_2(self):
		while True:
			take = input("Chest Pain: ")
			if(not take.isnumeric()):
				print("type a number")
				continue
			if(int(take)<0 or int(take)>10):
				print("type a number between 0 and 10")
				continue
			break
		if(int(take)>=5):
			take = "yes"
		else:
			take="no"
		self.declare(Fact(chest_pain=take))

	@Rule(Fact(action='find_disease'), NOT(Fact(cough=W())),salience = 1)
	def symptom_3(self):
		while True:
			take = input("Cough: ")
			if(not take.isnumeric()):
				print("type a number")
				continue
			if(int(take)<0 or int(take)>10):
				print("type a number between 0 and 10")
				continue
			break
		if(int(take)>=5):
			take = "yes"
		else:
			take="no"
		self.declare(Fact(cough=take))

	@Rule(Fact(action='find_disease'), NOT(Fact(fainting=W())),salience = 1)
	def symptom_4(self):
		while True:
			take = input("Fainting: ")
			if(not take.isnumeric()):
				print("type a number")
				continue
			if(int(take)<0 or int(take)>10):
				print("type a number between 0 and 10")
				continue
			break
		if(int(take)>=5):
			take = "yes"
		else:
			take="no"
		self.declare(Fact(fainting=take))

	@Rule(Fact(action='find_disease'), NOT(Fact(fatigue=W())),salience = 1)
	def symptom_5(self):
		while True:
			take = input("Fatigue: ")
			if(not take.isnumeric()):
				print("type a number")
				continue
			if(int(take)<0 or int(take)>10):
				print("type a number between 0 and 10")
				continue
			break
		if(int(take)>=5):
			take = "yes"
		else:
			take="no"
		self.declare(Fact(fatigue=take))
	 
	@Rule(Fact(action='find_disease'), NOT(Fact(sunken_eyes=W())),salience = 1)
	def symptom_6(self):
		while True:
			take = input("Sunken Eyes: ")
			if(not take.isnumeric()):
				print("type a number")
				continue
			if(int(take)<0 or int(take)>10):
				print("type a number between 0 and 10")
				continue
			break
		if(int(take)>=5):
			take = "yes"
		else:
			take="no"
		self.declare(Fact(sunken_eyes=take))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(low_body_temp=W())),salience = 1)
	def symptom_7(self):
		while True:
			take = input("Low Body Temperature: ")
			if(not take.isnumeric()):
				print("type a number")
				continue
			if(int(take)<0 or int(take)>10):
				print("type a number between 0 and 10")
				continue
			break
		if(int(take)>=5):
			take = "yes"
		else:
			take="no"
		self.declare(Fact(low_body_temp=take))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(restlessness=W())),salience = 1)
	def symptom_8(self):
		while True:
			take = input("Restlessness: ")
			if(not take.isnumeric()):
				print("type a number")
				continue
			if(int(take)<0 or int(take)>10):
				print("type a number between 0 and 10")
				continue
			break
		if(int(take)>=5):
			take = "yes"
		else:
			take="no"
		self.declare(Fact(restlessness=take))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(sore_throat=W())),salience = 1)
	def symptom_9(self):
		while True:
			take = input("Sore throat: ")
			if(not take.isnumeric()):
				print("type a number")
				continue
			if(int(take)<0 or int(take)>10):
				print("type a number between 0 and 10")
				continue
			break
		if(int(take)>=5):
			take = "yes"
		else:
			take="no"
		self.declare(Fact(sore_throat=take))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(fever=W())),salience = 1)
	def symptom_10(self):
		while True:
			take = input("Fever: ")
			if(not take.isnumeric()):
				print("type a number")
				continue
			if(int(take)<0 or int(take)>10):
				print("type a number between 0 and 10")
				continue
			break
		if(int(take)>=5):
			take = "yes"
		else:
			take="no"
		self.declare(Fact(fever=take))

	@Rule(Fact(action='find_disease'), NOT(Fact(nausea=W())),salience = 1)
	def symptom_11(self):
		while True:
			take = input("Nausea: ")
			if(not take.isnumeric()):
				print("type a number")
				continue
			if(int(take)<0 or int(take)>10):
				print("type a number between 0 and 10")
				continue
			break
		if(int(take)>=5):
			take = "yes"
		else:
			take="no"
		self.declare(Fact(nausea=take))

	@Rule(Fact(action='find_disease'), NOT(Fact(blurred_vision=W())),salience = 1)
	def symptom_12(self):
		while True:
			take = input("Blurred Vision: ")
			if(not take.isnumeric()):
				print("type a number")
				continue
			if(int(take)<0 or int(take)>10):
				print("type a number between 0 and 10")
				continue
			break
		if(int(take)>=5):
			take = "yes"
		else:
			take="no"
		self.declare(Fact(blurred_vision=take))

	@Rule(Fact(action='find_disease'), NOT(Fact(loss_of_taste=W())),salience = 1)
	def symptom_13(self):
		while True:
			take = input("Loss of sense of taste: ")
			if(not take.isnumeric()):
				print("type a number")
				continue
			if(int(take)<0 or int(take)>10):
				print("type a number between 0 and 10")
				continue
			break
		if(int(take)>=5):
			take = "yes"
		else:
			take="no"
		self.declare(Fact(loss_of_taste=take))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"),Fact(loss_of_taste="no"))
	def disease_0(self):
		self.declare(Fact(disease="Jaundice"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"),Fact(loss_of_taste="no"))
	def disease_1(self):
		self.declare(Fact(disease="Alzheimers"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"),Fact(loss_of_taste="no"))
	def disease_2(self):
		self.declare(Fact(disease="Diarrhea"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"),Fact(loss_of_taste="no"))
	def disease_2(self):
		self.declare(Fact(disease="Arthritis"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"),Fact(loss_of_taste="no"))
	def disease_3(self):
		self.declare(Fact(disease="Tuberculosis"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"),Fact(loss_of_taste="no"))
	def disease_4(self):
		self.declare(Fact(disease="Asthma"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"),Fact(loss_of_taste="no"))
	def disease_5(self):
		self.declare(Fact(disease="Sinusitis"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="yes"),Fact(nausea="yes"),Fact(blurred_vision="no"),Fact(loss_of_taste="no"))
	def disease_5(self):
		self.declare(Fact(disease="Malaria"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"),Fact(loss_of_taste="no"))
	def disease_6(self):
		self.declare(Fact(disease="Epilepsy"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"),Fact(loss_of_taste="yes"))
	def disease_6(self):
		self.declare(Fact(disease="COVID-19"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"),Fact(loss_of_taste="no"))
	def disease_7(self):
		self.declare(Fact(disease="Heart Disease"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"),Fact(loss_of_taste="no"))
	def disease_8(self):
		self.declare(Fact(disease="Diabetes"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"),Fact(loss_of_taste="no"))
	def disease_9(self):
		self.declare(Fact(disease="Glaucoma"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"),Fact(loss_of_taste="no"))
	def disease_10(self):
		self.declare(Fact(disease="Hyperthyroidism"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"),Fact(loss_of_taste="no"))
	def disease_11(self):
		self.declare(Fact(disease="Heat Stroke"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"),Fact(loss_of_taste="no"))
	def disease_12(self):
		self.declare(Fact(disease="Hypothermia"))

	@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
	def disease(self, disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		if(disease=="COVID-19"):
			print("YOU HAVE CORONA!! Rest and wear masks and drink water. Stay safe!!! Our team members are with you. In spirit.")
		print("The most probable disease that you have is %s\n" %(id_disease))
		print("Some information about the disease is given as follows: \n")
		print(disease_details+"\n")
		print("The modus operandi for curing is: \n")
		print(treatments+"\n")

	@Rule(Fact(action='find_disease'),
		  Fact(headache=MATCH.headache),
		  Fact(back_pain=MATCH.back_pain),
		  Fact(chest_pain=MATCH.chest_pain),
		  Fact(cough=MATCH.cough),
		  Fact(fainting=MATCH.fainting),
		  Fact(sore_throat=MATCH.sore_throat),
		  Fact(fatigue=MATCH.fatigue),
		  Fact(low_body_temp=MATCH.low_body_temp),
		  Fact(restlessness=MATCH.restlessness),
		  Fact(fever=MATCH.fever),
		  Fact(sunken_eyes=MATCH.sunken_eyes),
		  Fact(nausea=MATCH.nausea),
		  Fact(blurred_vision=MATCH.blurred_vision),
		  Fact(loss_of_taste=MATCH.loss_of_taste),NOT(Fact(disease=MATCH.disease)),salience = -999)

	def not_matched(self,headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision, loss_of_taste):
		print("\nDid not find any disease that matches your exact symptoms")
		print("So no need to worry, but please get tested for the most probable disease.")
		lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision, loss_of_taste]
		max_count = 0
		max_disease = "Tiredness"
		for key,val in symptom_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		if(max_disease == "Tiredness"):
			print("You are fine. At worst you are a bit tired. Calm down and stop crying. Sleep and play video games. Do not drink boiling water. All your worries are worthless and you should feel bad. Cross the road while looking both sides at once. Do you want to check for new symptoms?")
		else:
			if_not_matched(max_disease)


if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print("Would you like to diagnose some other symptoms?")
		if input() == "no":
			exit()
		#print(engine.facts)