import oshla_utils
from oshla_utils import get_yaml


ConfigFile="config.yml"
AdvancedConfigFile="advanced_config.yml"
PastMessagesFile="past_messages.yml"
VersionFile="version.yml"
SecretsFile="secrets.yml"

#--- Some documentation on what variables in this file are (some info may be outdated) ---
#CONFIG-VARS
#DiscordToken - Discord bot/userbot token
#DiscordBotType - Type of Discord bot (userbot, bot)
#DiscordBotPrefix - Discord bot prefix
#DiscordResponseChance - Chance the Discord bot will respond to a message
#DiscordMessageWait - Wait to send a message? True, False
#OpenAIPersonalities - List of personalities
#OpenAIPersonality - User chosen personality
#IgnoredUsers - Users that are ignored by the bot

#ADVANCED-CONFIG-VARS
#OpenAIPrompt - Prompt to give OpenAI
#OpenAITokenLimit - OpenAI token limit
#LengthLimit - AI input length limit
#LengthyAction - What to do if a message is too long (clip, ignore, weird)
#FilterProfanity - Filter profanity from the AI
#UsePrompt - Use prompt or not
#ParseAIOutput - Parse the AI output
#CacheConfig - Cache the config during runtime
#Debug - Enable debugging
#DebugExclude - Exclude certain modules
#OpenAIStop - Stop words
#UseOldMessages - Whether to use messages the bot has sent previously instead of generating a new one
#BadSpelling - If the bot should spell badly

#MISC-VARS
#PastMessages - Past messages the bot has sent encoded in Base64 matched to SHA-256 hashes of a lowercase version of the message it was responding to
#CurrentVersionHuman - Current version in a human readable format, "0.1", "0.2" etc.
#CurrentVersion - Current version in a format easily read by the script. ("1", "2", "3" etc.)
#OpenAIAPIKey - OpenAI API key to use
#UberduckAuthHeader - Authorization header to use when sending API requests to Uberduck.ai

#VAR-TYPES
#OpenAIPrompt - str
#OpenAITokenLimit - int
#OpenAIPersonality - str
#LengthLimit - int
#LengthyAction - str
#FilterProfanity - bool
#UsePrompt - bool
#ParseAIOutput - bool
#Debug - bool
#DebugExclude - list
#DiscordBotPrefix - str
#DiscordResponseChance - float
#DiscordMessageWait - bool
#OpenAIAPIKey - str
#OpenAIStop - str
#IgnoredUsers - list
#PastMessages - dict
#UseOldMessages - bool
#CurrentVersionHuman - str
#CurrentVersion - int
#UpdateInfoLink - str
#BadSpelling - bool
#UseVC - bool
#UberduckAuthHeader - str
#------------------------

def Configure(Module):
    global CacheConfig
    global CachedConfig
    global CachedAdvancedConfig
    global CachedPastMessages
    global CachedSecrets
    advconfig=get_yaml(AdvancedConfigFile)
    config=get_yaml(ConfigFile)
    if bool(advconfig['cache-config'])==True:
        CacheConfig=True
    else:
        CacheConfig=False
    CachedConfig=config
    CachedAdvancedConfig=advconfig
    CachedPastMessages=get_yaml(PastMessagesFile)
    CachedSecrets=get_yaml(SecretsFile)
    if bool(advconfig['debug'])==True:
        oshla_utils.DebugEnable(ShowTime=False,Exclude=advconfig['debug-exclude'],Module=Module)

def DebugLog(log,Functions=['MAIN']):
    oshla_utils.DebugLog(log,Module="trollbot_config",Functions=Functions)

