from graph import agent



state = {

"user_input":"我喜欢胡桃木,预算4000",

"requirement": {},

"product": {},

"stock":0,

"knowledge":"",

"answer":"",

"memory": {},

"user_profile": {},

"logs":[]

}

result = agent.invoke(state)
print("\n===== Agent运行日志 =====")

for log in result["logs"]:
    print(log)


print("\n===== 最终回答 =====")

print(result["answer"])

