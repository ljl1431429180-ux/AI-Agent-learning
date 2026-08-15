from langchain_ollama import ChatOllama



llm = ChatOllama(
    model="qwen2.5",
    temperature=0
)





# =========================
# Agent 大脑
# 负责思考下一步动作
# 不执行工具
# =========================


def agent_brain(
    requirement,
    history,
    tool_results,
    observation_history,
    status,
    user_profile
):


    # =====================
    # 强制状态控制
    # =====================


    # 已完成库存查询

    if status == "INVENTORY_DONE":


            return """
            Final:
            DONE
            """




    # 没有找到商品

    if status == "NO_PRODUCT":


        return """

Final:

抱歉，目前没有找到完全符合您要求的商品。

您可以调整一下尺寸、颜色或者预算，我可以继续帮您寻找合适的浴室柜。

"""



    # 商品无库存

    if status == "OUT_OF_STOCK":


        return """

Final:

抱歉，该商品目前暂无库存。

如果您需要，我可以帮您推荐其他类似款式。

"""





    # =====================
    # 正常思考
    # =====================


    prompt = f"""

你是一个电商客服Agent的大脑。


你的任务：

根据当前状态决定下一步行动。


====================

用户需求:

{requirement}

====================

用户长期偏好:

{user_profile}

====================

====================

历史聊天:

{history}

用户长期偏好:

{user_profile}
====================

已经执行结果:

{tool_results}


====================

观察结果:

{observation_history}


====================

当前状态:

{status}


====================



你拥有工具:



1. search_products


作用：

根据用户需求搜索商品。


参数格式:


{{
    "requirement":
    {{
        "size":"",
        "style":"",
        "budget":0
    }}
}}



--------------------



2. check_inventory


作用：

查询商品库存。


参数格式:


{{
    "product_id":"商品ID"
}}



====================


执行规则:


规则1:

如果状态是:

START


必须调用:

search_products



禁止输出Final。




--------------------


规则2:

如果状态是:

SEARCH_DONE


必须调用:

check_inventory



禁止再次调用search_products。




--------------------


规则3:

如果状态是:

NO_PRODUCT


不要调用工具。

直接结束。



--------------------


规则4:

如果状态是:

INVENTORY_DONE


不要调用工具。

直接结束。



--------------------


规则5:

不要重复调用已经执行的工具。


====================


输出格式:


调用工具:


Action:
工具名称


PARAM:
JSON参数




结束:


Final:
回复内容



只输出结果。

不要解释。

"""


    response = llm.invoke(
        prompt
    )


    return response.content