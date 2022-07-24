from time import sleep
import trollbot_config,trollbot_core,oshla_utils,sys,os,random
trollbot_config.Configure("trollbot_commands")
from oshla_utils import StartsWith
from start_cmd import PrintGreeting


PreviousCommand="NONE"

def DebugLog(log,Functions=["MAIN"]):
    oshla_utils.DebugLog(log,Module="trollbot_commands",Functions=Functions)

def Log(Log,Type="INFO"):
    if Type=="INFO":
        print("[INFO] "+str(Log))
    elif Type=="WARN":
        print(oshla_utils.SpecialText(Text="[WARN]",Color="Yellow")+" "+str(Log))
    elif Type=="ERROR":
        print(oshla_utils.SpecialText(Text="[ERROR]",Bold=True,Color="Red")+" "+str(Log))

def PrintHelp(topic="all"):
    DebugLog("PrintHelp function triggered",Functions=["PrintHelp"])
    topic=str(topic).lower()
    if topic=="all":
        print('''\033[1;37mai:\033[0m
   Description: Makes the specified account start talking to people using OpenAI's Davinci model. You can talk to the AI directly instead of via Discord by setting the first parameter to "direct"
   \033[0;32mUsage\033[0m: "ai {accounts file}:{account entry}|direct {channel to restrict the bot to (set to "*" to respond to all messages)}"
   Examples: 
   - ai accs.yml:account1 *
   - ai accounts.yml:myaccount 752025169048109067
   - ai direct
   \033[0;33mNOTE\033[0m: This command requires a valid OpenAI API key

\033[1;37mname:\033[0m
   Description: Generates a random name. Possible name types: "dsmp", "sus", "weird", "hypixel", "weird2", "random"
   \033[0;32mUsage\033[0m: "name {name type}"
   Example: "name sus"

\033[1;37mmessage:\033[0m
   Description: Generates a random message. Possible message types: "cringe", "sus", "twitter", "funny", "good", "ip", "dsmp", "poop", "game", "ytbot", "random"
   \033[0;32mUsage\033[0m: "message {message type}"
   Example: "message cringe"''')
    elif topic=="ai":
        print("""\033[1;37mai:\033[0m
   Description: Makes the specified account start talking to people using OpenAI's Davinci model. You can talk to the AI directly instead of via Discord by setting the first parameter to "direct"
   \033[0;32mUsage\033[0m: "ai {accounts file}:{account entry}|direct {channel to restrict the bot to (set to "*" to respond to all messages)}"
   Examples: 
   - ai accs.yml:account1 *
   - ai accounts.yml:myaccount 752025169048109067
   - ai direct
   \033[0;33mNOTE\033[0m: This command requires a valid OpenAI API key
   """)
    elif topic=="raid":
        print("""\033[1;37mraid:\033[0m
   Description: Sends odd messages in the specified channels using 3 different accounts
   \033[0;32mUsage\033[0m: "raid {channel ID} {accounts file}"
   Example: "raid 903089870619160582 accs.yml"
   \033[0;33mNOTE\033[0m: Requires at least 3 working accounts configured in the accounts file. Accounts are more likely to be locked by Discord when used with the raid command.""")
    elif topic=="name":
        print('''\033[1;37mname:\033[0m
   Description: Generates a random name. Possible name types: "dsmp", "sus", "weird", "hypixel", "weird2", "random"
   \033[0;32mUsage\033[0m: "name {name type}"
   Example: "name sus"''')
    elif topic=="message":
        print('''\033[1;37mmessage:\033[0m
   Description: Generates a random message. Possible message types: "cringe", "sus", "twitter", "funny", "good", "ip", "dsmp", "poop", "game", "ytbot", "random"
   \033[0;32mUsage\033[0m: "message {message type}"
   Example: "message cringe"''')
    elif topic=="check-config":
        print('''\033[1;37mcheck-config:\033[0m
   Description: Checks most config files for mistakes
   \033[0;32mUsage\033[0m: "check-config"
   Example: "check-config"''')
    elif topic=="profile":
        print('''\033[1;37mprofile:\033[0m
   Description: Sets an accounts profile picture. Possible profile types: "generic", "minecraft", "sus"
   \033[0;32mUsage\033[0m: "profile {accounts file}:{account entry} {profile type}"
   Example: "profile accs.yml:account1 minecraft"''')

    else:
        DebugLog("ValueError raised",Functions=["PrintHelp"])
        raise ValueError








