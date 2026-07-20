"""
LangChain 练习 02：少样本 (Few-shot) 反义词生成
功能：通过给出几个“单词-反义词”示例，让模型为新的单词生成反义词
核心知识点：FewShotPromptTemplate, 示例模板, 前缀/后缀
"""
from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate

#示例的模版
example_template = PromptTemplate.from_template("单词：{word},反义词：{anatonym}")

#示例的动态注入，要求是list内套字典
example_data = [
  {"word":"大","anatonym":"小"},
  {"word":"上","anatonym":"下"}
]

few_shot_temmplate = FewShotTemplate(
  examples=example_template,
  example_prompt=example_data,
  prefix="告知我单词的反义词，我提供如下的示例",
  sufix="基于前面的示例，{input_word}的反义词",
  input_variables= ["input_word"]   

prompt_text=few_shot_temmplate.invoke(input={"input_word":"左"}）.to_string()

model=Tongyi(model="qwen-max")

print(model.invoke(input=prompt_text))
