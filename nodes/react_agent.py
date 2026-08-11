from langchain_ollama import ChatOllama
import json

from tools.tools_registry import tools


llm = ChatOllama(
    model="qwen2.5",
    temperature=0
)



def parse_action(text):

    action = None
    params = {}


    # 兼容:
    # Action:
    # Tool Name: xxx

    if "Tool Name:" in text:

        action = (
            text
            .split("Tool Name:")[1]
            .split("\n")[0]
            .strip()
        )


    elif "Action:" in text:

        action = (
            text
            .split("Action:")[1]
            .split("\n")[0]
            .strip()
        )



    if "PARAM:" in text:

        param_text = (
            text
            .split("PARAM:")[1]
        )


        if "Final:" in param_text:

            param_text = param_text.split("Final:")[0]


        try:

            params=json.loads(
                param_text.strip()
            )

        except:

            params={}



    return action,params




def get_tool(name):

    for tool in tools:

        if tool.name==name:

            return tool


    return None





def react_agent(state):


    user_input=state["user_input"]


    prompt=f"""

你是电商商品Agent。


用户:

{user_input}



工具:


search_products

参数:

{{
"requirement":
{{
"size":"",
"style":"",
"budget":0
}}
}}



check_inventory

参数:

{{
"product_id":"8067"
}}



规则:

如果不知道商品id:

必须 search_products。


拿到商品id后:

必须 check_inventory。


调用工具后，根据结果继续。


最终：

Final:
回答



格式:

Thought:

Action:

Tool Name:

PARAM:



"""



    for step in range(6):


        print(
            f"===== 第 {step+1} 次思考 ====="
        )


        response=llm.invoke(prompt)


        content=response.content


        print(content)



        action,params=parse_action(content)



        # 最终答案

        if "Final:" in content and action is None:


            state["answer"]=(
                content
                .split("Final:")[1]
                .strip()
            )


            return state



        if action:


            tool=get_tool(action)


            if tool:


                print(
                    "执行工具:",
                    action
                )

                print(
                    "参数:",
                    params
                )


                try:

                    result=tool.invoke(params)


                except Exception as e:

                    result=str(e)



                print(
                    "工具返回:"
                )

                print(result)



                prompt += f"""


工具:

{action}


返回结果:

{result}


现在继续。


如果已经知道答案:

输出:

Final:

"""


            else:


                prompt += "\n没有找到该工具"


    state["answer"]="暂时无法完成查询"


    return state