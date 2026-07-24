"""
LangChain 练习 05：JSON解析器与流式传输 (JSON Parser & Streaming)
功能：
  1. 第一次调用：根据姓氏和性别生成名字，并要求模型以 JSON 格式返回。
  2. JsonOutputParser 将 JSON 字符串解析为 Python 字典（提取 name）。
  3. 第二次调用：将名字填入新提示词，让模型解析名字的含义。
  4. 使用 stream() 方法逐字打印最终结果，模拟"打字机效果"。

核心知识点：JsonOutputParser（结构化输出）, stream()（流式传输）, 链式多步骤调用
"""
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi

# 创建所需的解析器
json_parser = JsonOutputParser()
str_parser = StrOutputParser()

# 创建模型
model = ChatTongyi(model="qwen3-max")

# 第一个提示词模版
first_prompt = PromptTemplate.from_template(
    "我邻居姓{lastname},刚生了个{gender},请起名,"
    "并封装为JSON格式返回给我。要求key是name,value就是你起的名字，请严格遵守格式要求"
)

#第二个提示词模版
second_prompt = PromptTemplate.from_template(
    "姓名：{name},请帮我解析含义"
)

# 构建链
chain = first_prompt | model | json_parser | second_prompt | model | str_parser


for chunk in chain.stream({"lastname":"张","gender":"女"}):
    print(chunk,end="",flush=True)
