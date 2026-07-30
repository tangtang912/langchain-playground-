"""
LangChain 练习 09：PDF 文件加载器 (PyPDFLoader)
功能：加载带密码保护的 PDF 文件，支持按页拆分或合并为单文档。
核心知识点：PyPDFLoader, mode="page" vs "single", password 参数, 元数据提取
"""

# 加载 PDF 文件（路径：回到上级目录，进入 data 文件夹）
from langchain_community.document_loaders import PDFLoader
loader=PDFLoader(
  fila_path="../data/大屁.pdf",
  mode="page",
  password="260730"
)

print("===== 开始逐页加载 PDF =====")
i=1
for doc in loader.lazy_load():
  i+=1
  print(doc)
  print（“=”*20，i）
