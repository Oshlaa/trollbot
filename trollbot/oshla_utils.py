import yaml, random
ExcludeModules=[]

Debug=False
def DebugEnable(ShowTime=False,Exclude=['none'],Module="MAIN"):
    global Debug
    global DebugLogShowTime
    global ExcludeModules
    """
    Makes the `DebugLog()` function print to terminal.
    """
    #print(f"[DEBUG] [{str(Module)}] Debugging started")

    if "oshla_utils" not in Exclude:
        print("[DEBUG] [oshla_utils] [DebugEnable] Importing 'datetime'")
    
    global datetime
    from datetime import datetime

    if "oshla_utils" not in Exclude:
        if ShowTime==True:
            print('[DEBUG '+str(datetime.now())+"] [oshla_utils] [DebugEnable] Imported 'datetime'")
        else:
            print("[DEBUG] [oshla_utils] [DebugEnable] Imported 'datetime'")
    Debug=True
    DebugLogShowTime=ShowTime
    ExcludeModules=Exclude

def DebugLog(log,Module="MAIN",Functions=["MAIN"]):
    """
    Logs things to terminal.
    """
    if Module in ExcludeModules:
        return

    if Debug==True:
        functions=""
        for Function in Functions:
            functions=functions+f" [{str(Function)}]"
        if DebugLogShowTime==True:
            print('[DEBUG '+str(datetime.now())+f'] [{str(Module)}]{str(functions)} {str(log)}')
        else:
            print(f'[DEBUG] [{str(Module)}]{str(functions)} {str(log)}')

def get_yaml(filename=str):
    #DebugLog("get_yaml function triggered",Module="oshla_utils")
    #DebugLog(f"Loading file '{str(filename)}'",Module="oshla_utils",Functions=["get_yaml"])
    """
    Loads a YAML file
    """
    #DebugLog("Loading file...",Module="oshla_utils")
    with open(str(filename)) as file:
        YMLFile = yaml.load(file, Loader=yaml.SafeLoader)
    #DebugLog("File loaded",Module="oshla_utils")
    return YMLFile

def RandString(length=int,type=1):
    """
    Generates a random string.

    Types:
    1: Numbers and letters
    2: Only letters
    3: Numbers, letters, and some special characters
    """
    DebugLog("RandString function triggered",Module="oshla_utils")
    if int(type)==1:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        DebugLog("Type 1 RandString selected",Module="oshla_utils",Functions=["RandString"])
    elif int(type)==2:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        DebugLog("Type 2 RandString selected",Module="oshla_utils",Functions=["RandString"])
    elif int(type)==3:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$&*?"
        DebugLog("Type 3 RandString selected",Module="oshla_utils",Functions=["RandString"])
    loop = 0
    final = ""
    DebugLog("Generating string...",Module="oshla_utils",Functions=["RandString"])
    while loop<int(length):
        char=chars[random.randint(0, len(chars)-1)]
        final=str(str(char)+str(final))
        loop = loop+1
    final=str(final)
    return final

def SpecialText(Text=str,Bold=False,Color="White"):
    #DebugLog("SpecialText function triggered",Module="oshla_utils")
    if Bold==True:
        #DebugLog("Bold=True",Module="oshla_utils")
        Bold="1"
    else:
        #DebugLog("Bold=False",Module="oshla_utils")
        Bold="0"
    if Color=="White":
        #DebugLog("Color=White",Module="oshla_utils")
        Color="37m"
    elif Color=="Red":
        #DebugLog("Color=Red",Module="oshla_utils")
        Color="31m"
    elif Color=="Green":
        #DebugLog("Color=Green",Module="oshla_utils")
        Color="32m"
    elif Color=="Blue":
        #DebugLog("Color=Blue",Module="oshla_utils")
        Color="34m"
    elif Color=="Yellow":
        #DebugLog("Color=Yellow",Module="oshla_utils")
        Color="33m"
    else:
        DebugLog("Color invalid, using White",Module="oshla_utils",Functions=['SpecialText'])
        Color="37m"
    final=f"\033[{Bold};{Color}{str(Text)}\033[0m"
    return final

def WriteToFile(Text,File=str,UseBytes=False):
    DebugLog("WriteToFile function triggered",Module="oshla_utils")
    if UseBytes==True:
        mode='wb'
    else:
        mode="w"
    with open(str(File), mode) as File:
        File.write(Text)

def StartsWith(text, startingtext):
    #DebugLog("StartsWith function triggered",Module="oshla_utils")
    text, startingtext=str(text), str(startingtext)
    if text[0:len(startingtext)]==startingtext:
        return True
    else:
        return False