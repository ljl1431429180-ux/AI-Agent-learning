from tools.tools_registry import tools
from memory.chat_memory import ChatMemory

from nodes.agent_brain import agent_brain
from nodes.result_analyzer import analyze_tool_result
from nodes.answer_generator import generate_answer
from nodes.extract_memory import extract_memory
from nodes.requirement_checker import check_requirement

import json



# =========================
# 初始化Memory
# =========================

memory = ChatMemory()



# =========================
# 获取工具
# =========================

def get_tool(name):

    for tool in tools:

        if tool.name == name:

            return tool


    return None




# =========================
# 兼容获取state
# =========================

def get_state_value(state,key,default=None):


    # 字典

    if isinstance(state,dict):

        return state.get(
            key,
            default
        )


    # 对象

    return getattr(
        state,
        key,
        default
    )





# =========================
# 兼容修改state
# =========================

def set_state_value(state,key,value):


    if isinstance(state,dict):

        state[key]=value


    else:

        setattr(
            state,
            key,
            value
        )





# =========================
# Action解析
# =========================

def parse_action(text):


    action=None

    params={}



    lines=text.splitlines()



    for i,line in enumerate(lines):

        line=line.strip()


        if line.startswith("Action:"):


            action=line.replace(
                "Action:",
                ""
            ).strip()



            if action=="":


                if i+1<len(lines):

                    action=lines[i+1].strip()


            break





    if "PARAM:" in text:


        try:


            param_text=text.split(
                "PARAM:"
            )[1]


            start=param_text.find("{")

            end=param_text.rfind("}")


            if start!=-1 and end!=-1:


                params=json.loads(

                    param_text[start:end+1]

                )


        except Exception as e:


            print(
                "参数解析失败:",
                e
            )



    return action,params





# =========================
# ReAct Agent
# =========================

def react_agent(state):


    print(
        "===== ReAct Agent启动 ====="
    )



    user_input=get_state_value(
        state,
        "user_input",
        ""
    )

    state = extract_memory(state)


    user_profile = get_state_value(
        state,
        "user_profile",
        {}
    )



    requirement_result = check_requirement(
        user_profile
    )



    print(
        "需求检查:",
        requirement_result
    )

    print(
        "用户画像:",
        user_profile
    )

    if not requirement_result["complete"]:


        missing = requirement_result["missing"]


        question = "为了帮您推荐合适的浴室柜，还需要了解："


        for item in missing:

            question += "\n- " + item



        set_state_value(

            state,

            "answer",

            question

        )


        set_state_value(

            state,

            "status",

            "NEED_INFO"

        )


        return state

    try:

        history=memory.get_recent(
            10
        )

    except:


        history=[]





    status="START"


    tool_results={}


    observation_history=[]


    executed_tools=[]


    max_iterations=5





    for step in range(max_iterations):


        print(
            f"===== 第 {step+1} 次思考 ====="
        )





        content=agent_brain(

            user_input,

            history,

            tool_results,

            observation_history,

            status,

            user_profile
            
        )



        print(content)





        # =====================
        # Final
        # =====================

        if "Final:" in content:


            answer = generate_answer(
                user_input,

                tool_results,

                user_profile

            )



            set_state_value(

                state,

                "answer",

                answer

            )




            try:


                memory.add_chat(

                    user_input,

                    answer

                )


            except Exception as e:


                print(
                    "保存失败:",
                    e
                )



            print(
                "===== Agent结束 ====="
            )



            return state





        # =====================
        # Action
        # =====================

        action,params=parse_action(
            content
        )




        if action is None:


            print(
                "没有Action"
            )


            continue





        # =====================
        # 防止重复调用
        # =====================

        if action in executed_tools:


            print(
                "工具重复:",
                action
            )


            status="ERROR"

            break






        tool=get_tool(
            action
        )



        if tool is None:


            print(
                "工具不存在:",
                action
            )


            continue






        print(
            "执行工具:",
            action
        )


        print(
            "参数:",
            params
        )





        try:


            result=tool.invoke(
                params
            )


        except Exception as e:


            result={

                "error":str(e)

            }





        print(
            "Observation:"
        )


        print(result)






        # =====================
        # 分析工具结果
        # =====================

        analysis=analyze_tool_result(

            action,

            result

        )


        print(
            "分析结果:"
        )


        print(analysis)






        observation={

            "tool":action,

            "result":analysis

        }



        observation_history.append(
            observation
        )



        tool_results[action]=analysis



        executed_tools.append(
            action
        )





        # =====================
        # 状态更新
        # =====================

        result_status = analysis.get(
            "status"
        )



        if result_status == "PRODUCT_FOUND":


            status = "SEARCH_DONE"



        elif result_status == "STOCK_AVAILABLE":


            status = "INVENTORY_DONE"



        elif result_status == "NO_PRODUCT":


            status = "NO_PRODUCT"



        elif result_status == "OUT_OF_STOCK":


            status = "OUT_OF_STOCK"



        else:


            status = "TOOL_ERROR"


    






    set_state_value(

        state,

        "answer",

        "暂时无法完成查询"

    )


    return state