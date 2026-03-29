"""
Pisloth 机器人控制 MCP 工具函数.
"""

import asyncio
from typing import Any, Dict

from src.utils.logging_config import get_logger

# 导入 pisloth_action 模块
from .pisloth_action import do_action, reset_servos

logger = get_logger(__name__)


async def control_pisloth(args: Dict[str, Any]) -> str:
    """
    控制 Pisloth 机器人执行动作.
    """
    try:
        action_type = args.get("action_type", "stop")

        # 在线程池中运行同步函数
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, do_action, action_type)

        return f"成功执行动作: {action_type}"

    except Exception as e:
        logger.error(f"控制 Pisloth 失败: {e}")
        return f"控制 Pisloth 失败: {str(e)}"


async def reset_pisloth(args: Dict[str, Any]) -> str:
    """
    重置 Pisloth 机器人到初始位置.
    """
    try:
        # 在线程池中运行同步函数
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, reset_servos)

        return "成功重置 Pisloth 机器人"

    except Exception as e:
        logger.error(f"重置 Pisloth 失败: {e}")
        return f"重置 Pisloth 失败: {str(e)}"