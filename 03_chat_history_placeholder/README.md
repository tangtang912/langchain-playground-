# 对话历史与占位符

本练习展示如何使用 `ChatPromptTemplate` 配合 `MessagesPlaceholder` 来管理多轮对话历史。

## 关键区别（复习重点）
- `Tongyi`（之前用的）：用于文本补全，输入输出都是纯字符串。
- `ChatTongyi`（现在用的）：用于对话模型，输入输出都是消息对象（Message），内容在 `.content` 里。

## 运行
`python main.py`

## 预期效果
模型会基于之前已有的两首诗，再续写一首新的唐诗。
