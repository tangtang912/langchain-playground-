"""
LangChain 练习 04：链式调用与输出解析器 (Chain & Output Parser)
功能：连续调用两次模型，第一次起名，第二次对名字进行"自我精炼"或追加解释
核心知识点：LCEL 链式调用（|）, StrOutputParser（将AI消息转为字符串）
关键注意：链末尾加了 parser，最终返回的是 str，而不是 AIMessage！
"""

from langchain.core.output_parsers import StrOutputParser
from langchain.core.prompts import PromptTemplate
from langchain.community.chat_models.tongyi import ChatTongyi
from langchain.core.messages import AIMessages

parser = StrOutputParser()
model = ChatTongyi(model = "qwen3-max")
prompt = PromptTemplate.from_template(
  "我邻居姓{lastname},刚生了个{gender},请起名,简短回答"
)
chain = response:AIMessage = chain.invoke(input={"lastname": "张", "gender": "女"})
print(response)
