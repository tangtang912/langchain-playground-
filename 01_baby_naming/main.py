01_baby_naming/main.py
"""
LangChain 练习 01：零样本 (Zero-shot) 起名器
功能：通过通义千问，根据姓氏和性别生成名字
记忆口诀：模板 -> 模型 -> 链 -> 传参
"""
import os
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

# 从环境变量取 Key（必须在运行前设置好）
model = Tongyi(model="qwen-max")

# 定义模板
prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},你帮我起个名字，简单回答"
)

# 构建链
chain = prompt_template | model

# 执行并打印
if __name__ == "__main__":
    res = chain.invoke({"lastname": "张", "gender": "女儿"})
    print(res)
