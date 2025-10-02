from InquirerPy import inquirer
import receiverclient
import senderclient
import server


mode = inquirer.select(message="Which mode would you like to run in?", choices=["server", "client"]).execute()

if mode == "server":
    server.run()
elif mode == "client":
    clienttype = inquirer.select(message="Which client would you like to run?", choices=["receiver", "sender"]).execute()
    if clienttype == "receiver":
        receiverclient.run()
    elif clienttype == "sender":
        senderclient.run()