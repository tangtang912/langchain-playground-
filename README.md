# 🧪 LangChain 学习沙盒

存放我学习 LangChain 期间的所有零散练习。

## 📂 项目列表

| 文件夹 | 说明 | 核心知识点 |
| :--- | :--- | :--- |
| [01_baby_naming](./01_baby_naming) | 根据姓氏和性别起名 | PromptTemplate, LCEL |
| [02_few_shot_antonym](./02_few_shot_antonym) | 少样本反义词生成 | FewShotPromptTemplate, 示例模板 |
| [03_chat_history_placeholder](./03_chat_history_placeholder) | 带历史记录的对话作诗 | ChatPromptTemplate, MessagesPlaceholder, ChatTongyi |
| [04_chain_with_parser](./04_chain_with_parser) | 链式调用与输出解析器 | LCEL管道符, StrOutputParser, 多模型串联 |
| [05_json_parser_and_stream](./05_json_parser_and_stream) | JSON解析与流式传输 | JsonOutputParser, stream(), 多步骤链 |
| [06_runnable_lambda](./06_runnable_lambda) | 自定义函数注入链 | RunnableLambda, 自定义逻辑 |
| [07_csv_loader](./07_csv_loader) | CSV 数据加载与解析 | CSVLoader, 懒加载迭代器 |
| [08_json_loader](./08_json_loader) | JSON / JSON Lines 数据加载 | `JSONLoader`, `jq_schema`, `json_lines` |
| [09_pdf_loader](./09_pdf_loader) | PDF 文档加载（含密码） | `PyPDFLoader`, `mode="page"/"single"`, 密码保护 |
| [10_text_splitter](./10_text_splitter) | 长文本递归分割 | `RecursiveCharacterTextSplitter`, `chunk_size`, `chunk_overlap` |
| [11_vector_store](./11_vector_store) | 向量存储与相似度检索 | InMemoryVectorStore, DashScopeEmbeddings, add/delete/search |
| [11_chroma_store](./11_chroma_store) | Chroma 持久化向量库 | Chroma, 持久化存储, 元数据过滤 |
| [12_rag_pipeline](./12_rag_pipeline) | 完整 RAG 检索增强生成 | 向量检索 + 提示词拼接 + LLM 生成 |
| [13_rag_passthrough_retriever](./13_rag_passthrough_retriever) | LCEL 分支数据流 | RunnablePassthrough, as_retriever, 标准RAG链 |
## 🔧 如何运行

1.  复制 `.env.example` 为 `.env` 并填入你的 API Key。
2.  进入对应文件夹，查看 `main.py`。
