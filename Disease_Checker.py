print("Hello")
print("Wanna check if you got a disease? , Well enter your symptoms and lets find out!")
symptom_1=input("Enter THE MOST MAJOR SYMPTOM that you got. Like really Major , Don't Worry no need to be embarassed :)")
symptom_2=input("Now do the same thing but the 2nd Most Major Symptom , again do NOT hold back we need to know")

if (symptom_1 == "runny nose" or symptom_1 == "block nose") and symptom_2 == "sneezing":
    print(" According to my calculations, you got a case of the **Common Cold**.")
    
elif (symptom_1 == "fever" or symptom_1 == "high fever") and symptom_2 == "body pain":
    print(" Looks like you might have the **Flu (Influenza)**. This might be one of the less accurate guess , due to the huge similarity of influenza symptoms with other diseases , so get checked!!")

elif (symptom_1 == "dry cough" or symptom_1 == "cough") and symptom_2== "loss of smell":
    print(" Hmm... these symptoms match with **COVID-19**.aka everyone's nightmare in 2020 , see a doctor , and quarantine your self while your at it")

elif (symptom_1 == "fever") and symptom_2== "chills":
    print("You might have **Malaria**   see a doctor ASAP!")

elif (symptom_1 == "high fever") and symptom_2== "joint pain":
    print("Uhhh... you could be dealing with **Dengue**.Mosquitoes amyryt ?? ")

elif (symptom_1 == "fever") and (symptom_2== "abdominal pain" or symptom_2=="abdomen pain"):
    print("This sounds like **Typhoid**. I feel you bro... (not really)")

elif (symptom_1 == "vomiting") and symptom_2 =="diarrhea":
    print("Classic case of **Food Poisoning**. BRO I CAN RELATE , i mean my creator can relate. i am a piece of code . ")

elif (symptom_1 == "shortness of breath") and symptom_2== "wheezing":
    print("These are signs of **Asthma**.I hope you got one of those inhalers. Sometimes I am grateful to be an AI chatbot. Oops im getting too sentient, gotta go simple. YOU SAW NOTHING PATIENT ")

elif (symptom_1 == "cough with mucus") and symptom_2 == "chest pain":
    print(" You might have **Pneumonia**.This can be serious visit a hospital NOOWWWW")

elif (symptom_1 == "frequent urination") and (symptom_2 == "excessive thirst" or ("thirsty" in symptom_2)):
    print("Sounds like early **Diabetes** signs. I think you ate one to much donuts man... or woman")
else:
    print(" Sorry! I couldn't match those symptoms with a known condition")
    print("This is just a basic program — please consult a real doctor!")
print("The program is coming to an end , Warning , This is a program which guesstimates your disease , do consult a doctor for dire cases! , Bye Patient! , i know you will miss me and i will miss you 2!!")



