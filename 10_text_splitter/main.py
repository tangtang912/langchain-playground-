
"""
LangChain 练习 10：递归字符文本分割器 (RecursiveCharacterTextSplitter)
功能：加载较大的文本文件，并使用递归字符分割器将其拆分为语义块。
核心知识点：TextLoader, RecursiveCharacterTextSplitter, chunk_size, chunk_overlap, 自定义分隔符
"""

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. 加载文本（路径：回到上级目录，进入 data 文件夹）
loader=TextLoader("../data/Python基础语法手册.txt", encoding="utf-8"）
docs=loader.load()
print(docs)
print(len(docs))

# 2. 创建分割器
splitter=RecursiveCharacterTextSplitter（
  chunk_size=500,
  chunk_overlap=50,
  separators=["\n\n", "\n", "。", "，", "！", "？", ".", "!", "?", " ", ""],
  length_function=len
)

split_docs=splitter.split_documents(docs)
print(len(split_docs))
for doc in split_docs:
    print("="*20)
    print(doc)
    print("="*20)
