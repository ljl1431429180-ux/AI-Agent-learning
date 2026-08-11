from tools.inventory import check_inventory



result = check_inventory.invoke(
    {
        "product_id":"8067"
    }
)


print(result)