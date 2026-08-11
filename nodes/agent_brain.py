from langchain_ollama import ChatOllama

from tools.product import search_products
from tools.inventory import check_inventory


# 初始化模型
llm = ChatOllama(
    model="qwen2.5",
    temperature=0
)


# 注册工具
tools = [
    search_products,
    check_inventory
]


llm_with_tools = llm.bind_tools(tools)



def agent_brain(state):

    user_input = state["user_input"]


    print("\n========== Agent思考 ==========")

    print("用户需求:")
    print(user_input)



    messages = [
        {
            "role": "system",
            "content":
            """
你是一个浴室柜销售Agent。

你的任务：

1. 根据用户需求寻找商品
2. 如果用户询问库存，需要查询库存
3. 综合工具结果回答用户

可使用工具：
search_products
check_inventory

不要编造商品信息。
"""
        },
        {
            "role": "user",
            "content": user_input
        }
    ]



    # 第一次调用模型

    response = llm_with_tools.invoke(messages)



    # 判断是否调用工具

    if response.tool_calls:


        print("\n========== 工具调用 ==========")


        for tool_call in response.tool_calls:


            print("\n工具名称:")
            print(tool_call["name"])


            print("参数:")
            print(tool_call["args"])



            # 执行搜索商品

            if tool_call["name"] == "search_products":

                result = search_products.invoke(
                    tool_call["args"]
                )


            # 执行库存查询

            elif tool_call["name"] == "check_inventory":

                result = check_inventory.invoke(
                    tool_call["args"]
                )


            else:

                result = "没有找到对应工具"



            print("\n工具返回:")
            print(result)



            # 把工具结果加入消息

            messages.append(
                response
            )


            messages.append(
                {
                    "role":"tool",
                    "content":str(result),
                    "tool_call_id":tool_call["id"]
                }
            )



        # 第二次让模型总结

        final_response = llm.invoke(messages)



        print("\n========== 最终回答 ==========")

        print(final_response.content)



        state["answer"] = final_response.content



    else:


        print("\n模型没有调用工具")

        print(response.content)


        state["answer"] = response.content



    return state