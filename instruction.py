import os
import subprocess

class Commander:
    def __init__(self):
        self.confirm= ["Yes", "Affirmative", "Sure", "Do it", "Confirm"]
        self.cancel=["Don't","Wait","Cancel","No"]
        
    def discover(self, text):

        text=text.lower()
        
        if "what" in text and "name" in text:

            if "your" in text:
                self.respond("Hey, I am Pie , Nice to meet you!!")
            if "my" in text:
                self.respond("I just realized that I don't know your name. I am sorry. We are still friends right?")

        elif "start" in text or "lauch" in text or "open" in text: 
                       
            app=text.split(" ",1)[-1]
            self.respond("Opening" + app)
            try:
                subprocess.call("start "+app, shell= True)
            except:
                self.respond("Sorry I could not find anything to open")

        else:
            self.respond("Sorry, I need to look for this answer. Come back later.")
            
    def respond(self, response):
        subprocess.call("mshta vbscript:Execute(\"CreateObject(\"\"SAPI.SpVoice\"\").Speak(\"\""+response+"\"\")(window.close)\")", shell= True)