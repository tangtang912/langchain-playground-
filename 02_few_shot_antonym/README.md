02_few_shot_antonym/README.md
# 少样本反义词生成

本练习演示如何使用 `FewShotPromptTemplate` 给模型提供示例，让其学会“反义词”任务。

## 运行
`python main.py`

## 预期输出
模型会根据“大→小、上→下”的示例，推理出“左”的反义词（很可能是“右”）。
