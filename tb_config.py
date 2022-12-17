import coloredlogs, logging, tb_utils
coloredlogs.install(level=tb_utils.GetLogLevel(), fmt='[%(module)s] [%(funcName)s] [%(levelname)s]: %(message)s')


class Config():
    def __init__(self, CacheConfig):
        self.CacheConfig = CacheConfig

        self.AdvancedConfigFile = tb_utils.AdvancedConfigFile
        self.ConfigFile = tb_utils.ConfigFile
        self.LogLevelFile = tb_utils.LogLevelFile
        self.AccsFile = tb_utils.AccsFile
        self.SecretsFile = tb_utils.SecretsFile
        self.VersionFile = tb_utils.VersionFile

        if self.CacheConfig==True:
            logging.debug("Caching config files")
            self.CachedAdvancedConfigFile = tb_utils.get_yaml(self.AdvancedConfigFile)
            self.CachedConfigFile = tb_utils.get_yaml(self.ConfigFile)
            self.CachedLogLevelFile = tb_utils.get_yaml(self.LogLevelFile)
            self.CachedAccsFile = tb_utils.get_yaml(self.AccsFile)
            self.CachedSecretsFile = tb_utils.get_yaml(self.SecretsFile)
            self.CachedVersionFile = tb_utils.get_yaml(self.VersionFile)


    def OpenAIPrompt(self):
        if self.CacheConfig==True:
            return str(self.CachedConfigFile['openai-prompt'])
        else:
            return str(tb_utils.get_yaml(self.ConfigFile)['openai-prompt'])

    def OpenAITokenLimit(self):
        if self.CacheConfig==True:
            return str(self.CachedAdvancedConfigFile['token-limit'])
        else:
            return str(tb_utils.get_yaml(self.AdvancedConfigFile)['token-limit'])

    #gotta do a lot more config variables soon...