# 链式调用与输出解析器

本练习重点展示 LCEL（LangChain 表达式语言）的链式调用，以及 `StrOutputParser` 的作用。

## ⚠️ 重要结论
- `StrOutputParser` 会把模型的 `AIMessage` 对象“剥开”，只提取纯文本 `.content`。
- 如果链的末尾是 `| parser`，那么 `chain.invoke()` 返回的是 `str`，而不是 `AIMessage`。

## 代码亮点
连续调用了两次模型，实现了“AI 自我精炼”的初级形态。

## 运行
`python main.py`
