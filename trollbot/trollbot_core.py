import trollbot_config
trollbot_config.Configure("trollbot_core")
from oshla_utils import DebugLog
import oshla_utils

FinalName=None

def Config(entry):
    #DebugLog(f"Running trollbot_config.GetConfig('{str(entry)}')",Module="trollbot_core")
    return trollbot_config.GetConfig(entry)


DebugLog("Importing libraries random, time, sys, openai",Module="trollbot_core")
import random, time, sys, openai
DebugLog("Imported libraries",Module="trollbot_core")



def Log(Log,Type="INFO"):
    if Type=="INFO":
        print("[INFO] "+str(Log))
    elif Type=="WARN":
        print(oshla_utils.SpecialText(Text="[WARN]",Color="Yellow")+" "+str(Log))
    elif Type=="ERROR":
        print(oshla_utils.SpecialText(Text="[ERROR]",Bold=True,Color="Red")+" "+str(Log))



def matrix(duration=2): #Completely un-needed thing
    EndTime=int(time.time()+duration)
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()~?+-=/}{_`"
    while time.time()<EndTime:
        final=""
        charloop=0
        while charloop<20:
            char=str(chars[random.randint(0,len(chars)-1)])
            final=f'{final}   {char}'
            charloop=charloop+1
        print(str(final))
        time.sleep(0.02)

def hax(duration=1): #Completely un-needed thing V2!
    EndTime=int(time.time()+duration)
    sleeptime=[0.5]
    with open('trollbot_core.py') as f:
        lines = f.readlines()
        while time.time()<EndTime:
            print(lines[random.randint(0,700)])
            time.sleep(int(sleeptime[random.randint(0,len(sleeptime)-1)]))


def GenerateName(nametype="random"):
    if str(type(nametype))!="<class 'str'>":
        DebugLog("'nametype' is not a string",Module="trollbot_core",Functions=['GenerateName'])
        raise TypeError
    #DebugLog(f"Generating a name with type '{nametype}'",Module="trollbot_core",Functions=['GenerateName'])
    def dsmp():
        DebugLog("Generating a type 'dsmp' name",Module="trollbot_core",Functions=['GenerateName','dsmp'])
        x=['xx','Xx','XX','Oo']
        x2=['xx','xX','XX','oO']
        character=['Dream','TommyInnit','GeorgeNotFound','Sapnap','BadBoyHalo','Fundy','Wilbur','Skeppy','Technoblade','Ranboo']
        like=['ILike','ILIKE','ILove','ILY','ily','Ily','ILOVE']
        cool=['IsCool','ISCOOL','Iscool','IsAwesome','IsAWESOME','ISAWESOME','IsGreat','isCOOL']
        xsel=random.randint(0,len(x)-1)
        x=x[xsel]
        x2=x2[xsel]
        character=character[random.randint(0,len(character)-1)]
        like=like[random.randint(0,len(like)-1)]
        cool=cool[random.randint(0,len(cool)-1)]

        if random.randint(1,2)==1:
            part1=character
            part2=cool
        else:
            part1=like
            part2=character
        if random.randint(1,5)==3:
            subfinal=f'{part1}_{part2}'
        else:
            subfinal=part1+part2
        if "ily" not in subfinal.lower():
            if random.randint(1,3)==2:
                subfinal=f'{x}{subfinal}{x2}'
        if "ILY" in subfinal:
            subfinal=subfinal.upper()
        if random.randint(1,20)==11:
            subfinal==subfinal.replace('o','0').replace('O','0').replace('s','5').replace('S','5').replace('e','3').replace('E','3')
        #DebugLog("Finished generating name",Module="trollbot_core",Functions=['GenerateName','dsmp'])
        return str(subfinal)
    def weird():
        DebugLog("Generating a type 'weird' name",Module="trollbot_core",Functions=['GenerateName','weird'])
        wP1=['Fart','Poop','You','Hand','Arm','Mouse','Leg','Foot','Eye','Finger','Cat','Dog','Kitten','Puppy','Chair','Lamp','Bed','Anime','Human','Joe','Goop']
        wP2=['Licker','Eater','Maker','Shaker','Hater','Creator','Lover','Liker','User','Abuser']
        x=['xx','Xx','XX','Oo']
        x2=['xx','xX','XX','oO']
        xsel=random.randint(0,len(x)-1)
        x=x[xsel]
        x2=x2[xsel]
        wP1=wP1[random.randint(0,len(wP1)-1)]
        wP2=wP2[random.randint(0,len(wP2)-1)]

        if random.randint(1,5)==3:
            subfinal=f'{wP1}_{wP2}'
        else:
            subfinal=wP1+wP2
        if random.randint(1,5)==4:
            subfinal=subfinal.upper()
        elif random.randint(1,5)==4:
            subfinal=subfinal.lower()
        if random.randint(1,3)==2:
            subfinal=f'{x}{subfinal}{x2}'
        if random.randint(1,20)==11:
            subfinal==subfinal.replace('o','0').replace('O','0').replace('s','5').replace('S','5').replace('e','3').replace('E','3')
        #DebugLog("Finished generating name",Module="trollbot_core",Functions=['GenerateName','weird'])
        return subfinal
    def sus():
        DebugLog("Generating a type 'sus' name",Module="trollbot_core",Functions=['GenerateName','sus'])
        sP1=['AmongUs','Amongus','Amogus','Gus','Mogus','Emogus']
        sP2=['IsSussy','IsSus','IsWeird','IsCool','IsAwesome','IsGreat','IsBad']
        x=['xx','Xx','XX','Oo']
        x2=['xx','xX','XX','oO']
        xsel=random.randint(0,len(x)-1)
        x=x[xsel]
        x2=x2[xsel]
        sP1=sP1[random.randint(0,len(sP1)-1)]
        sP2=sP2[random.randint(0,len(sP2)-1)]
        if random.randint(1,5)==3:
            subfinal=f'{sP1}_{sP2}'
        else:
            subfinal=sP1+sP2
        if random.randint(1,5)==4:
            subfinal=subfinal.upper()
        elif random.randint(1,5)==4:
            subfinal=subfinal.lower()
        if random.randint(1,3)==2:
            subfinal=f'{x}{subfinal}{x2}'
        if random.randint(1,20)==11:
            subfinal==subfinal.replace('o','0').replace('O','0').replace('s','5').replace('S','5').replace('e','3').replace('E','3')
        #DebugLog("Finished generating name",Module="trollbot_core",Functions=['GenerateName','sus'])
        return subfinal
    def hypixel():
        DebugLog("Generating a type 'hypixel' name",Module="trollbot_core",Functions=['GenerateName','hypixel'])
        P1=['0H','0h','Oh','x','Ohhhhh','0hhhhh','ily','Ily','ILY','Best','Poggers','Pog']
        P2=['Duck','Ducks','Cat','Cats','Kat','Katz','Kats','Ducc','Duccs','Capybara','Capybaras','Puppy','Kitten','Kittens','Strong','Cool','Great','Sweaty','Insane','Amazing','Glue','Puff','Puffy','Poof','Fox','Foxxy','Doggy','Dog','Kitty','Apple','Pear','Orange','Velocity','Reach','Aura']
        x=['xx','Xx','XX','Oo']
        x2=['xx','xX','XX','oO']
        xsel=random.randint(0,len(x)-1)
        x=x[xsel]
        x2=x2[xsel]
        P1=P1[random.randint(0,len(P1)-1)]
        P2=P2[random.randint(0,len(P2)-1)]
        if random.randint(1,5)==3:
            subfinal=f'{P1}_{P2}'
        else:
            subfinal=P1+P2
        if random.randint(1,5)==4:
            subfinal=subfinal.upper()
        elif random.randint(1,5)==4:
            subfinal=subfinal.lower()

        if random.randint(1,20)==11:
            subfinal==subfinal.replace('o','0').replace('O','0').replace('s','5').replace('S','5').replace('e','3').replace('E','3')
        #if "oh" or "0h" or "x" or "ily" in subfinal.lower():
        #    print()
        #else:
        #    if random.randint(1,3)==2:
        #       subfinal=f'{x}{subfinal}{x2}'
        if random.randint(1,20)==10:
            if random.randint(1,5)==1:
                ms="MS"
            else:
                ms="ms"
            subfinal=str(random.randint(0,999))+ms
        #DebugLog("Finished generating name",Module="trollbot_core",Functions=['GenerateName','hypixel'])
        return subfinal
    def weird2():
        DebugLog("Generating a type 'weird2' name",Module="trollbot_core",Functions=['GenerateName','weird2'])
        P1=['dex','slu','sla','pluh','ploo','bu','bo','blo','bla','zlu','plu','pla','pa','za','boo']
        P2=['muh','uh','guh','gen','n','gan','gon','slun','lun','blun','dun','gloo','ploo','pluh','oo','a']
        P1=P1[random.randint(0,len(P1)-1)]
        P2=P2[random.randint(0,len(P2)-1)]
        subfinal=P1+P2
        if random.randint(1,5)==4:
            subfinal=subfinal.upper()
        elif random.randint(1,5)==4:
            subfinal=subfinal.lower()
        if random.randint(1,20)==11:
            subfinal==subfinal.replace('o','0').replace('O','0').replace('s','5').replace('S','5').replace('e','3').replace('E','3')
        #DebugLog("Finished generating name",Module="trollbot_core",Functions=['GenerateName','weird2'])
        return subfinal
    
    nametype=nametype.lower()
    if nametype=="dsmp":
        return str(dsmp())
    elif nametype=="sus":
        return str(sus())
    elif nametype=="weird":
        return str(weird())
    elif nametype=="hypixel":
        return str(hypixel())
    elif nametype=="weird2":
        return str(weird2())
    elif nametype=="random":
        #DebugLog("nametype='random', choosing random name type",Module="trollbot_core",Functions=['GenerateName'])
        rand1=random.randint(1,5)
        if rand1==1:
            final=dsmp()
        elif rand1==2:
            final=sus()
        elif rand1==3:
            final=weird()
        elif rand1==4:
            final=hypixel()
        elif rand1==5:
            final=weird2()
    else:
        DebugLog("'"+str(nametype)+"' is not a valid nametype",Module="trollbot_core",Functions=['GenerateName'])
        raise ValueError
    return str(final)

def GenerateMessage(messagetype="random"):
    #DebugLog("Generating random message",Module="trollbot_core",Functions=['GenerateMessage'])
    if str(type(messagetype))!="<class 'str'>":
        DebugLog("'messagetype' is not a string",Module="trollbot_core",Functions=['GenerateMessage'])
        raise TypeError

    def cringe():
        DebugLog("Generating a type 'cringe' message",Module="trollbot_core",Functions=['GenerateMessage','cringe'])
        cringe = ['mogus','cring','cringey','cringe']
        thats = ["that's","thats","that is"]
        bro = ["broski","bro","man","brother"]
        emoji = [":pensive:",""]
        cringe=cringe[random.randint(0,3)]
        thats=thats[random.randint(0,2)]
        bro=bro[random.randint(0,3)]
        emoji=emoji[random.randint(0,1)]
        final = str(thats+" "+cringe)
        pos=random.randint(1,4)
        if pos==1:
            final = str(emoji+" "+bro+" "+final)
        elif pos==2:
            final = str(emoji+" "+final+" "+bro)
        elif pos==3:
            final = str(bro+" "+final+" "+emoji)
        elif pos==4:
            final = str(final+" "+bro+" "+emoji)
        if final[0]==" ":
            final=final[1:]
        #DebugLog("Generated message",Module="trollbot_core",Functions=['GenerateMessage','cringe'])
        return final


    def sus():
        DebugLog("Generating a type 'sus' message",Module="trollbot_core",Functions=['GenerateMessage','sus'])
        sus = ['mogus','sussy','sus','amogus','weird','wacky']
        thats = ["that's","thats","that is"]
        bro = ["broski","bro","man","brother"]
        emoji = [":flushed:",":face_with_raised_eyebrow:",":hot_face:",""]
        sus=sus[random.randint(0,3)]
        thats=thats[random.randint(0,2)]
        bro=bro[random.randint(0,3)]
        emoji=emoji[random.randint(0,3)]
        final = str(thats+" "+sus)
        if random.randint(1,10)==7:
            sus=sus.upper()
        pos=random.randint(1,4)
        if pos==1:
            final = str(emoji+" "+bro+" "+final)
        elif pos==2:
            final = str(emoji+" "+final+" "+bro)
        elif pos==3:
            final = str(bro+" "+final+" "+emoji)
        elif pos==4:
            final = str(final+" "+bro+" "+emoji)
        if final[0]==" ":
            final=final[1:]
        #DebugLog("Generated message",Module="trollbot_core",Functions=['GenerateMessage','sus'])
        return final

    def twitter():
        DebugLog("Generating a type 'twitter' message",Module="trollbot_core",Functions=['GenerateMessage','twitter'])
        twitterphrases = ["cope harder","cope","L","dont care","ratio","blocked","touch grass","climb a tree","take a dump",":clown:"]
        loops=0
        final = twitterphrase=twitterphrases[random.randint(0,9)]
        while loops<3:
            if random.randint(1,30)==9:
                twitterphrase=twitterphrases[random.randint(0,9)].upper()
            else:
                twitterphrase=twitterphrases[random.randint(0,9)]
            final = final+" + "+twitterphrase
            loops=loops+1
        if final[0]==" ":
            final=final[1:]
        #DebugLog("Generated message",Module="trollbot_core",Functions=['GenerateMessage','twitter'])
        return final

    def funny():
        DebugLog("Generating a type 'funny' message",Module="trollbot_core",Functions=['GenerateMessage','funny'])
        funny = ['LOL','LUL','LOOOOOL','loool','lol','lul','funny']
        final=funny[random.randint(0,6)]
        if final[0]==" ":
            final=final[1:]
        #DebugLog("Generated message",Module="trollbot_core",Functions=['GenerateMessage','funny'])
        return final

    def good():
        DebugLog("Generating a type 'good' message",Module="trollbot_core",Functions=['GenerateMessage','good'])
        good = ['pog','poggers','pogggggg','good','awesome','amazing','insane','cool','not cap']
        thats = ["that's","thats","that is"]
        bro = ["broski","bro","man","brother"]
        good=good[random.randint(0,8)]
        thats=thats[random.randint(0,2)]
        bro=bro[random.randint(0,3)]

        final = str(thats+" "+good)
        if random.randint(1,10)==7:
            good=good.upper()
        pos=random.randint(1,2)
        if pos==1:
            final = str(bro+" "+final)
        elif pos==2:
            final = str(final+" "+bro)

        if final[0]==" ":
            final=final[1:]
        #DebugLog("Generated message",Module="trollbot_core",Functions=['GenerateMessage','good'])
        return final

    def ip():
        DebugLog("Generating a type 'ip' message",Module="trollbot_core",Functions=['GenerateMessage','ip'])
        yo = ['ayo :flushed:','yooo','yo','ayo',':flushed:']
        yo=yo[random.randint(0,4)]
        ipaddress = str(str(random.randint(1,256))+"."+str(random.randint(1,256))+"."+str(random.randint(1,256))+"."+str(random.randint(1,256)))
        final = str(ipaddress)
        if random.randint(1,10)==7:
            yo=yo.upper()
        pos=random.randint(1,2)
        if pos==1:
            final = str(yo+" "+final)
        elif pos==2:
            final = str(final+" "+yo)

        if final[0]==" ":
            final=final[1:]
        #DebugLog("Generated message",Module="trollbot_core",Functions=['GenerateMessage','ip'])
        return final

    def dsmp():
        DebugLog("Generating a type 'dsmp' message",Module="trollbot_core",Functions=['GenerateMessage','dsmp'])
        love = ['i love','anyone else love','I LOVE','ANYONEEEEE LOVE','I LIKE','i like','any1 else like','anyone else really love']
        emojis= [':hot_face:',':smiling_face_with_3_hearts:',':drooling_face:',':two_hearts:',':heart_eyes_cat:',':heart_eyes:']
        dsmpchar = ['dream','tommyinnit','ranboo','sapnap','georgenotfound','badboyhalo','tubbo','wilbur','quackity']
        love=love[random.randint(0,7)]
        emoji=emojis[random.randint(0,5)]
        dsmpchar=dsmpchar[random.randint(0,8)]
        final = str(love+" "+dsmpchar)

        pos=random.randint(1,2)
        if pos==1:
            final = str(emoji+" "+final)
        elif pos==2:
            final = str(final+" "+emoji)

        if final[0]==" ":
            final=final[1:]
        #DebugLog("Generated message",Module="trollbot_core",Functions=['GenerateMessage','dsmp'])
        return final

    def poop():
        DebugLog("Generating a type 'poop' message",Module="trollbot_core",Functions=['GenerateMessage','poop'])
        ims = ['anyone else','im really','any1 else really','im so','bro im so','why am i so','why am i','help im really']
        emojis= [':stuck_out_tongue:',':confounded:',':weary:',':tired_face:',':persevere:',':worried:',':face_with_symbols_over_mouth:',':grimacing:']
        thing = ['constipated','gassy rn','gassy','full of gas','runny','constipated rn','constipated right now','gassy right now']
        im=ims[random.randint(0,7)]
        emoji=emojis[random.randint(0,7)]
        thing=thing[random.randint(0,7)]
        final = str(im+" "+thing)
        if random.randint(1,20)==19:
            final=final.upper()


        if random.randint(1,3)==3:
            final=final+str("?"*random.randint(1,8))

        pos=random.randint(1,2)
        if pos==1:
            final = str(emoji+" "+final)
        elif pos==2:
            final = str(final+" "+emoji)

        if final[0]==" ":
            final=final[1:]
        #DebugLog("Generated message",Module="trollbot_core",Functions=['GenerateMessage','poop'])
        return final

    def game():
        DebugLog("Generating a type 'game' message",Module="trollbot_core",Functions=['GenerateMessage','game'])
        love = ['i love playin','i love','i love playing','i like','i really like','i really like playing','i really really love']
        game = ['roblox','fortnite','among us','fall guys']
        love=love[random.randint(0,6)]

        game=game[random.randint(0,3)]
        final = str(love+" "+game)
        if random.randint(1,10)==6:
            final=final.upper()
        if random.randint(1,10)==5:
            final=str(final+final[len(final)-1:]*random.randint(1,11))
        if random.randint(1,3)==3:
            final=final+str("!"*random.randint(1,16))

        if final[0]==" ":
            final=final[1:]
        #DebugLog("Generated message",Module="trollbot_core",Functions=['GenerateMessage','game'])
        return final

    def ytbot():
        DebugLog("Generating a type 'ytbot' message",Module="trollbot_core",Functions=['GenerateMessage','ytbot'])
        looking = ["lookin' for",'you lookin for','lookin for','u looking at','you looking for','ayo u lookin for','guys r u lookin for','Are You Looking For']
        emojis= [':ballot_box_with_check:',':white_check_mark:',':eggplant:',':peach:',':heart_eyes_cat:',':smiling_imp:',':heart_eyes:',':hot_face:',':flushed:',':yum:',':kissing_closed_eyes:',':wink:',':smiling_face_with_3_hearts:',':relaxed:',':weary:',':tired_face:',':persevere:',':drooling_face:',':woozy_face:']
        thing = ['dream','tommyinnit','ranboo','sapnap','georgenotfound','badboyhalo','tubbo','wilbur','quackity','bathwater','ASMR','NFTs','CRYPTOCURRENCY']
        looking=looking[random.randint(0,len(looking)-1)]
        emoji=emojis[random.randint(0,len(emojis)-1)]+emojis[random.randint(0,len(emojis)-1)]+emojis[random.randint(0,len(emojis)-1)]+emojis[random.randint(0,len(emojis)-1)]+emojis[random.randint(0,len(emojis)-1)]+emojis[random.randint(0,len(emojis)-1)]
        thing=thing[random.randint(0,len(thing)-1)]
        final = str(looking+" "+thing)

        pos=random.randint(1,2)
        if pos==1:
            final = str(emoji+" "+final)
        elif pos==2:
            final = str(final+" "+emoji)

        if final[0]==" ":
            final=final[1:]
        #DebugLog("Generated message",Module="trollbot_core",Functions=['GenerateMessage','ytbot'])
        return final

    messagetype=messagetype.lower()
    if messagetype=="cringe":
        return str(cringe())
    elif messagetype=="sus":
        return str(sus())
    elif messagetype=="twitter":
        return str(twitter())
    elif messagetype=="funny":
        return str(funny())
    elif messagetype=="good":
        return str(good())
    elif messagetype=="ip":
        return str(ip())
    elif messagetype=="dsmp":
        return str(dsmp())
    elif messagetype=="poop":
        return str(poop())
    elif messagetype=="game":
        return str(game())
    elif messagetype=="ytbot":
        return str(ytbot())
    elif messagetype=="random":
        #DebugLog("messagetype='random', choosing random message type",Module="trollbot_core",Functions=['GenerateMessage'])
        rand1=random.randint(1,5)
        if rand1==1:
            return str(cringe())
        elif rand1==2:
            return str(sus())
        elif rand1==3:
            return str(twitter())
        elif rand1==4:
            return str(funny())
        elif rand1==5:
            return str(good())
        elif rand1==6:
            return str(ip())
        elif rand1==7:
            return str(dsmp())
        elif rand1==8:
            return str(poop())
        elif rand1==9:
            return str(game())
    else:
        DebugLog("'"+str(messagetype)+"' is not a valid messagetype",Module="trollbot_core",Functions=['GenerateMessage'])
        raise ValueError

def OpenAIBadSpelling(inputtext):
    DebugLog("OpenAIBadSpelling function triggered",Module="trollbot_core",Functions=['MAIN'])
    openai.api_key = Config("OpenAIAPIKey")
    inputtext=str(inputtext)
    DebugLog(f"inputtext={inputtext}",Module="trollbot_core",Functions=['OpenAIBadSpelling'])
    OpenAIPrompt_Final="Make the following message have very bad grammar and spelling. \n\nHuman: {input}".replace("{input}",str(inputtext))
    DebugLog(f"""Sending the following request to OpenAI:\n ---START---
openai.Completion.create(
engine="text-davinci-002",
prompt={OpenAIPrompt_Final},
temperature=0.8,
max_tokens={str(Config("OpenAITokenLimit"))},
top_p=1,
frequency_penalty=0.0,
presence_penalty=0.6,
stop=[" Human:"]
)
---END---""",Module="trollbot_core",Functions=['OpenAIBadSpelling'])
    try:
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=str(OpenAIPrompt_Final),
        temperature=0.8,
        max_tokens=Config("OpenAITokenLimit"),
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:"]
        )
    except:
    #except openai.error.AuthenticationError:
        Log("Could not send request to OpenAI. Make sure you have used the right API key.",Type="ERROR")
        return

    DebugResponse=str(response)
    DebugLog(f"""OpenAI response: \n---START---\n{DebugResponse}\n---STOP---""",Module="trollbot_core",Functions=['OpenAIBadSpelling'])
    final=str(response.choices[0].text)
    try:
        final=final.split(f':')[1]
    except IndexError:
        pass
    final=final.replace("\n", "", 2)

    if Config("FilterProfanity")==True:
        DebugLog("Importing 'better_profanity'",Module="trollbot_core",Functions=['OpenAIBadSpelling'])
        try:
            from better_profanity import profanity
            DebugLog("Imported 'profanity_filter'",Module="trollbot_core",Functions=['OpenAIBadSpelling'])
        except ImportError:
            DebugLog("Exiting")
            print("Could not import library 'better_profanity'",Module="trollbot_core",Functions=['OpenAIBadSpelling'])
            sys.exit()
        DebugLog("Censoring AI output",Module="trollbot_core",Functions=['OpenAIBadSpelling'])
        final=profanity.censor(str(final),censor_char='-')
    DebugLog("Finished executing function 'OpenAIBadSpelling'",Module="trollbot_core")
    return final

def OpenAIResponse(inputtext,Sender="Human"):
    DebugLog("OpenAIResponse function triggered",Module="trollbot_core")
    global OpenAIPrompt
    openai.api_key = Config("OpenAIAPIKey")
    inputtext=str(inputtext)
    DebugLog(f"inputtext={inputtext}",Module="trollbot_core",Functions=['OpenAIResponse'])
    OpenAIPrompt=str(Config("OpenAIPrompt"))
    OpenAIPrompt_Final=OpenAIPrompt.replace("{botname}",FinalName).replace("{personality}",Config("OpenAIPersonality")).replace("{sendername}",Sender).replace("{message}",str(inputtext))
    OpenAIStopFinal=Config("OpenAIStop").replace("{botname}",FinalName).replace("{personality}",Config("OpenAIPersonality")).replace("{sendername}",Sender).replace("{message}",str(inputtext))
    DebugLog(f"""Sending the following request to OpenAI:\n ---START---
openai.Completion.create(
engine="text-davinci-002",
prompt={OpenAIPrompt_Final},
temperature=1,
max_tokens={str(Config("OpenAITokenLimit"))},
top_p=1,
frequency_penalty=0.0,
presence_penalty=0.6,
stop=[" Human:"]
)
---END---""",Module="trollbot_core",Functions=['OpenAIResponse'])
    try:
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=str(OpenAIPrompt_Final),
        temperature=1,
        max_tokens=Config("OpenAITokenLimit"),
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[OpenAIStopFinal]
        )
    except Exception as Except:
    #except openai.error.AuthenticationError:
        Log("Could not send request to OpenAI. Make sure you have used the right API key.",Type="ERROR")
        DebugLog(Except)
        return
    DebugResponse=str(response)
    DebugLog(f"""OpenAI response: \n---START---\n{DebugResponse}\n---STOP---""",Module="trollbot_core",Functions=['OpenAIResponse'])
    final=str(response.choices[0].text)

    if Config("ParseAIOutput")==True:
        try:
            subfinal=final.split('\n')[1]
            if len(subfinal) > 100:
                final=subfinal
        except IndexError:
            pass


        final=final.replace(f"{FinalName}:","")
        final=final.replace("\n", "", 2)

    if Config("FilterProfanity")==True:
        DebugLog("Importing 'better_profanity'",Module="trollbot_core",Functions=['OpenAIResponse'])
        try:
            from better_profanity import profanity
            DebugLog("Imported 'profanity_filter'",Module="trollbot_core",Functions=['OpenAIResponse'])
        except ImportError:
            DebugLog("Exiting",Module="trollbot_core",Functions=['OpenAIResponse'])
            print("Could not import library 'better_profanity'",Functions=['OpenAIResponse'])
            sys.exit()
        DebugLog("Censoring AI output",Module="trollbot_core",Functions=['OpenAIResponse'])
        final=profanity.censor(str(final),censor_char='-')
    DebugLog("Finished executing function 'OpenAIResponse'",Module="trollbot_core")
    return final