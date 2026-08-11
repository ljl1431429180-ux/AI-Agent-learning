from typing import TypedDict


class AgentState(TypedDict):

    user_input:str

    requirement:dict

    product:dict

    stock:int

    knowledge:str

    answer:str

    memory:dict

    user_profile:dict
    
    logs:list