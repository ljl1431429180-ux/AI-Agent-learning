from tools.product import search_products
from tools.inventory import check_inventory


# =========================
# Agent 可调用工具列表
# =========================

tools = [

    search_products,

    check_inventory

]


# =========================
# 根据名字查找工具
# =========================

def get_tool(tool_name):

    for tool in tools:

        if tool.name == tool_name:

            return tool

    return None