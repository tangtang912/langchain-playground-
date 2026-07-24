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
## 🔧 如何运行

1.  复制 `.env.example` 为 `.env` 并填入你的 API Key。
2.  进入对应文件夹，查看 `main.py`。
