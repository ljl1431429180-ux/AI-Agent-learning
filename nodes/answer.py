from langchain_ollama import ChatOllama



llm = ChatOllama(
    model="qwen2.5",
    temperature=0
)




def generate_answer(state):


    user_input = state["user_input"]



    product = state.get(
        "product",
        []
    )


    stock = state.get(
        "stock",
        {}
    )



    prompt = f"""

你是淘宝浴室柜客服。


用户需求:

{user_input}



商品信息:

{product}



库存信息:

{stock}



请回复客户。


要求:

1.介绍匹配商品

2.说明尺寸

3.说明风格

4.说明价格

5.说明库存

6.语气像淘宝客服

7.不要提Agent、工具、代码



"""


    response = llm.invoke(
        prompt
    )



    state["answer"] = response.content



    return state