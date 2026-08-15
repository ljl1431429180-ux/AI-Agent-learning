# =========================
# 工具结果分析器
# =========================
# 作用:
# 将工具返回结果转换成Agent状态
# 不调用LLM
# 不执行工具
# =========================



def analyze_tool_result(
    tool_name,
    result
):


    # =====================
    # 商品搜索结果分析
    # =====================

    if tool_name == "search_products":



        # 没找到商品

        if (
            result is None
            or result == []
        ):


            return {

                "type":"failed",

                "status":"NO_PRODUCT",


                "message":
                "没有找到符合条件的商品",


                "product_id":None

            }





        # 找到商品


        product = result[0]



        return {


            "type":"success",

            "status":"PRODUCT_FOUND",


            "message":
            "找到符合条件商品，需要继续查询库存",



            "product_id":
            product.get("id"),



            "product":
            product


        }









    # =====================
    # 库存结果分析
    # =====================

    elif tool_name == "check_inventory":



        if isinstance(result,dict):


            stock = result.get(
                "stock",
                0
            )



            if stock > 0:


                return {


                    "type":"success",

                    "status":"STOCK_AVAILABLE",


                    "message":
                    "商品有库存，可以推荐给用户",


                    "stock":
                    stock


                }



            else:


                return {


                    "type":"failed",

                    "status":"OUT_OF_STOCK",


                    "message":
                    "商品暂无库存",


                    "stock":
                    0

                }







    # =====================
    # 工具异常
    # =====================

    if isinstance(result,dict):

        if "error" in result:


            return {


                "type":"failed",

                "status":"TOOL_ERROR",


                "message":
                result["error"]

            }







    # =====================
    # 未知工具
    # =====================


    return {


        "type":"unknown",

        "status":"UNKNOWN",


        "message":
        "未知工具结果"

    }