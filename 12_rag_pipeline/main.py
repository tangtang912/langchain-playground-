"""
LangChain 练习 12：完整的 RAG 管道 (Retrieval-Augmented Generation)
功能：用户提问 → 向量检索 → 组装提示词 → LLM 生成回答（基于参考资料）
核心知识点：RAG 完整链路, InMemoryVectorStore, similarity_search, ChatPromptTemplate, LCEL
"""

from langchain_core.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.vector_stores import InMemoryVectorStore
from langchain_core.output_parsers import StrOutputParse

# 1. 初始化组件
model=ChatTongyi(model="qwen3-max")
vector_store=InMemoryVectorStore(
  embedding=DashScopeEmbeddings(model="text-embedding-v4
                               )

# 2. 准备提示词模板（system 中包含参考资料占位符）
prompt=ChatPromptTemplate(
  [
    ("system": "以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料：\n{content}。"),
    ("user", "用户提问：{input}")
  ]
)

# 3. 准备向量库数据（直接添加文本）
vector_store.add_texts=(
      [
        "减肥就是要少吃多练",
        "在减肥期间吃东西很重要，清淡少油控制卡路里摄入并运动起来",
        "跑步是很好的运动哦"
    ]
)

# 4. 用户提问
input_text = "怎么减肥？"

# 5. 向量检索（相似度搜索，返回最相关的 2 条）
result=vector_store.similarity_search(input_text,k=2)

# 6. 组装参考资料（用序号和换行拼接，清晰易读）
reference_text="[
for doc in result:
  reference+= doc.page_content
reference_text+=]"
print(reference_text)

# 7. 调试函数：打印最终提示词内容（用于学习验证）
del print_prompt(prompt):
  print(prompt.to_string())
  print("="*20)
  return prompt

# 8. 构建完整链（检索 → 组装 → 打印 → 模型 → 解析）
chain = prompt|print_prompt|model|StrOutParser

  
# 9. 执行
res=chain.invoke({"input":input_text,"content":reference_text})
print(res)
