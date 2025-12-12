import datetime
import time
a = input("ENTER YOUR NAME: ")
b = datetime.datetime.now().hour
if 5 <= b <= 11:
    print("HEY GOOD MORNING", a)
elif 11 <= b <= 17:
    print("HEY GOOD AFTERNOON",a)
elif 17 <= b <= 20:
    print("HEY GOOD GIVENING",a)
else:
    print("HEY GOODNIGHT",a)
 
print("===> HEY, WELCOME : I AM YOUR COSMOS <===")
print("YOU CAN ASK ME SOME BASIC QUESTIONS, TYPE 'BYE' TO EXIT")

response = {
    "hey" : "hello, i am cosmos. you are fine?",
    "fine" : "that's great. How can I help you.",
    "who are you" : "I am cosmos. tell me something about you.",
    "how are you" : "I am fine. Hope you are also fine.",
    "motivate me" : "EVERY SINGLE STEP MAKES YOU GREAT ! KEEP GOING.",
    "happy" : "good to kown this, keep happy all the time.",
    "bye" : " ",
    "tell me something intersting" : "Australia is wider than the moon, and the Eiffel Tower can be up to 15 cm taller in the summer due to thermal expansion. It is impossible to hum while holding your nose, and the shortest war in history, between England and Zanzibar, lasted only 38 minutes. "
    

}

def responseofjarvis(userquestions):
    userquestions = userquestions.lower()
    for eachkey in response:
        if eachkey in userquestions:
            return response[eachkey]
    return " I AM NOT ABLE TO TELL, THAT BECAUSE I AM STILL IN LEARNING PHASE."

while True:
    userinput = input("ASK SOMETHING TO ME : ")
    reply = responseofjarvis(userinput)
    print("COSMOS :", reply)
    if "bye" in userinput.lower():
        print("THANKYOU",a)
        break
        

