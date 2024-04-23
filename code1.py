import speech_recognition as sr
from pyfirmata import Arduino, SERVO, util
from time import sleep

'''r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

port = 
pin=10
board= Arduino(port)

board.digital[pin].mode = SERVO

def rotate(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.015)

with mic as source:
    r.adjust_for_ambient_noise(source)
    while True:
        audio= r.listen(source)
        try:
            if r.recognize_google(audio) == 'switch on':
                print("switch is on")
                for i in range(0,45):
                    rotate(pin,i)

            else:
                print("Hey, How can i help you ?")
        
        except:
            print("no audio")'''

# Initialize the microphone
mic = sr.Microphone(device_index=1)

# Use a context manager to properly handle the microphone resource
with mic as source:
    try:
        # Adjust for ambient noise before capturing the audio
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source)
        
        # Now capture the audio
        audio = r.listen(source)

        # Perform speech recognition
        text = r.recognize_google(audio)
        print("You said:", text)

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))