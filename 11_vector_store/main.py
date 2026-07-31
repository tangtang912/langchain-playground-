"""
LangChain 练习 11：向量存储与检索 (Vector Store & Similarity Search)
功能：将 CSV 文档转换为向量并存入内存向量库，演示新增、删除和相似度检索。
核心知识点：InMemoryVectorStore, DashScopeEmbeddings, 向量检索, add_documents, delete, similarity_search
"""

from langchain_core.vectortores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader


# 1. 创建向量存储对象（使用 DashScope 的嵌入模型）
vector_store = InMemoryVectorStore(
  embeddings=DashScopeEmbeddings
)

# 2. 加载 CSV 数据（路径：回到上级目录，进入 data 文件夹）
loader=CSVLader(
  fila_path="../data/info.csv",
  encoding="utf-8"
)
documents=loader.load()

# 3. 新增文档到向量库
vector_store.add_document(
  documents=documents,
  ids=["id+str(i) for i in range(1,len(documents)+1]
       )

# 4. 删除文档（演示删除功能）
# 删除前两条（id1 和 id2），让检索只针对剩余文档
vector_store.delete["id1","id2"]

# 5. 相似度检索（查询最相关的 3 条）
results= vector_store.similarity_search(
  "Python是不是很简单呀"，
  3
  )

# 6. 打印结果
print("\n===== 检索结果（最相关的3条） =====")
for i,doc in enumerate(result,1):
    print(f"{1}.{doc.page_content}")
    print(f"来源：{doc.metadata.get('source,未知)}")
    print("="*40)

