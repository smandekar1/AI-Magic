import speech_recognition as sr   #use google speech recognition program 
from gtts import gTTS             #use google text-to-speech program 
from pygame import mixer          #use the mixer to play computer's speech


# GOOGLE SPEECH RECOGNITION CODE TO RECOGNIZE YOUR SPEECH! :)


while True:                       # continuously listen to user for  input

    r = sr.Recognizer()           #using the Recognizer program from speech recognition tool to recognize your speech
    with sr.Microphone()as source: #turning the microphone as a listening source
        r.adjust_for_ambient_noise(source)      # this code cancels any background noise
        print('Talk now: ')        # Asks the user to start talking
        audio = r.listen(source)   #Recognizer listens to the microphone's source and stores that content in audio

    try:
        message = (r.recognize_google(audio)) #takes the audio content to recognizes the user's speech and stores in message
                                           
        print(message)                        #outputs and prints the user message, such as 'Hello', etc
    
    
#GOOGLE TEXT TO SPEECH CODE RESPOND BACK TO YOU!  :)

#condition to respond to "hello"
        if 'hello' in message:                         # if google speech recognition hears hello from you
            speech = ('Hello, I love the ninja turtles')  # this is the text response to 'hello'
            tts = gTTS(text=speech, lang='en')         # convert above written text into speech 
            tts.save('C:\\audio\\hello.mp3')# save speech in mp3 (change to your file location)
            mixer.init()                               # start mixer to play mp3
            mixer.music.load('C:\\audio\\hello.mp3') # load file
            mixer.music.play() # play file

#condition to respond to "Bob"
        if 'Bob' in message:                         # if google speech recognition hears hello from you
            speech = ('Hey Ravi')  # this is the text response to 'hello'
            tts = gTTS(text=speech, lang='en')         # convert above written text into speech 
            tts.save('C:\\audio\\hello2.mp3')# save speech in mp3 (change to your file location)
            mixer.init()                               # start mixer to play mp3
            mixer.music.load('C:\\audio\\hello2.mp3') # load file
            mixer.music.play() # play file

#condition to respond to "Sam"
        if 'Sam' in message:                         # if google speech recognition hears hello from you
            speech = ('Hey Sam, how is it going?')  # this is the text response to 'hello'
            tts = gTTS(text=speech, lang='en')         # convert above written text into speech 
            tts.save('C:\\audio\\hello3.mp3')# save speech in mp3 (change to your file location)
            mixer.init()                               # start mixer to play mp3
            mixer.music.load('C:\\audio\\hello3.mp3') # load file
            mixer.music.play() # play file


#condition to respond to "good morning"
        if 'good morning' in message:
            speech = ('Good Morning, its going to be a great day!')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\audio\\hello1.mp3')
            mixer.init()
            mixer.music.load('C:\\audio\\hello1.mp3')
            mixer.music.play()

    except Exception as e:                             # throw an exception or error
        print("Could not understand")                  # when user speech is meaningless











