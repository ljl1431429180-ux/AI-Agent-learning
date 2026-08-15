from typing import TypedDict, Any



class AgentState(TypedDict):


    # 用户输入

    user_input:str



    # 历史聊天

    history:list



    # 用户画像

    user_profile:dict



    # 当前状态

    status:str



    # 缺失需求

    missing_requirements:list



    # 工具结果

    product:Any


    stock:Any



    # 最终答案

    answer:str



    # 工具记录

    tool_results:dict



    observation_history:list



    executed_tools:list