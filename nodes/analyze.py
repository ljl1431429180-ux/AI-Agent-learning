from state import AgentState

from langchain_ollama import ChatOllama

import json


llm = ChatOllama(
    model="qwen2.5",
    temperature=0
)



def analyze_requirement(state: AgentState):

    user_input = state["user_input"]


    prompt = f"""
你是一个电商浴室柜客服助手。

请分析用户需求。

用户输入：

{user_input}


请只返回JSON：

{{
"size":"",
"style":"",
"budget":0
}}

不要输出其他文字。
"""


    response = llm.invoke(prompt)


    requirement = json.loads(
        response.content
    )


    state["requirement"] = requirement


    print(
        "Analyze:需求分析完成"
)


    return state
