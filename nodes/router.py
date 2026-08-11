from state import AgentState


def router(state: AgentState):

    user_input = state["user_input"]


    # 查询库存
    if (
        "库存" in user_input
        or "有货" in user_input
        or "还有多少" in user_input
    ):

        state["route"] = "stock"

        state["logs"].append(
            "Router: 判断需要库存查询流程"
        )


    # 购买推荐
    elif (
        "推荐" in user_input
        or "购买" in user_input
        or "买" in user_input
        or "选择" in user_input
        or "适合" in user_input
    ):

        state["route"] = "search"

        state["logs"].append(
            "Router: 判断商品推荐流程"
        )


    # 产品知识
    elif (
        "材质" in user_input
        or "尺寸" in user_input
        or "介绍" in user_input
        or "功能" in user_input
    ):

        state["route"] = "rag"

        state["logs"].append(
            "Router: 判断知识库查询流程"
        )


    else:

        state["route"] = "rag"

        state["logs"].append(
            "Router: 默认进入知识库"
        )


    return state