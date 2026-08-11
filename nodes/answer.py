from state import AgentState

from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen2.5",
    temperature=0,
    num_predict=300
)



def generate_answer(state: AgentState):


    prompt = f"""

你是一名专业浴室柜客服。


用户需求：

{state["user_input"]}



商品信息：

{state["product"]}



库存信息：

{state["stock"]}



产品知识库信息：

{state["knowledge"]}



请根据以上信息回答用户。


要求：

1. 推荐合适商品
2. 说明产品卖点
3. 告知价格和库存
4. 语气像真实客服


不要输出分析过程。

"""


    response = llm.invoke(prompt)


    state["answer"] = response.content


    return state