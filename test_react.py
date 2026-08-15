from state import AgentState
from nodes.react_agent import react_agent



print("电商客服 Agent")
print("输入 exit 退出")



state = None



while True:


    user=input(
        "用户:"
    )


    if user=="exit":
        break



    # 第一次创建state

    if state is None:


        state = AgentState(
            user
        )


    else:


        # 后续只更新输入

        state.user_input = user




    result = react_agent(
        state
    )



    print(
        "客服:",
        result.answer
    )