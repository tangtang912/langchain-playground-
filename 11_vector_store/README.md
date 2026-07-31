# 向量存储与检索 (Vector Store) - 练习 11

本练习演示如何使用 `InMemoryVectorStore` 将文档向量化，并进行相似度检索。

## 文件结构
- `main.py`：主程序
- `../data/info.csv`：测试数据文件（位于仓库根目录的 data 文件夹）

## 核心知识点
- **InMemoryVectorStore**：内存向量库，适合小规模数据测试。
- **DashScopeEmbeddings**：阿里云通义的嵌入模型，将文本转换为向量。
- **add_documents()**：批量添加文档并指定 ID。
- **delete()**：按 ID 删除文档。
- **similarity_search()**：向量相似度检索，返回最相关的 k 条文档。

## 运行
`python main.py`

## 注意
`DashScopeEmbeddings` 需要设置 `DASHSCOPE_API_KEY` 环境变量（与通义千问共用一个 Key）。
