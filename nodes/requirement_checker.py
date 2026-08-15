# =========================
# 用户需求完整性检查
# =========================
# 不调用LLM
# 不调用工具
# 只负责判断缺少什么信息
# =========================



def check_requirement(user_profile):


    missing = []



    # 尺寸

    if not user_profile.get("size"):

        missing.append(
            "尺寸"
        )



    # 风格

    if not user_profile.get("style"):

        missing.append(
            "风格"
        )



    # 预算

    if not user_profile.get("budget"):

        missing.append(
            "预算"
        )




    if missing:


        return {

            "complete":False,

            "missing":missing

        }



    return {

        "complete":True,

        "missing":[]

    }