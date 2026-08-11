from tools.inventory import check_inventory
from tools.product import search_products


print("===== 测试库存工具 =====")


result1 = check_inventory.invoke(
    {
        "product_id": "8067"
    }
)


print(result1)



print("\n===== 测试商品工具 =====")


result2 = search_products.invoke(
    {
        "requirement":
        {
            "size": "120cm",
            "style": "胡桃木",
            "budget": 4000
        }
    }
)


print(result2)