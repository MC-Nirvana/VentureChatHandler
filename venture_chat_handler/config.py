from mcdreforged.api.all import *

# 定义默认配置
class RegexConfig(Serializable):
    chat_prefix_regex: str = r'(\[.*] )?(?P<name>[^>]+)>>> (?P<message>.*)'

# 全局配置对象
config: RegexConfig

# 加载配置文件
def load_config(server):
    global config
    config = server.load_config_simple(target_class=RegexConfig)