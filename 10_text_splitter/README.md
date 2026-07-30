# 递归字符文本分割器 (RecursiveCharacterTextSplitter) - 练习 10

本练习演示如何使用 `RecursiveCharacterTextSplitter` 将长文本分割成适合 LLM 上下文窗口的块。

## 文件结构
- `main.py`：主程序
- `../data/Python基础语法手册.txt`：测试文本文件（位于仓库根目录的 data 文件夹）

## 核心知识点
- **chunk_size**：每个文本块的最大字符数（这里是 500）。
- **chunk_overlap**：块之间的重叠字符数（这里是 50），用于保持语义连贯性。
- **separators**：递归分割的优先级列表，先按段落 `\n\n` 切，再按句子标点切。
- **split_documents()**：将加载的 Document 列表拆分成更小的 Document 列表。

## 运行
`python main.py`

## 预期输出
打印原始文档数量（通常为 1），以及分割后的块数量，并预览前 3 个块的内容。
