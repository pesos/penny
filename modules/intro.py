import re

def intro(phenny,input):
    if input == ".intro":
        phenny.say("Everyone! Please introduce yourself in one line (Name, Department, Year")
        return

    else:
        matchObj = re.match( r'.intro (.*)', input, re.M|re.I)
        if matchObj:
            phenny.say(matchObj.group(1)+ ": Please introduce yourself in one line (Name, Department, Year)")
            return
        else:
            phenny.reply("Sorry, retry!")
            return

intro.commands = ['intro']
intro.priority = 'medium'	
