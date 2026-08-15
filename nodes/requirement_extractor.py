from langchain_ollama import ChatOllama
import json



llm = ChatOllama(
    model="qwen2.5",
    temperature=0
)





def extract_requirement(user_input):


    prompt = f"""


你是一个商品需求分析助手。


用户输入:

{user_input}



请提取浴室柜购买需求。


只输出JSON。


格式:


{{
"size":"",
"style":"",
"budget":0
}}



规则:

1. 没有提到尺寸，size为空字符串。

2. 没有提到风格，style为空字符串。

3. 没有提到预算，budget为0。

4. 不要解释。

5. 只输出JSON。


"""


    response = llm.invoke(
        prompt
    )


    text = response.content



    try:


        start=text.find("{")

        end=text.rfind("}")


        data=json.loads(

            text[start:end+1]

        )


        return data



    except Exception:


        return {

            "size":"",
            "style":"",
            "budget":0

        }