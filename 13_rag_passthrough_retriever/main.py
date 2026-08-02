"""
LangChain 练习 13：RunnablePassthrough 与 as_retriever
功能：使用 as_retriever() 将向量库转换为 Runnable 接口，
     使用 RunnablePassthrough 透传用户输入，构建标准 LCEL 链。
核心知识点：as_retriever, RunnablePassthrough, LCEL 分支数据流
"""

from langchain_core.chat_models import ChatTongyi
from langchain_community.prompt import ChatPromotTemplate
from langchain_core.vectorstores import InMemoryVectorstore
from langchain_core.runnables import RunnablePassthrough
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.output_parsers import StrOutputParser

# 1. 初始化组件
model=ChatTongyi(model="qwen3-max")
vector_stores=InMemoryVectorstore(
  embeddings=DashScopeEmbedings(model="text-embedding=v4")
)

# 2. 准备提示词模板
prompt=ChatPromptTemplate(
  [
    ("system":", "以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料：{content}。"),
    ("user","用户提问:{input}")
  ]
  )
    
# 3. 准备向量库数据
vector_store.add_texts(
  [
  "减肥就是要少吃多练",
        "在减肥期间吃东西很重要，清淡少油控制卡路里摄入并运动起来",
        "跑步时很好的运动哦"
  ]
  )
input_text="怎么减肥？"

# 4. 将向量库转换为 Retriever（Runnable 接口）
retriever=vector_store.as_retriever(search_kwargs={k:2})

# 5. 格式化检索结果的函数
def format_func(docs):
    if not docs:
        return "无相关参考资料"

formatted_str = "["
for doc in docs:
  formatted_str += doc.page_content
formatted_str += "]"
return formatted_str
  
# 6. 构建 LCEL 链（重点理解数据流）
chain = {"input":RunnablePassthrough(),"content":retriever|format_func} | prompt | model |StrOutputParser()

# 7. 执行
res=chain.invoke(input_text)
