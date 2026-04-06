"""
Pisloth 机器人控制管理器.
"""

from src.utils.logging_config import get_logger

logger = get_logger(__name__)


class PislothManager:
    """
    Pisloth 管理器.
    """

    def __init__(self):
        pass

    def init_tools(self, add_tool, PropertyList, Property, PropertyType):
        """
        初始化并注册所有 Pisloth 控制工具.
        """
        from .tools import control_pisloth

        # 控制 Pisloth 动作
        control_props = PropertyList(
            [
                Property("action_type", PropertyType.STRING, default_value="stand"),
            ]
        )
        add_tool(
            (
                "control_pisloth",
                "【机器人动作控制】这是你的身体，当用户要求你前进、后退、跳舞或站立时调用此工具。\n"
                "功能：控制 Pisloth 机器人执行物理动作，如前进、后退、跳舞或站立。\n"
                "支持的动作：\n"
                "- 'forward': 机器人前进\n"
                "- 'backward': 机器人后退\n"
                "- 'dance': 执行跳舞动作（机器人会进行舵机运动模拟跳舞）\n"
                "- 'stand': 站立不动（默认动作）\n"
                "使用场景：用户说'前进'、'后退'、'跳个舞'、'跳舞'、'站好'等时调用。\n"
                "参数说明：action_type - 动作类型，字符串类型，默认 'stand'\n"
                "注意：这是物理机器人控制，确保硬件连接正常。",
                control_props,
                control_pisloth,
            )
        )


# 单例模式
_pisloth_manager = None


def get_pisloth_manager():
    """
    获取 Pisloth 管理器单例.
    """
    global _pisloth_manager
    if _pisloth_manager is None:
        _pisloth_manager = PislothManager()
    return _pisloth_manager