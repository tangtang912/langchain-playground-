"""
LangChain 练习 07：CSV 文档加载器 (CSVLoader)
功能：使用 CSVLoader 加载本地的 stu.csv 数据，并逐条打印文档对象。
核心知识点：CSVLoader, load() 批量加载, lazy_load() 懒加载（迭代器）
注意：运行本代码需要同级目录下的 data/stu.csv 文件存在。
"""

from langchain_community.document_loaders import CSV.loader
loader.CSVload(
  file_path="../data/stu.csv",
  csv_args ={
    "delimiter":",",
    "quoterchar":'"'
  },
  encoding="utf-8"
)

#批量加载.load()
documents =loader.load()
for document in documents:
  print(document)
  
#懒加载.lazy_load()
print("===== 使用懒加载逐条打印 =====")
for ducument in loader.lazy_load():
    print(document)
