#! /usr/bin/env python3
# -*- coding: utf-8 -*

"""
Simple script to test to irc module.
"""


import irc.bot

class Botanik(irc.bot.SingleServerIRCBot):
    def __init__(self, channel="#paulla", nickname="botanik", server="irc.freenode.net", port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel
        self.yakafokon = ['falloir','faut','il faille','faudra','fallait','il fallût','fallu']

    def on_welcome(self, c, e):
        """ Le bot dit bonjour """
        c.join(self.channel)
        c.privmsg(self.channel, "cyp c'est pour quand le prochain sprint ?")
        c.privmsg(self.channel, "cyp j'ai vraiment l'impression de mouler !")
        lost_masters = ['solevis', 'Llew', 'Mika64']
        for master in lost_masters:
            c.privmsg(self.channel, "Mon maître %s m'a abandonné" % master)
        
    def on_pubmsg(self, c, e):
        """ Le bot écoute ce qui se raconte """
        message = e.arguments()[0]
        for terme in self.yakafokon:
            if terme in message:
                c.privmsg(self.channel, "¡¡¡ YAKAFOKON detected !!!")
                break
     

def main():
    """Main function."""
    bot = Botanik()
    bot.start()
    #import pdb; pdb.set_trace()

if __name__ == "__main__":
    main()