def ExecuteCommand(command=str):
    #DebugLog("ExecuteCommand function triggered",Functions=["ExecuteCommand"])
    global PreviousCommand
    originalcommand=str(command)
    command=str(command).lower()
    if StartsWith(text=command,startingtext="none")==True:
        return
    if StartsWith(text=command,startingtext="exit")==True or StartsWith(text=command,startingtext="quit")==True:
        DebugLog("Exit/quit command triggered",Functions=["ExecuteCommand"])
        print("\n\033[1;31mExiting\033[0m\n")
        sys.exit()
    
    if command=="r" or StartsWith(command,"r "):
        if PreviousCommand!="NONE":
            print("\033[1;37m>\033[0m"+str(PreviousCommand))
        ExecuteCommand(PreviousCommand)
        return
    if StartsWith(text=command,startingtext="repeat")==True:
        try:
            interval=int(command.split(" ")[1])
        except:
            Log("Error parsing parameters",Type="ERROR")
            return
        repeatcommand=str(command.replace(f"repeat {str(interval)} ",""))
        try:
            while True:
                ExecuteCommand(repeatcommand)
                sleep(interval)
        except KeyboardInterrupt:
            print("\n")
            return
        except Exception:
            Log("Error while trying to repeat command",Type="ERROR")
            return

    PreviousCommand=command
    if StartsWith(text=command,startingtext="name")==True:
        DebugLog("Running name command",Functions=["ExecuteCommand"])
        if command=="name " or command=="name":
            print("'"+trollbot_core.GenerateName()+"'")
            return
        try:
            print("'"+trollbot_core.GenerateName(nametype=command.replace("name","").replace(" ",""))+"'")
        except ValueError:
            Log("Error while executing 'name' command: Incorrect name type provided. Use 'help name' for help",Type="ERROR")
        return
    elif StartsWith(text=command,startingtext="message")==True:
        DebugLog("Running message command",Functions=["ExecuteCommand"])
        if command=="message" or command=="message ":
            print("'"+trollbot_core.GenerateMessage()+"'")
            return
        try:
            print("'"+trollbot_core.GenerateMessage(messagetype=command.replace("message","").replace(" ",""))+"'")
        except ValueError:
            Log("Error while executing 'message' command: Incorrect message type provided. Use 'help message' for help",Type="ERROR")
        return
    elif StartsWith(text=command,startingtext="help")==True:
        DebugLog("Running help command",Functions=["ExecuteCommand"])
        if command.replace("help","").replace(" ","")=="":
            PrintHelp("all")
            return
        else:
            try:
                PrintHelp(command.replace("help","").replace(" ",""))
                return
            except ValueError:
                print(f"No help topic for '"+command.replace("help","").replace(" ","")+"'")
                return
    elif StartsWith(text=command,startingtext="ai")==True:
        DebugLog("Running ai command",Functions=["ExecuteCommand"])
        try:
            if command.split(" ")[1]=="direct":
                trollbot_core.FinalName=trollbot_core.GenerateName()
                DebugLog("Starting prompt...",Functions=["ExecuteCommand","ai"])
                try:
                    while True:
                        AIResponse=trollbot_core.OpenAIResponse(input("Say something to the AI: "),Sender="Human")
                        if AIResponse==None:
                            DebugLog("OpenAIResponse returned 'None' exiting",Functions=["ExecuteCommand","ai"])
                            return
                        else:
                            print(AIResponse)
                except Exception as Except:
                    Log("Error while running command 'ai'",Type="ERROR")
                    DebugLog(f"Exception raised:\n{str(Except)}",Functions=["ExecuteCommand","ai"])
                except KeyboardInterrupt:
                    print("\n")
                    return

                return
            DebugLog("Attempting to parse parameters...",Functions=["ExecuteCommand","ai"])
            AccountFile=command.split(" ")[1].split(":")[0]
            AccountName=command.split(" ")[1].split(":")[1]
            DiscordChannel=command.split(" ")[2]
        except:
            Log("Error parsing parameters",Type="ERROR")
            return
        
        try:
            DebugLog("Loading accounts file...",Functions=["ExecuteCommand","ai"])
            AccountsFile=oshla_utils.get_yaml(filename=AccountFile)
            DebugLog("Getting info from accounts file...",Functions=["ExecuteCommand","ai"])
            DiscordBotType=AccountsFile[AccountName][1]
            DiscordBotToken=AccountsFile[AccountName][0]
        except:
            Log("Error getting info from accounts file",Type="ERROR")
            return

        try:
            DebugLog("Importing trollbot_discord_ai",Functions=["ExecuteCommand","ai"])
            import trollbot_discord_ai
            DebugLog("Setting variables",Functions=["ExecuteCommand","ai"])
            trollbot_discord_ai.DiscordBotToken=DiscordBotToken
            trollbot_discord_ai.DiscordBotType=DiscordBotType
            trollbot_discord_ai.DiscordChannel=DiscordChannel
            DebugLog("Starting Discord bot...",Functions=["ExecuteCommand","ai"])
            trollbot_discord_ai.StartBot()
        except Exception as Except:
            DebugLog("Exception raised:\n"+str(Except),Functions=["ExecuteCommand","ai"])
            Log("Error while attempting to run module trollbot_discord_ai",Type="ERROR")
            return

    elif StartsWith(text=command,startingtext="profile")==True:
        DebugLog("Running 'profile' command...",Functions=["ExecuteCommand"])
        try:
            AccountFile=command.split(" ")[1].split(":")[0]
            AccountName=command.split(" ")[1].split(":")[1]
            AccountsFile=oshla_utils.get_yaml(filename=AccountFile)
            DiscordBotType=AccountsFile[AccountName][1]
            DiscordBotToken=AccountsFile[AccountName][0]

            if command.split(" ")[2]=="generic":
                directory="Avatars/Generic"
            elif command.split(" ")[2]=="minecraft":
                directory="Avatars/Minecraft"
            elif command.split(" ")[2]=="sus":
                directory="Avatars/sus"
            else:
                Log("Invalid profile type. Use 'help profile' for a list of profile types",Type="ERROR")
                return
        except Exception as Except:
            DebugLog("Exception raised:\n"+str(Except),Functions=["ExecuteCommand","profile"])
            Log("Error parsing parameters",Type="ERROR")
            return

        try:
            Avatars=[]
            for path in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, path)):
                    Avatars.append(path)
        except Exception as Except:
            Log("Error while trying to find avatar files",Type="ERROR")
            DebugLog("Exception raised:\n"+str(Except),Functions=["ExecuteCommand","profile"])
            return

        ProfilePictureFile=directory+"/"+str(Avatars[random.randint(0,len(Avatars)-1)])

        try:
            DebugLog("Importing trollbot_discord_profile",Functions=["ExecuteCommand","profile"])
            import trollbot_discord_profile
            DebugLog("Setting variables",Functions=["ExecuteCommand","profile"])
            trollbot_discord_profile.DiscordBotToken=DiscordBotToken
            trollbot_discord_profile.DiscordBotType=DiscordBotType
            trollbot_discord_profile.ProfilePictureFile=ProfilePictureFile
            DebugLog("Starting...",Functions=["ExecuteCommand","profile"])
            trollbot_discord_profile.StartBot()
        except Exception as Except:
            DebugLog("Exception raised:\n"+str(Except),Functions=["ExecuteCommand","profile"])
            Log("Error running module 'trollbot_discord_profile'",Type="ERROR")
            return


    elif StartsWith(text=command,startingtext="clear")==True:
        DebugLog("Clearing...",Functions=["ExecuteCommand","clear"])
        PreviousCommand="NONE"
        print("\033c")
        DebugLog("Printing greeting...",Functions=["ExecuteCommand","clear"])
        PrintGreeting()
        return
    elif command=="" or StartsWith(text=command,startingtext=" ")==True:
        return
    else:
        Log("Unknown command '"+originalcommand.split(" ")[0]+"'",Type="WARN")
        return

def CommandLine():
    DebugLog("Starting Trollbot command line...",Functions=["CommandLine"])
    try:
        while True:
                UserInput=input("\033[1;37m>\033[0m")
                try:
                    ExecuteCommand(UserInput)
                except KeyboardInterrupt:
                    DebugLog("KeyboardInterrupt exception raised",Functions=["CommandLine"])
                    print("\n")
    except KeyboardInterrupt:
        DebugLog("KeyboardInterrupt exception raised",Functions=["CommandLine"])
        print("\n\n\033[1;31mExiting\033[0m\n")
        sys.exit()