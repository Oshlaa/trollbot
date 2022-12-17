import sys, os, yaml, random, coloredlogs, logging


#Define file and directory names
ConfigDirectory=os.path.join(os.getcwd(),'config')

ConfigFile=os.path.join(ConfigDirectory,"config.yml")

AdvancedConfigFile=os.path.join(ConfigDirectory,"advanced_config.yml")

VersionFile=os.path.join(ConfigDirectory,"version.yml")

SecretsFile=os.path.join(ConfigDirectory,"secrets.yml")

AccsFile=os.path.join(ConfigDirectory,"accs.yml")

RequirementsFile=os.path.join(os.getcwd(),"requirements.txt")

LogLevelFile=os.path.join(ConfigDirectory,"logging.yml")

if sys.platform=="linux":
    logging.debug('OS detected as Linux')
    StartScriptFile="start.sh"
elif sys.platform=="win32":
    logging.debug('OS detected as Windows')
    StartScriptFile="start.bat"
else:
    logging.critical('OS not recognized')

StartScriptFile=os.path.join(os.path.dirname(os.getcwd()),StartScriptFile)


#Set up logging:

def GetLogLevel():
    #If the YAML config file does not exist use the DEBUG logging level
    if os.path.exists(LogLevelFile)==False:
        logging.error(LogLevelFile+" does not exist")
        logginglevel=logging.DEBUG
    else:
        #Load YAML config file
        with open(LogLevelFile) as file:
            logginglevel = yaml.load(file, Loader=yaml.SafeLoader)['log-level']

        #Use INFO log level if logging level is set to "low"
        if str(logginglevel).lower()=="low":
            logginglevel=logging.INFO

        #Use DEBUG log level if logging level is set to "high"
        elif str(logginglevel).lower()=="high":
            logginglevel=logging.DEBUG
    
    return logginglevel


#Configure the logging module
coloredlogs.install(level=GetLogLevel(), fmt='[%(module)s] [%(funcName)s] [%(levelname)s]: %(message)s')


#Print some variables for easy reference
logging.debug('ConfigDirectory: '+ConfigDirectory)
logging.debug('ConfigFile: '+ConfigFile)
logging.debug('AdvancedConfigFile: '+AdvancedConfigFile)
logging.debug('VersionFile: '+VersionFile)
logging.debug('SecretsFile: '+SecretsFile)
logging.debug('AccsFile: '+AccsFile)
logging.debug('LogLevelFile: '+LogLevelFile)
logging.debug('RequirementsFile: '+RequirementsFile)
logging.debug('StartScriptFile: '+StartScriptFile)




#Gets the content out of a YAML file
def get_yaml(filename=str):
    logging.debug(f"Loading YAML data from file '{str(filename)}'")
    with open(str(filename)) as file:
        YMLFile = yaml.load(file, Loader=yaml.SafeLoader)
    return YMLFile




#guess what im too lazy to recode this because it works for now
def RandString(length=int,type=1):
    if int(type)==1:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    elif int(type)==2:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif int(type)==3:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$&*?"
    loop = 0
    final = ""
    while loop<int(length):
        char=chars[random.randint(0, len(chars)-1)]
        final=str(str(char)+str(final))
        loop = loop+1
    final=str(final)
    return final

#Makes text bold/multicolored
def SpecialText(Text=str,Bold=False,Color="White"):
    if Bold==True:
        Bold="1"
    else:
        Bold="0"
    if Color=="White":
        Color="37m"
    elif Color=="Red":
        Color="31m"
    elif Color=="Green":
        Color="32m"
    elif Color=="Blue":
        Color="34m"
    elif Color=="Yellow":
        Color="33m"
    else:
        logging.debug("Color invalid, using white")
        Color="37m"
    finalstring=f"\033[{Bold};{Color}{str(Text)}\033[0m"
    return finalstring

#Literally just writes stuff to a file and if it does not exist it will create it for you
def WriteToFile(Text,File=str,UseBytes=False):
    #Set open() mode
    if UseBytes==True:
        mode='wb'
    else:
        mode="w"

    #Create file
    if os.path.exists(File)==False:
        logging.debug(f"Creating file '{str(File)}'")
        file = open(File, "x")
        file.close()

    #Write to the file
    logging.debug(f"Writing to file '{str(File)}'")
    with open(str(File), mode) as File:
        File.write(Text)

#Checks if a string starts with another string
def StartsWith(text, startingtext):
    #Make sure its a string (yes, ik this is redundant)
    text, startingtext=str(text), str(startingtext)

    #Check if the first part of text = startingtext
    if text[0:len(startingtext)]==startingtext:
        return True
    else:
        return False