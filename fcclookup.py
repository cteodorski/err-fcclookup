from errbot import BotPlugin, botcmd
import requests

class fcc(BotPlugin):
    """
    This is a very basic plugin to search the FCC ULS database
    """

    @botcmd  # flags a command
    def fccsearch(self, msg, args):  # a command callable with !tryme


        """
        Use !fccsearch <callsign> to search the FCC ULS database
        """

        return 'It *works* !'  # This string format is markdown.
