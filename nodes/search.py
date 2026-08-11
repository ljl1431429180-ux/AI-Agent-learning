from state import AgentState

from tools.product import search_products



def search_product(state: AgentState):

    requirement = state["requirement"]


    products = search_products(requirement)


    # 找到商品
    if products:

        state["product"] = products[0]


    # 没找到商品，返回默认商品
    else:

        state["product"] = {

            "id": "8067",

            "size": "120cm",

            "style": "胡桃木",

            "price": 2999

        }


    return state