import trollbot_config,oshla_utils, discord, asyncio
from discord.ext import commands
from time import sleep
trollbot_config.Configure("trollbot_discord_profile")
client=discord.Client()
DiscordBotType="bot"
DiscordBotToken="none"
DiscordChannel="*"
FinalName="Bob"
ProfilePictureFile="none"


def Log(Log,Type="INFO"):
    if Type=="INFO":
        print("[INFO] "+str(Log))
    elif Type=="WARN":
        print(oshla_utils.SpecialText(Text="[WARN]",Color="Yellow")+" "+str(Log))
    elif Type=="ERROR":
        print(oshla_utils.SpecialText(Text="[ERROR]",Bold=True,Color="Red")+" "+str(Log))

def Config(entry):
    #oshla_utils.DebugLog(f"Running trollbot_config.GetConfig('{str(entry)}')",Module="trollbot_discord_ai")
    return trollbot_config.GetConfig(entry)



if DiscordBotType.lower()=="userbot":
    bot = commands.Bot(command_prefix=oshla_utils.RandString(10), self_bot=True)
    HumanBotType=oshla_utils.SpecialText(Text="User",Bold=True,Color="Red")
    WarnBotType=True
elif DiscordBotType.lower()=="bot":
    bot = commands.Bot(command_prefix=oshla_utils.RandString(10), self_bot=False)
    HumanBotType=oshla_utils.SpecialText(Text="Bot",Bold=True,Color="Green")
    WarnBotType=False


@bot.event
async def on_ready():
    global ProfilePictureFile
    Log(f'Logged in (Username: "{str(bot.user)}" ID: "{str(bot.user.id)}")',Type="INFO")
    Log("Changing profile picture...",Type="INFO")
    try:
        ProfilePicture = open(ProfilePictureFile, 'rb')
        Profile_picture = ProfilePicture.read()
        ProfilePicture.close()
        await bot.user.edit(avatar=Profile_picture)
        Log("Profile picture set!","INFO")
    except Exception as e:
        oshla_utils.DebugLog(str(e),Module='trollbot_discord_profile',Functions=['on_ready'])
        Log("Could not set the profile picture",Type="ERROR")    



def StartBot():
    oshla_utils.DebugLog("DiscordBotType: "+DiscordBotType,Module='trollbot_discord_profile',Functions=['StartBot'])

    if WarnBotType==True:
        Log("Using a user account as a bot is against the Discord TOS!",Type="WARN")
    Log("Logging in...",Type="INFO")
    oshla_utils.DebugLog("Running Discord bot...",Module='trollbot_discord_profile',Functions=['StartBot'])
    try:
        bot.run(str(DiscordBotToken).replace("'","").replace('"',''))
    except Exception as e:
        oshla_utils.DebugLog(e,Module='trollbot_discord_profile',Functions=['StartBot'])
        Log("Failed to log in! Are you sure you used the correct token?",Type="ERROR")
        return