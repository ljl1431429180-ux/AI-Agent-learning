from state import AgentState


def extract_memory(state: AgentState):

    text = state["user_input"]


    profile = {}


    if "胡桃木" in text:
        profile["style"] = "胡桃木"


    if "现代风" in text:
        profile["style"] = "现代风"


    if "预算" in text:

        budget = text.split("预算")[1]

        profile["budget"] = budget.strip()



    if "1.2米" in text:

        profile["size"] = "1.2米"


    if "1.5米" in text:

        profile["size"] = "1.5米"



    state["user_profile"] = profile



    state["logs"].append(
        "Memory:提取用户画像"
    )


    return state