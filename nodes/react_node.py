from langchain_ollama import ChatOllama

from tools.product import search_products
from tools.inventory import check_inventory

import json
import re



llm = ChatOllama(
    model="qwen2.5",
    temperature=0
)



tools = {

    "search_products": search_products,

    "check_inventory": check_inventory

}




def extract_json(text):

    try:

        match = re.search(
            r"\{.*\}",
            text,
            re.S
        )


        if match:

            return json.loads(
                match.group()
            )


    except Exception as e:

        print(
            "JSON解析失败:",
            e
        )


    return {}





def react_node(state):


    user_input = state["user_input"]



    prompt=f"""

你是一个浴室柜销售Agent。


你可以调用工具：


search_products:

搜索商品

参数:

{{
"wood_type":"",
"size":"",
"budget":0
}}



check_inventory:

查询库存

参数:

{{
"product_id":""
}}



严格输出:


Thought:

思考


Action:

工具名称


PARAM:

JSON参数



用户问题:

{user_input}



"""


    response = llm.invoke(prompt)


    text=response.content



    print("\n===== ReAct Agent启动 =====")

    print(text)



    # 判断工具


    if "Action:" not in text:


        state["answer"]=text

        return state



    if "search_products" in text:

        action="search_products"


    elif "check_inventory" in text:

        action="check_inventory"


    else:

        state["answer"]=text

        return state




    params=extract_json(text)



    print(
        "参数:",
        params
    )



    # =========================
    # 搜索商品
    # =========================


    if action=="search_products":



        product_result = search_products.invoke(

            {

            "requirement":{


                "size":
                params.get(
                    "size"
                ),


                "style":
                params.get(
                    "style",
                    params.get(
                        "wood_type"
                    )
                ),


                "budget":
                params.get(
                    "budget"
                )

            }

            }

        )



        print(
            "商品结果:",
            product_result
        )



        state["product"]=product_result



        # 自动查询库存

        if product_result:


            product_id = product_result[0]["id"]



            stock_result = check_inventory.invoke(

                {

                "product_id":
                product_id

                }

            )


            state["stock"]=stock_result



            print(
                "库存结果:",
                stock_result
            )



    # =========================
    # 用户直接查库存
    # =========================


    elif action=="check_inventory":



        stock_result = check_inventory.invoke(

            {

            "product_id":
            params.get(
                "product_id"
            )

            }

        )


        state["stock"]=stock_result




    # =========================
    # 最终回答
    # =========================


    final_prompt=f"""


用户需求:

{user_input}



商品信息:

{state.get("product")}



库存信息:

{state.get("stock")}



请作为淘宝浴室柜客服回复。



要求:

1.介绍匹配商品

2.说明尺寸

3.说明风格

4.说明价格

5.说明库存情况

6.不要提工具



"""


    final_response=llm.invoke(
        final_prompt
    )



    state["answer"]=final_response.content



    return state