def GetConfig(entry):
    entryorig=str(entry)
    entry=str(entry).lower()
    final=None
    config=ConfigFile
    advancedconfig=AdvancedConfigFile
    PastMessages=PastMessagesFile
    secrets=SecretsFile
    if entry=="openaiprompt":
        if CacheConfig==True:
            final=str(CachedAdvancedConfig['openai-prompt'])
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
        else:
            final=str(get_yaml(advancedconfig)['openai-prompt'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="openaitokenlimit":
        if CacheConfig==True:
            final=CachedAdvancedConfig['token-limit']
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
        else:
            final=int(get_yaml(advancedconfig)['token-limit'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="uberduckauthheader":
        if CacheConfig==True:
            final=CachedSecrets['uberduck-auth-header']
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
        else:
            final=int(get_yaml(secrets)['uberduck-auth-header'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="openaipersonality":
        if CacheConfig==True:
            final=str(list(CachedConfig['personalities'])[int(CachedConfig['personality'])-1])
            DebugLog(f"Took {entryorig} from cache",Functions="GetConfig")
        else:
            final=str(list(get_yaml(config)['personalities'])[int(get_yaml(config)['personality'])-1])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="lengthlimit":
        if CacheConfig==True:
            final=int(CachedAdvancedConfig['length-limit'])
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
        else:
            final=int(get_yaml(advancedconfig)['length-limit'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="lengthyaction":
        if CacheConfig==True:
            final=str(CachedAdvancedConfig['lengthy-messages-action'])
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
        else:
            final=str(get_yaml(advancedconfig)['lengthy-messages-action'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="filterprofanity":
        if CacheConfig==True:
            final=bool(CachedAdvancedConfig['filter-profanity'])
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
        else:
            final=bool(get_yaml(advancedconfig)['filter-profanity'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="useprompt":
        if CachedAdvancedConfig['no-prompt']==True:
            final=False
        else:
            final=True
        DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])

    if entry=="parseaioutput":
        if CacheConfig==True:
            final=bool(CachedAdvancedConfig['parse-output'])
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
        else:
            final=bool(get_yaml(advancedconfig)['parse-output'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="debug":
        final=bool(CachedAdvancedConfig['debug'])
        DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])

    if entry=="debugexclude":
        final=list(CachedAdvancedConfig['debug-exclude'])
        DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])

    if entry=="discordbotprefix":
        if CacheConfig==True:
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
            final=str(CachedConfig['bot-prefix'])
        else:
            final=str(get_yaml(config)['bot-prefix'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="discordresponsechance":
        if CacheConfig==True:
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
            final=float(CachedConfig['response-chance'])
        else:
            final=float(get_yaml(config)['response-chance'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="discordmessagewait":
        if CacheConfig==True:
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
            final=bool(CachedConfig['send-wait'])
        else:
            final=bool(get_yaml(config)['send-wait'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="openaiapikey":
        if CacheConfig==True:
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
            final=str(CachedSecrets['openai-api-key'])
        else:
            final=str(get_yaml(secrets)['openai-api-key'])
            DebugLog(f"Took {entryorig} from secrets.yml",Functions=["GetConfig"])

    if entry=="openaistop":
        if CacheConfig==True:
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
            final=str(CachedAdvancedConfig['openai-stop'])
        else:
            final=str(get_yaml(advancedconfig)['openai-stop'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="ignoredusers":
        if CacheConfig==True:
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
            final=list(CachedConfig['ignored-users'])
        else:
            final=list(get_yaml(config)['ignored-users'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="pastmessages":
        if CacheConfig==True:
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
            final=dict(CachedPastMessages)
        else:
            final=dict(get_yaml(PastMessages))
            DebugLog(f"Took {entryorig} from YAML file",Functions=["GetConfig"])

    if entry=="useoldmessages":
        if CacheConfig==True:
            final=bool(CachedAdvancedConfig['use-old-messages'])
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
        else:
            final=bool(get_yaml(advancedconfig)['use-old-messages'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="currentversionhuman":
        final=str(get_yaml(VersionFile)['version_human'])
        DebugLog(f"Took {entryorig} from 'version.yml'",Functions=["GetConfig"])

    if entry=="currentversion":
        final=int(get_yaml(VersionFile)['version'])
        DebugLog(f"Took {entryorig} from 'version.yml'",Functions=["GetConfig"])

    if entry=="badspelling":
        if CacheConfig==True:
            final=bool(CachedAdvancedConfig['bad-spelling'])
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
        else:
            final=bool(get_yaml(advancedconfig)['bad-spelling'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])

    if entry=="usevc":
        if CacheConfig==True:
            DebugLog(f"Took {entryorig} from cache",Functions=["GetConfig"])
            final=bool(CachedConfig['join-voice'])
        else:
            final=bool(get_yaml(config)['join-voice'])
            DebugLog(f"Took {entryorig} from YAML config",Functions=["GetConfig"])
    
    return final


