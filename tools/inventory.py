from langchain_core.tools import tool



# 库存数据库

inventory = {


    "8067":5,


    "8070":0,


    "8090":8


}




@tool
def check_inventory(product_id:str):
    """
    查询商品库存。

    参数:
    {
        "product_id":"8067"
    }

    返回库存数量
    """



    stock = inventory.get(
        product_id,
        0
    )



    return {

        "product_id":product_id,

        "stock":stock

    }