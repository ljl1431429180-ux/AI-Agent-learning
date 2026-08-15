from state import AgentState

from tools.memory import load_memory, update_memory



def read_memory(state:AgentState):


    memory = load_memory()



    state["history"] = memory



    print(
        "Memory:读取用户历史"
    )



    return state





def save_user_memory(state:AgentState):


    update_memory(
        state["user_input"]
    )



    print(
        "Memory:保存本次请求"
    )



    return state