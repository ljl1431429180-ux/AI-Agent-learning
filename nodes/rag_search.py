from state import AgentState

from tools.rag import search_knowledge


def rag_search(state: AgentState):

    query = state["user_input"]


    result = search_knowledge(query)


    state["knowledge"] = result


    return state