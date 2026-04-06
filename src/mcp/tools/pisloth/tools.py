"""
Pisloth 机器人控制 MCP 工具函数.
"""

import asyncio
from typing import Any, Dict

from src.utils.logging_config import get_logger

# 导入 sloth 模块
from .sloth import pisloth_do_action

logger = get_logger(__name__)


async def control_pisloth(args: Dict[str, Any]) -> str:
    """
    控制 Pisloth 机器人执行动作.
    """
    try:
        action_type = args.get("action_type", "stand")

        # 在线程池中运行同步函数
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, pisloth_do_action, action_type)

        return f"成功执行动作: {action_type}"

    except Exception as e:
        logger.error(f"控制 Pisloth 失败: {e}")
        return f"控制 Pisloth 失败: {str(e)}"