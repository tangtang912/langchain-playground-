# RunnablePassthrough 与 as_retriever - 练习 13

本练习展示 LangChain LCEL 中的**分支数据流**模式，用 `as_retriever()` 将向量库包装为 Runnable。

## 核心知识点

### `as_retriever()`
- 将 `InMemoryVectorStore`（非 Runnable）转换为标准的 `Retriever`（Runnable 子类）
- 自动处理向量检索逻辑，统一输入输出接口

### `RunnablePassthrough`
- 在 LCEL 链中"透传"数据，不做任何转换
- 常用于构建字典的某个字段值，让其他分支（如检索）并行处理

### 数据流图解
