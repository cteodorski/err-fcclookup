from errbot import BotPlugin, botcmd
import requests
import pprint

class fcc(BotPlugin):
    """
    This is a very basic plugin to search the FCC ULS database
    """

    @botcmd  # flags a command
    def fccsearch(self, msg, args):  # a command callable with !tryme


        """
        Use !fccsearch <callsign> to search the FCC ULS database
        """
        api = "http://data.fcc.gov/api/license-view/basicSearch/getLicenses?searchValue="
        url = api + args + "&format=json"
        print(url)

        results = requests.get(url)
        records = results.json()
        name = records['Licenses']['License']['licName']
        print(name)


        return 'It *works* !'  # This string format is markdown.
