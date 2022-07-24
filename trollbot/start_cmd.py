import trollbot_config, oshla_utils, trollbot_commands
trollbot_config.Configure("start_cmd")




def Config(entry):
    #oshla_utils.DebugLog(f"Running trollbot_config.GetConfig('{str(entry)}')",Module="start_cmd",Functions=[])
    return trollbot_config.GetConfig(entry)



def PrintGreeting():
    #print("\033c")
    print("\n")
    #print("------------------------------------------------------------------------------")
    print("████████   █████       ████     ██      ██      █████       ████    ████████")
    print("   ██      ██   ██   ██    ██   ██      ██      ██   ██   ██    ██     ██")
    print("   ██      █████     ██    ██   ██      ██      █████     ██    ██     ██")
    print("   ██      ██   ██   ██    ██   ██      ██      ██   ██   ██    ██     ██")
    print("   ██      ██   ██     ████     █████   █████   █████       ████       ██")
    #print("------------------------------------------------------------------------------")


    print("\n")
    print(oshla_utils.SpecialText(Text=f"TrollBot v{Config('CurrentVersionHuman')} by oshla",Bold=True,Color="White"))
    if Config("FilterProfanity")==True:
        ProfanityReadable=oshla_utils.SpecialText(Text="ON",Bold=True,Color="Green")
    else:
        ProfanityReadable=oshla_utils.SpecialText(Text="OFF",Bold=True,Color="Red")
    print(f"\nProfanity filtering is {ProfanityReadable}")
    print("\n\n")
    print('Type "help" for help.\n')


def Start():
    PrintGreeting()
    trollbot_commands.CommandLine()


if __name__=="__main__":
    Start()