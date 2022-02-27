# Importing files
import speech_recognition as sr
import simpleaudio as sa
import random
from pynput.keyboard import Key, Controller
from pycaw.pycaw import AudioUtilities

# Indication that it started listening
print("Started.")

# Instantiating recognizer as r.
r = sr.Recognizer()

while True:
    
    with sr.Microphone() as source:

        # Ask user to speak and get what he says in Audio
        audio = r.listen(source, phrase_time_limit=2)      

        # Try to recognize what he said
        try:
            # Use google's recognizer
            text = r.recognize_google(audio)
    
        # If there was an error tell user nothing was recognized.
        except:
            text = 0
            continue 
        
        # List of Hotspot words
        words = ["Rizwan", "redwan", "Bhagwan"]

        # Null check
        if text != 0: 
            # if any word in list is in sentence 
            if any(word in text for word in words):
                # Print attendance found
                print("Attendance found")
                
                # Get all current processes
                sessions = AudioUtilities.GetAllSessions()

                # Loop through sessions
                for session in sessions: 
                    # IF current session is Zoom
                    if session.Process and session.Process.name() == "Zoom.exe":
                        # Get session volume and mute it
                        volume = session.SimpleAudioVolume
                        volume.SetMute(1, None)

                # Setup the keyboard controller
                keyboard = Controller()

                # Press the Space key
                keyboard.press(Key.space)

                # Get Audio File, make it into an object, play it, and wait for it to end.
                filename = f'present/Present{random.randrange(1,5)}.wav'   
                wave_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wave_obj.play()
                play_obj.wait_done()
                
                #Release the space key
                keyboard.release(Key.space)
                
                # Loop through sessions again
                for session in sessions: 
                    # IF current session is Zoom
                    if session.Process and session.Process.name() == "Zoom.exe":
                        # Get session volume and unmute it
                        volume = session.SimpleAudioVolume
                        volume.SetMute(0, None)
                # break and exit program
                break