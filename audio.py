import pyaudio
import wave
import speech_recognition as sr
import subprocess

def Say(text):
    text = "You said " + text
    subprocess.call("mshta vbscript:Execute(\"CreateObject(\"\"SAPI.SpVoice\"\").Speak(\"\""+text+"\"\")(window.close)\")", shell= True)


def PlaySound(filename):
    chunksize=1024
    #opening the wave file
    wf=wave.open(filename)
    
    pa=pyaudio.PyAudio()

    #used to stream the audio
    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),#Returns sample width in bytes and
        channels = wf.getnchannels(), #Returns number of audio channels
        rate = wf.getframerate(), #Returns number of audio frames.
        output = True
    )

    #reading the first chunk
    data_stream = wf.readframes(chunksize) 

    #reading till the last chunk
    while data_stream:
        stream.write(data_stream)
        data_stream= wf.readframes(chunksize)


    stream.close()

    pa.terminate()



r = sr.Recognizer()

def InitSpeech():
    print("Listening....")
    PlaySound("./sharp.wav")

    with sr.Microphone() as source: # use the default microphone as the audio source
        print("Say something")
        audio = r.listen(source) # listen for the first phrase and extract it into audio data


    command = ""

    try:
        command = r.recognize_google(audio) # recognize speech using Google Speech Recognition
        print("Your command:")
        print(command)

        Say(command)
    except:
        print("Sorry, I didn't get it. Would you mind repeating it?")

    
    

    PlaySound("./sharp.wav")

InitSpeech()


