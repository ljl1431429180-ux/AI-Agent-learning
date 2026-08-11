import json
import os


MEMORY_FILE = "memory/user_memory.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return {
            "user_profile": {},
            "history": []
        }


    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_memory(memory):

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            memory,
            f,
            ensure_ascii=False,
            indent=4
        )



def read_memory(state):

    memory = load_memory()


    state["memory"] = memory


    if "logs" not in state:
        state["logs"] = []


    state["logs"].append(
        "Memory:读取用户历史"
    )


    return state



def update_memory(state):

    memory = load_memory()


    # 保存聊天记录
    memory["history"].append(
        state["user_input"]
    )


    # 保存用户画像
    if state.get("user_profile"):


        memory["user_profile"].update(
            state["user_profile"]
        )


    save_memory(memory)



    state["logs"].append(
        "Memory:保存用户记忆"
    )


    return state