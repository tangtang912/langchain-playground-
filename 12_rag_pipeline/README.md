# 完整 RAG 管道 (Retrieval-Augmented Generation) - 练习 12

本练习演示了一个**完整的 RAG 链路**：用户提问 → 向量检索 → 拼接参考资料 → LLM 生成回答。

## 核心知识点
- **RAG 完整流程**：检索 + 增强 + 生成
- **InMemoryVectorStore**：内存向量库存储知识
- **similarity_search**：基于语义相似度检索相关文档
- **ChatPromptTemplate**：将检索结果动态拼入 System Prompt
- **LCEL 链式调用**：`prompt | model | parser`

## 运行
`python main.py`

## 预期效果
模型会基于向量库中 3 条健康知识，生成关于“怎么减肥”的简洁专业回答。
