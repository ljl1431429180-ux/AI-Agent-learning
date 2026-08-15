from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen2.5",
    temperature=0.3
)



def generate_answer(
    user_input,
    tool_results,
    user_profile=None
):


    prompt = f"""

你是一名淘宝浴室柜客服。


客户需求：

{user_input}

用户偏好:

{user_profile}


商品查询结果：

{tool_results}



请生成客服回复。


要求：

回复要求：

1. 像淘宝客服聊天
2. 语气自然
3. 不要编造商品不存在的信息
4. 只能使用查询结果里的信息
5. 必须包含：
   - 商品编号
   - 尺寸
   - 风格
   - 价格
   - 库存
6. 不确定的信息不要回答


回复：

"""


    response = llm.invoke(
        prompt
    )


    return response.content