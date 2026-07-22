"""
LangChain 练习 03：对话模型与消息占位符 (Chat Model & MessagesPlaceholder)
功能：模拟带有历史记录的连续对话，让AI扮演“边塞诗人”连续作诗
核心知识点：ChatPromptTemplate, MessagesPlaceholder, ChatTongyi（区别于普通Tongyi）
"""

from langchain_core.prompts import ChatPromptTemplate,MessagePlacehoder
from langchain_community.chat_models.tongyi import ChatTongyi

chat_prompt_template=ChatPromptTemplate(
  [
    ("system":"你是一个边塞诗人")，
    MessagesPlaceholder("history")
   （"human":"写一首唐诗“）
  ]
    )

history_data=[
  ("human":"写一首唐诗"),
  ("ai":"锄禾日当午，汗滴禾下土。谁种盘中餐，粒粒皆辛苦。"),
  ("human":"好诗，再来一首"),
  ("ai":"床前明月光，疑是地上霜。举头望明月，低头思故乡。")
]

model = ChatTongyi(model="qwen3-max")
chain = chat_prompt_template|model
res = chain.invoke({"history":history_data})
print(res.content)

#或者
prompt_text=chat_prompt_template。invoke({"history":history_data}).to_string
print(prompt_text)
model = ChatTongyi(model="qwen3-max")
res = model.invoke(prompt_text)
print(res.content,type(res)
