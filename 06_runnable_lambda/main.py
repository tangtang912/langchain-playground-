"""
LangChain 练习 06：自定义函数注入 (RunnableLambda)
功能：使用 RunnableLambda 在链中嵌入自定义 Python 函数，
     手动将第一次模型输出的名字包装成字典，供下游提示词使用。
核心知识点：RunnableLambda（自定义逻辑）, LCEL 链式调用
"""
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableLambda

# 组件初始化
parser = StrOutputParser()
model = ChatTongyi(model="qwen-max")

# 第一个提示词：让模型直接输出简短名字（纯文本）
first_prompt = PromptTemplate.from_template(
    "我邻居姓{lastname},刚生了个{gender},请起名,简短回答"
)

# 第二个提示词：接收名字并解析含义
second_prompt = PromptTemplate.from_template(
    "姓名：{name},请帮我解析含义"
)

# 自定义函数：将 AI 的回复（纯文本名字）包装成字典
# 入参是 AIMessage，出参是 dict，符合下游 PromptTemplate 的预期
my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})

# 构建链：起名 -> 手动包装成字典 -> 解析含义 -> 输出纯文本
chain = first_prompt | model | my_func | second_prompt | model | parser

# 流式打印结果
for chunk in chain.stream({"lastname": "张", "gender": "女"}):
    print(chunk, end="", flush=True)
