import re

from strip_ansi import strip_ansi
from typing import List
from typing_extensions import override
from mcdreforged.utils import string_utils
from mcdreforged.info_reactor.info import InfoSource, Info
from mcdreforged.handler.impl import AbstractMinecraftHandler
from venture_chat_handler.config import RegexConfig, load_config

class VentureChatHandler(AbstractMinecraftHandler):
    # 获取处理器的名称
    def get_name(self) -> str:
        return 'venturechat_handler'

    # 从服务器标准输出中解析原始结果
    @classmethod
    def get_server_stdout_raw_result(cls, text: str) -> Info:
        if type(text) is not str:
            raise TypeError('The text to parse should be a string')
        result = Info(InfoSource.SERVER, text)
        result.content = strip_ansi(string_utils.clean_console_color_code(text))
        return result

    # 获取内容解析的正则表达式模式
    @classmethod
    @override
    def get_content_parsing_formatter(cls) -> re.Pattern:
        return re.compile(
            r'\[(?P<hour>\d+):(?P<min>\d+):(?P<sec>\d+) (?P<logging>[^]]+)]'
            r': (?P<content>.*)'
        )

    # 获取玩家消息解析的正则表达式模式列表
    @classmethod
    @override
    def get_player_message_parsing_formatter(cls) -> List[re.Pattern]:
        regex = RegexConfig.chat_prefix_regex
        return [re.compile(regex)]
def on_load(server, prev_module):
    load_config(server)
    server.register_server_handler(VentureChatHandler())