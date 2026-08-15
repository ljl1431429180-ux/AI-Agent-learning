import json
import os



class ChatMemory:


    def __init__(self):


        # 当前文件目录

        base_dir = os.path.dirname(
            os.path.abspath(__file__)
        )


        self.memory_file = os.path.join(
            base_dir,
            "chat_memory.json"
        )


        self.messages = []


        self.load()






    # =========================
    # 加载历史聊天
    # =========================

    def load(self):


        if os.path.exists(
            self.memory_file
        ):


            try:

                with open(
                    self.memory_file,
                    "r",
                    encoding="utf-8"
                ) as f:


                    self.messages = json.load(f)



            except Exception:


                self.messages = []



        else:


            self.messages = []








    # =========================
    # 保存文件
    # =========================

    def save(self):


        with open(
            self.memory_file,
            "w",
            encoding="utf-8"
        ) as f:


            json.dump(
                self.messages,
                f,
                ensure_ascii=False,
                indent=2
            )








    # =========================
    # 添加单条消息
    # =========================

    def add_message(
        self,
        role,
        content
    ):


        self.messages.append(

            {

                "role": role,

                "content": content

            }

        )


        self.save()









    # =========================
    # 保存完整聊天
    # =========================

    def add_chat(
        self,
        user,
        assistant
    ):


        self.messages.append(

            {

                "role":"user",

                "content":user

            }

        )



        self.messages.append(

            {

                "role":"assistant",

                "content":assistant

            }

        )


        self.save()







    # =========================
    # 兼容 react_agent
    # =========================

    def save_memory(
        self,
        user,
        assistant
    ):


        self.add_chat(

            user,

            assistant

        )









    # =========================
    # 获取全部消息
    # =========================

    def get_messages(self):


        return self.messages







    # =========================
    # 获取历史
    # =========================

    def get_history(self):


        return self.messages







    # =========================
    # 获取最近消息
    # =========================

    def get_recent(
        self,
        limit=10
    ):


        return self.messages[-limit:]








    # =========================
    # 清空记忆
    # =========================

    def clear(self):


        self.messages = []


        self.save()