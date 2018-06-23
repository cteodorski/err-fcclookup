from errbot import BotPlugin, botcmd


class fcc(BotPlugin):

    @botcmd  # flags a command
    def fccsearch(self, msg, args):
        print("Holy Shit")
        return 'It *works* !'
