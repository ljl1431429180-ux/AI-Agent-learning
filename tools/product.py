from langchain_core.tools import tool


# 商品数据库
products = [

    {
        "id": "8067",
        "size": "120cm",
        "style": "胡桃木",
        "price": 2999
    },


    {
        "id": "8070",
        "size": "150cm",
        "style": "原木",
        "price": 3999
    },


    {
        "id": "8090",
        "size": "120cm",
        "style": "现代",
        "price": 2699
    }

]



@tool
def search_products(requirement: dict):
    """
    根据用户需求搜索商品。

    参数:
    {
        "size":"120cm",
        "style":"胡桃木",
        "budget":4000
    }

    返回符合条件的商品列表
    """


    result = []


    size = requirement.get("size")

    style = requirement.get("style")

    budget = requirement.get("budget",0)



    for product in products:


        # 尺寸匹配
        if size:

            if product["size"] != size:

                continue



        # 风格匹配
        if style:

            if product["style"] != style:

                continue



        # 预算匹配
        if budget:

            if product["price"] > budget:

                continue



        result.append(product)



    return result