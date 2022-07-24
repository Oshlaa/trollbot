import trollbot_core, trollbot_config, oshla_utils, random, discord, sys, asyncio, hashlib, os, base64, requests, contextlib, wave
from discord.ext import commands
from time import sleep
trollbot_config.Configure("trollbot_discord_ai")


client=discord.Client()


DiscordBotType="bot"
DiscordBotToken="none"
DiscordChannel="*"
FinalName="Bob"
global Speaking
Speaking=False

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
    global FinalName
    Log(f'Discord TrollBot started (Username: "{str(bot.user)}" ID: "{str(bot.user.id)}")',Type="INFO")
    oshla_utils.DebugLog("Discord bot started",Module='trollbot_discord_ai',Functions=["on_ready"])
    oshla_utils.DebugLog("Getting FinalName from bot name...",Module='trollbot_discord_ai',Functions=["on_ready"])
    FinalName=str(bot.user)[0:len(str(bot.user))-5]
    trollbot_core.FinalName=str(bot.user)[0:len(str(bot.user))-5]
    oshla_utils.DebugLog("FinalName: "+FinalName,Module='trollbot_discord_ai',Functions=["on_ready"])


@bot.event
async def on_message(message: discord.Message):
    ctx = await bot.get_context(message)


    WriteMessage=True
    finalcontent=str(message.content).replace(f"<@{bot.user.id}>",f"@{FinalName}")

    if str(bot.user.id) in str(message.author.id):
        return
    else:
        oshla_utils.DebugLog("Message recieved: "+str(message.content),Module='trollbot_discord_ai',Functions=['on_message'])

    if str(message.channel.id)!=DiscordChannel and DiscordChannel!="*":
        oshla_utils.DebugLog("Tried to respond to a message in the wrong channel",Module='trollbot_discord_ai',Functions=['on_message'])
        return

    if len(str(message.content))<3:
        oshla_utils.DebugLog("Tried to respond to a message below 3 characters",Module='trollbot_discord_ai',Functions=['on_message'])
        return

    if str(message.author.id) in Config("IgnoredUsers"):
        oshla_utils.DebugLog("Tried to respond to ignored user",Module='trollbot_discord_ai',Functions=['on_message'])
        return


    global Speaking
    if f"<@{bot.user.id}>" in message.content and Speaking==False:
        Speaking=True
        try:
            VoiceChannel=message.author.voice.channel
        except AttributeError:
            Log("User not in voice channel",Type="WARN")
            Speaking=False
            return

        speech=trollbot_core.OpenAIResponse(finalcontent,Sender=str(message.author.name))
        if str(message.author.name)+":" in speech:
            Log("Possible AI malfunction",Type="WARN")
            speech=trollbot_core.OpenAIResponse(finalcontent,Sender=str(message.author.name))
            if str(message.author.name)+":" in speech:
                Log("Potential AI malfunction occured a second time, cancelling message response",Type="ERROR")
                return


        Log("Requesting TTS for '"+str(speech)+"'",Type="INFO")
        payload = {
            "voicemodel_uuid": "1ecb0520-e82d-4646-8340-eae83d97c2dd",
            "pace": 0.5,
            "speech": speech
        }






        response = requests.post("https://api.uberduck.ai/speak-synchronous", json=payload, headers={"Accept": "application/json","uberduck-id": "anonymous","Content-Type": "application/json","Authorization": Config("UberduckAuthHeader")})
        Log("Request completed",Type="INFO")
        oshla_utils.DebugLog("Writing TTS to file 'voice.wav'",Module='trollbot_discord_ai',Functions=['on_message'])
        oshla_utils.WriteToFile(Text=response.content,File="voice.wav",UseBytes=True)

        try:
            oshla_utils.DebugLog("Getting length of .wav file...",Module='trollbot_discord_ai',Functions=['on_message'])
            with contextlib.closing(wave.open("voice.wav",'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
        except wave.Error as Except:
            oshla_utils.DebugLog(str(Except),Module='trollbot_discord_ai',Functions=['on_message'])
            Log("wave.Error raised",Type="ERROR")
            Speaking=False
            return

        duration=duration+1

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("voice.wav"))

        oshla_utils.DebugLog("Connecting to voice channel",Module='trollbot_discord_ai',Functions=['on_message'])
        await VoiceChannel.connect()

        oshla_utils.DebugLog("Playing voice",Module='trollbot_discord_ai',Functions=['on_message'])
        ctx.voice_client.play(source)
        sleep(duration)

        oshla_utils.DebugLog("Disconnecting from voice channel",Module='trollbot_discord_ai',Functions=['on_message'])
        await ctx.voice_client.disconnect()
        Speaking=False
        return


    if Config("DiscordBotPrefix").lower()=="none":
        pass
    else:
        if message.content.startswith(Config("DiscordBotPrefix")):
            finalcontent=finalcontent.replace(Config("DiscordBotPrefix"),"")
            pass
        else:
            oshla_utils.DebugLog("Message does not start with prefix",Module='trollbot_discord_ai',Functions=['on_message'])
            return
    
    if len(str(message.content))>Config("LengthLimit"):
        if Config("LengthyAction").lower()=="ignore":
            oshla_utils.DebugLog("Ignoring message due to length limit",Module='trollbot_discord_ai',Functions=['on_message'])
            return
        elif Config("LengthyAction").lower()=="clip":
            finalcontent=str(message.content)[:Config("LengthLimit")]
            oshla_utils.DebugLog("Clipping message due to length limit",Module='trollbot_discord_ai',Functions=['on_message'])
            Log("Clipping recieved message due to length limit...",Type="WARN")
        elif Config("LengthyAction").lower()=="weird":
            TrollbotMessage=trollbot_core.GenerateMessage()
            if Config("DiscordMessageWait")==True:
                await message.channel.trigger_typing()
                await asyncio.sleep(len(TrollbotMessage)/3)
            oshla_utils.DebugLog("Sending weird message due to length limit",Module='trollbot_discord_ai',Functions=['on_message'])
            Log("Sending non-AI generated message due to length limit...",Type="WARN")
            Log(f'Sending message "{str(TrollbotMessage)}"',Type="INFO")
            try:
                await message.channel.send(TrollbotMessage)
            except Exception as Except:
                oshla_utils.DebugLog("Exception raised while trying to send message\n"+str(Except),Module='trollbot_discord_ai',Functions=['on_message'])
                Log("Exception raised while trying to send message",Type="ERROR")
                return
            return

    if random.random() < Config("DiscordResponseChance") or isinstance(message.channel, discord.channel.DMChannel) or isinstance(message.channel, discord.channel.GroupChannel):
        oshla_utils.DebugLog("Sending message...",Module='trollbot_discord_ai',Functions=['on_message'])
        Log("Responding to a message...",Type="INFO")
        if Config("DiscordMessageWait")==True:
            try:
                await message.channel.trigger_typing()
            except Exception as Except:
                Log("Exception raised while trying to trigger typing",Type="ERROR")
                oshla_utils.DebugLog("Exception raised while trying to trigger typing\n"+str(Except),Module="trollbot_discord_ai",Functions=['on_message'])
                return

        messagehash = hashlib.sha256(str(message.content).lower().encode()).hexdigest()
        if Config("UseOldMessages")==True:
            Log("Using previously sent message...",Type="INFO")
            try:
                resp=str(Config("PastMessages")[messagehash])
                resp=base64.b64decode(resp)
                resp=resp.decode('utf-8')
                resp=str(resp)
            except KeyError:
                    resp=trollbot_core.OpenAIResponse(finalcontent,Sender=str(message.author.name))
                    if Config("BadSpelling")==True:
                        resp=trollbot_core.OpenAIBadSpelling(resp)
            respencoded=str(base64.b64encode(str(resp).encode('utf-8'))).replace("'","")[1:]
        else:
            resp=trollbot_core.OpenAIResponse(finalcontent,Sender=str(message.author.name))
            if Config("BadSpelling")==True:
               resp=trollbot_core.OpenAIBadSpelling(resp)
            respencoded=str(base64.b64encode(str(resp).encode('utf-8'))).replace("'","")[1:]

        try:
            blank=Config("PastMessages")[messagehash]
            WriteMessage=False
        except KeyError:
            pass

        resp=resp.replace(FinalName,f"<@{bot.user.id}>")

        if WriteMessage==True:
            os.system(f'echo "{str(messagehash)}: {str(respencoded)}">>past_messages.yml')

        if Config("DiscordMessageWait")==True:
            oshla_utils.DebugLog(f"Waiting for {str(len(resp)/10)} seconds...",Module='trollbot_discord_ai',Functions=['on_message'])
            await asyncio.sleep(len(resp)/10)
        oshla_utils.DebugLog("Sending message '"+resp+"'",Module='trollbot_discord_ai',Functions=['on_message'])
        try:
            Log(f'Sending message "{str(resp)}"',Type="INFO")
            await message.channel.send(resp,reference=message)
        except discord.errors.HTTPException:
            resp=trollbot_core.GenerateMessage()
            Log("HTTPException error raised",Type="WARN")
            Log(f'Trying to send non-AI generated message "{str(resp)}"',Type="INFO")
            try:
                await message.channel.send(resp,reference=message)
            except Exception as Except:
                oshla_utils.DebugLog("Exception raised while trying to send message\n"+str(Except),Module='trollbot_discord_ai',Functions=['on_message'])
                Log("Exception raised while trying to send message",Type="ERROR")
                return
        except Exception as Except:
            oshla_utils.DebugLog("Exception raised while trying to send message\n"+str(Except),Module='trollbot_discord_ai',Functions=['on_message'])
            Log("Exception raised while trying to send message",Type="ERROR")
            return
        oshla_utils.DebugLog("Sent message",Module='trollbot_discord_ai',Functions=['on_message'])



def StartBot():
    oshla_utils.DebugLog("DiscordBotType: "+DiscordBotType,Module='trollbot_discord_ai',Functions=['StartBot'])
    oshla_utils.DebugLog("DiscordChannel: "+DiscordChannel,Module='trollbot_discord_ai',Functions=['StartBot'])
    oshla_utils.DebugLog("FinalName: "+FinalName,Module='trollbot_discord_ai',Functions=['StartBot'])

    if WarnBotType==True:
        Log("Using a user account as a bot is against the Discord TOS!",Type="WARN")
    Log("Starting Discord bot...",Type="INFO")
    oshla_utils.DebugLog("Running Discord bot...",Module='trollbot_discord_ai',Functions=['StartBot'])
    try:
        bot.run(str(DiscordBotToken).replace("'","").replace('"',''))
    except discord.errors.LoginFailure:
        Log("Failed to log in! Are you sure you used the correct token?",Type="ERROR")
        return