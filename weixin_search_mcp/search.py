import sys
from typing import Annotated, Any, List, Dict, Optional
import asyncio
import time
import os
from fastmcp import FastMCP
from dotenv import load_dotenv

from pydantic import Field
import requests
from loguru import logger
from urllib.parse import urlparse, parse_qs
import argparse

# 导入工具函数
from weixin_search_mcp.tools.weixin_search import sogou_weixin_search, get_real_url, get_article_content

# 配置日志
def setup_logger(log_level="INFO"):
    """设置日志配置"""
    logger.remove()
    logger.add(
        sys.stderr,
        level=log_level,
        format= "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <4}</level> | <cyan>using_function:{function}</cyan> | <cyan>{file}:{line}</cyan> | <level>{message}</level>"
    )

setup_logger(log_level="INFO")

def weixin_search(query: Annotated[str, "搜索关键词"], page:  int = 1) -> List[Dict[str, str]]:
    """在搜狗微信搜索中搜索指定关键词并返回结果列表
    Args:
        query: 搜索关键词
    Returns:
        List[Dict[str, str]]: 搜索结果列表
    """
    return sogou_weixin_search(query, page)

def get_weixin_article_content(real_url: Annotated[str, "真实微信公众号文章链接"], referer: Annotated[Optional[str], "请求来源,weixin_search的返回值"]) -> str:
    """获取微信公众号文章的正文内容
    Args:
        real_url: 真实微信公众号文章链接
        referer: 可选,请求来源,weixin_search的返回值
    Returns:
        str: 微信公众号文章的正文内容
    """
    return get_article_content(real_url, referer)

if __name__ == "__main__":
    for i in range(1, 10):
        r = weixin_search('国芯一号', i)
        print(r)
