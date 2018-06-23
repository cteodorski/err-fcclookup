from errbot import BotPlugin, botcmd
import requests
import pprint
import json

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
        json_data = json.loads(results.json())
        pprint.pprint(json_data)
        return 'It *works* !'