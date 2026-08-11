from langchain_ollama import ChatOllama

from tools.product import search_products
from tools.inventory import check_inventory


llm = ChatOllama(
    model="qwen2.5",
    temperature=0
)


# 工具集合
tools = {

    "search_products": search_products,

    "check_inventory": check_inventory

}



def react_node(state):

    user_input = state["user_input"]


    prompt = f"""
你是一个浴室柜销售Agent。

你可以调用以下工具：

1. search_products
用途：
根据用户需求搜索商品。

参数：
{{
"wood_type":"",
"size":"",
"budget":0
}}


2. check_inventory
用途：
查询商品库存。

参数：
{{
"product_id":""
}}


请严格按照下面格式输出：

Thought:
你的思考

Action:
工具名称

PARAM:
JSON参数


用户问题：

{user_input}


如果已经获得答案：

Final:
最终回复

"""


    response = llm.invoke(prompt)


    text = response.content


    print("\n===== ReAct Agent启动 =====")

    print(text)



    # 判断是否调用工具

    if "Action:" in text:


        action = None


        if "search_products" in text:

            action = "search_products"


        elif "check_inventory" in text:

            action = "check_inventory"



        if action:


            print("\n执行工具:", action)


            # 简单参数解析

            if action == "search_products":


                result = search_products(
                    {
                        "wood_type":"胡桃木",
                        "size":"120cm",
                        "budget":4000
                    }
                )


            elif action == "check_inventory":


                result = check_inventory(
                    "8067"
                )


            print("\n工具结果:")

            print(result)



            # 第二次让LLM总结

            final_prompt = f"""

用户问题:

{user_input}


工具返回:

{result}


请根据工具结果回答用户。

要求：
像淘宝客服一样回答。
简洁、自然。


"""


            final_response = llm.invoke(final_prompt)


            state["answer"] = final_response.content


        else:

            state["answer"] = text



    else:

        state["answer"] = text



    return state