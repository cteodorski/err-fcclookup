from errbot import BotPlugin, botcmd


class fcc(BotPlugin):
    @botcmd  # flags a command
    def fccsearch(self, msg, args):
        return 'It *works* !'  # This string format is markdown.
