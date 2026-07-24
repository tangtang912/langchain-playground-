# 自定义函数注入 (RunnableLambda)

本练习展示如何使用 `RunnableLambda` 在 LCEL 链中嵌入任意 Python 函数。

## 核心概念对比
- **JsonOutputParser（练习05）**：自动解析 JSON 字符串。
- **RunnableLambda（练习06）**：手动编写函数，自由处理任意格式的数据。

## 链式逻辑
1. 模型生成名字（纯文本，如“张薇”）
2. `RunnableLambda` 将名字手动包装成 `{"name": "张薇"}`
3. 第二个提示词接收字典，继续让模型解析含义

## 运行
`python main.py`
