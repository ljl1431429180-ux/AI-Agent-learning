from state import AgentState


def check_stock(state: AgentState):

    product = state.get("product", {})


    if "id" not in product:
        state["stock"] = 0
        state["logs"].append(
            "Stock: 未找到商品编号"
        )
        return state


    product_id = product["id"]


    stock_data = {
        "8067":5,
        "8070":10,
        "8090":0
    }


    state["stock"] = stock_data.get(
        product_id,
        0
    )


    state["logs"].append(
        f"Stock: 商品{product_id}库存查询完成"
    )


    return state