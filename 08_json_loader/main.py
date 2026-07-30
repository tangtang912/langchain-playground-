"""
LangChain 练习 08：JSON / JSON Lines 文件加载器 (JSONLoader)
功能：使用 JSONLoader 加载本地的 stu_json_lines.json 数据，
     并通过 jq_schema 提取每个 JSON 对象中的 "name" 字段。
核心知识点：JSONLoader, jq_schema 语法, json_lines 参数
"""

from langchain_community.document_loaders import JSONLoader

loader=JSONLoader(
  file_path="../data/stu_json_lines.json",
  jq_schema=".name",
  text_content=False,
  json_lines=True
  ）

documents=load.loader()
print("===== 加载的文档 =====")
for doc in documents:
  print(doc)
