# CSV 文档加载器 (CSVLoader) - 练习 07

本练习演示如何使用 LangChain 的 `CSVLoader` 加载本地 CSV 文件。

## 文件结构
- `main.py`：主程序
- `../data/stu.csv`：测试数据文件（位于仓库根目录的 data 文件夹）

## 核心知识点
- **load()**：一次性将所有行加载为 Document 列表。
- **lazy_load()**：返回迭代器，按需逐条读取，适合大文件。

## 运行
`python main.py`
