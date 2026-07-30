# PDF 文件加载器 (PyPDFLoader) - 练习 09

本练习演示如何使用 `PyPDFLoader` 加载带密码保护的 PDF 文件。

## 文件结构
- `main.py`：主程序
- `../data/大屁.pdf`：测试 PDF 文件（位于仓库根目录的 data 文件夹）

## 核心知识点
- **password 参数**：支持加载加密的 PDF 文件。
- **mode="page"**（默认）：每一页生成一个独立的 Document 对象，元数据中包含页码。
- **mode="single"**：将整个 PDF 合并为一个 Document 对象。
- **lazy_load()**：懒加载，逐页读取，内存友好。

## 运行
`python main.py`

## 注意事项
PDF 文件有密码保护，代码中已硬编码密码 `960912`（实际项目中建议从环境变量读取）。
