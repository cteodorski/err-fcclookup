from errbot import BotPlugin, botcmd


class fcc(BotPlugin):
    """
    This is a very basic plugin to search the FCC license database
    !fcc SearchTerm 
    """

    @botcmd  # flags a command
    def search(self, msg, args):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """
        return 'It *works* !'  # This string format is markdown.
