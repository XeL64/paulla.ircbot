#! /usr/bin/env python
# -*- coding: utf-8 -*

"""
Simple script to test to irc module.
"""


import irc.bot

class Botanick(irc.bot.SingleServerIRCBot):
    def __init__(self, channel="#paulla", nickname="botanik", server="irc.freenode.net", port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

    def on_welcome(self, c, e):
        c.join(self.channel)
        c.privmsg(self.channel, u"solevis mon maître m'a abandonné")


def main():
    """Main function."""
    bot = Botanick()
    bot.start()
    #import pdb; pdb.set_trace()

if __name__ == "__main__":
    main()
