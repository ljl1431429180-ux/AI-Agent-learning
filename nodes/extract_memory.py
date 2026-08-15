# =========================
# 用户需求记忆提取
# =========================


def extract_memory(state):


    text = state.user_input



    # 读取已有画像

    profile = getattr(
        state,
        "user_profile",
        {}
    )



    # 防止None

    if profile is None:

        profile = state.user_profile




    # =====================
    # 提取风格
    # =====================


    if "胡桃木" in text:

        profile["style"] = "胡桃木"



    elif "现代风" in text:

        profile["style"] = "现代风"



    elif "黑色" in text:

        profile["style"] = "黑色"




    # =====================
    # 提取尺寸
    # =====================


    if "120cm" in text:

        profile["size"] = "120cm"



    elif "120厘米" in text:

        profile["size"] = "120cm"



    elif "150cm" in text:

        profile["size"] = "150cm"




    # =====================
    # 提取预算
    # =====================


    if "预算" in text:


        budget=text.split(
            "预算"
        )[1]


        profile["budget"] = budget.strip()



    # =====================
    # 保存回state
    # =====================


    state.user_profile = profile



    print(
        "更新用户画像:",
        profile
    )



    return state