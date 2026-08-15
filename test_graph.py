from graph import agent



# =========================
# 初始化 LangGraph State
# =========================

state = {


    # 用户输入

    "user_input":
    "我要一个120cm胡桃木浴室柜，预算3000",



    # 历史聊天

    "history":[],



    # 用户画像

    "user_profile":{},



    # 当前状态

    "status":
    "START",



    # 缺失需求

    "missing_requirements":[],



    # 工具结果

    "tool_results":{},



    # 工具观察

    "observation_history":[],



    # 已执行工具

    "executed_tools":[],



    # 日志

    "logs":[],



    # 最终答案

    "answer":""



}



print("===================")

print("开始运行Agent")

print("===================")



# =========================
# 调用LangGraph
# =========================

result = agent.invoke(
    state
)



print("===================")

print("Agent运行结束")

print("===================")



print()

print("最终答案:")

print(
    result.get(
        "answer",
        ""
    )
)



print()

print("用户画像:")

print(
    result.get(
        "user_profile",
        {}
    )
)



print()

print("日志:")

print(
    result.get(
        "logs",
        []
    )
)