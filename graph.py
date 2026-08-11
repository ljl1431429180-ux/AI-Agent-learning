from langgraph.graph import StateGraph, START, END


from state import AgentState


# 原来的节点
from nodes.memory import read_memory
from nodes.analyze import analyze_requirement
from nodes.answer import generate_answer


# 新ReAct节点
from nodes.react_node import react_node



# 创建工作流

workflow = StateGraph(AgentState)



# =====================
# 添加节点
# =====================


workflow.add_node(
    "memory",
    read_memory
)


workflow.add_node(
    "analyze",
    analyze_requirement
)


workflow.add_node(
    "react",
    react_node
)


workflow.add_node(
    "answer",
    generate_answer
)



# =====================
# 流程开始
# =====================


workflow.add_edge(
    START,
    "memory"
)



workflow.add_edge(
    "memory",
    "analyze"
)



workflow.add_edge(
    "analyze",
    "react"
)



workflow.add_edge(
    "react",
    "answer"
)



workflow.add_edge(
    "answer",
    END
)



# 编译Agent

agent = workflow.compile()