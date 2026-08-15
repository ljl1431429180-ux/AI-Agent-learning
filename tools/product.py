from langchain_core.tools import tool



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

    requirement:
    {
        "size":"120cm",
        "style":"胡桃木",
        "budget":4000
    }
    """



    # =========================
    # 兼容 Agent 多包一层
    # =========================

    if "requirement" in requirement:

        requirement = requirement["requirement"]



    result = []



    size = requirement.get(
        "size"
    )


    style = requirement.get(
        "style"
    )


    budget = requirement.get(
        "budget",
        0
    )



    for product in products:


        if size:

            if product["size"] != size:

                continue



        # 风格匹配

        if style:


            style_map = {


                "木色":[

                    "胡桃木",
                    "原木"

                ],


                "实木":[

                    "胡桃木",
                    "原木"

                ],


                "现代":[

                    "现代"

                ]

            }



            if style in style_map:


                if product["style"] not in style_map[style]:

                    continue


            else:


                if product["style"] != style:

                    continue



        if budget:

            if product["price"] > budget:

                continue



        result.append(product)



    return result