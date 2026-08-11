from tools.product import search_products


result = search_products.invoke(
    {
        "size":"120cm",
        "style":"胡桃木"
    }
)


print(result)