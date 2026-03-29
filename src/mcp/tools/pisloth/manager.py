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
        from .tools import control_pisloth, reset_pisloth

        # 控制 Pisloth 动作
        control_props = PropertyList(
            [
                Property("action_type", PropertyType.STRING, default_value="stop"),
            ]
        )
        add_tool(
            (
                "control_pisloth",
                "控制 Pisloth 机器人执行指定动作，如 'dance' (跳舞) 或 'stop' (停止)。",
                control_props,
                control_pisloth,
            )
        )

        # 重置 Pisloth
        reset_props = PropertyList()
        add_tool(
            (
                "reset_pisloth",
                "重置 Pisloth 机器人到初始位置。",
                reset_props,
                reset_pisloth,
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