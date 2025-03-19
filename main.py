from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api.message_components import At, Plain

@register("welcome", "Astrobot", "新人入群欢迎插件", "1.0.0")
class WelcomePlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    @filter.notice(type="group_increase")
    async def welcome_new_member(self, event: AstrMessageEvent):
        """新人入群时发送欢迎消息"""
        # 从原始消息中获取新成员QQ号
        user_id = str(event.raw_message.data["user_id"])
        
        # 构造欢迎消息
        welcome_msg = [
            At(qq=user_id),
            Plain(" 欢迎加入本群！请仔细阅读群公告～")
        ]
        
        # 发送消息
        yield event.chain_result(welcome_msg)

    async def terminate(self):
        pass