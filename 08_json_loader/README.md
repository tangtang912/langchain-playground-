# JSON / JSON Lines 加载器 (JSONLoader) - 练习 08

本练习演示如何使用 `JSONLoader` 加载 JSON Lines 格式的数据，并使用 `jq_schema` 提取指定字段。

## 文件结构
- `main.py`：主程序
- `../data/stu_json_lines.json`：测试数据文件（位于仓库根目录的 data 文件夹）

## 核心知识点
- **jq_schema**：类似 JSONPath 的语法，用于从 JSON 中提取特定数据（例如 `.name` 提取所有 name 字段）。
- **json_lines=True**：表示每行是一个独立的 JSON 对象（JSON Lines 格式），而不是一个巨大的 JSON 数组。

## 运行
`python main.py`

## 预期输出
程序会打印出从数据中提取的每个文档对象，内容为 `"张三"`、`"李四"`、`"王五"`。
