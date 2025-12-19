# web2json-agent

**让 AI 自动生成网页解析代码，告别手写 XPath 和 CSS 选择器**

## 💡 项目简介

**web2json-agent** 是一个基于 AI 的智能代码生成工具，能够**自动分析网页结构并生成高质量的 Python 解析代码**。

### ✨ 核心价值

传统方式开发网页解析器，你需要：
- ❌ 手动分析 HTML 结构，费时费力
- ❌ 逐个编写 XPath 或 CSS 选择器，容易出错
- ❌ 反复调试选择器，适配不同页面结构
- ❌ 处理数据结构和类型转换的繁琐代码

使用 **web2json-agent**，你只需要：
- ✅ 提供 2-5 个示例 HTML 文件
- ✅ 等待 1-2 分钟
- ✅ 获得可直接使用的解析器代码

**节省 80% 的开发时间，从几小时到几分钟！**

### 🎯 核心亮点

1. **🤖 完全自动化** - 无需手写 XPath、CSS 选择器或解析逻辑
2. **👁️ 多模态分析** - 结合 HTML 代码分析和视觉理解，提取更准确
3. **🛡️ 高鲁棒性** - 自动生成多个备选提取路径，适应页面结构变化
4. **📦 开箱即用** - 生成的代码可直接运行，支持 CLI 和 Python 导入
5. **🔄 智能优化** - 自动去除广告、导航等无效字段，优化数据结构

### 📋 示例

**输入：26 万字符的杂乱 HTML**（深度嵌套、无意义 class、大量广告和噪音）
```html
<html class="itcauecng idc0_347">
<head>
  <title>海南自贸港12月18日即将封关，「零关税」和「双15%」个税优惠政策...</title>
  <!-- ...省略 50+ 个 meta/link/script 标签... -->
</head>
<body>
  <div id="root" class="_2Jysd8SG _3kRqKz4Q">
    <div class="GlobalSideBar _1mQ9vkP3">...</div>  <!-- 导航栏 -->
    <div class="TopBar _2pWmP1eX">...</div>          <!-- 搜索框 -->

    <main>
      <!-- 问题标题buried在 5 层 div 嵌套中 -->
      <div class="QuestionHeader">
        <div class="QuestionHeader-content">
          <div class="QuestionHeader-main">
            <h1 class="QuestionHeader-title">海南自贸港12月18日即将封关...</h1>
            <div class="QuestionRichText--collapsed">
              <div class="RichText">
                <span>12月18日，海南自由贸易港将正式启动...</span>
      <!-- ...6 层嵌套... -->
              </div></div></div></div></div>

      <!-- 回答列表，每个回答有 5+ 层嵌套 -->
      <div class="List-list">
        <div class="List-item">
          <div class="ContentItem AnswerItem">
            <div class="ContentItem-main">
              <div class="RichContent">
                <div class="AuthorInfo-name">Saka财经</div>
                <div class="AuthorInfo-badge">CPA 注册会计师资格证持证人</div>
                <span class="RichText">海南这次一定要接住这个橄榄枝...</span>
      <!-- ...更多嵌套... -->
              </div></div></div></div>
        <!-- ...省略其他 53 个回答... -->
      </div>

      <aside>
        <div class="AdCard">...</div>  <!-- 广告 -->
        <div class="AdCard">...</div>  <!-- 广告 -->
      </aside>
    </main>
  </div>
  <script>window.__INITIAL_STATE__={"entities":{...}}</script>  <!-- 数万字符 -->
</body>
</html>
```

**输出：干净的结构化 JSON**（AI 自动识别核心内容，过滤噪音）
```json
{
  "title": "海南自贸港12月18日即将封关，「零关税」和「双15%」个税优惠政策将有什么变化？...",
  "question_author": "每日经济新闻",
  "question_author_badge": "已认证机构号",
  "question_description": "12月18日，海南自由贸易港将正式启动全岛封关运作...",
  "topics": ["投资", "商业", "股票", "海南", "海纳百川开放共赢"],
  "view_count": "183,426",
  "answer_count": "54 个回答",
  "answers": [
    {
      "author": "Saka财经",
      "author_badge": "CPA 注册会计师资格证持证人",
      "content": "海南这次一定要接住这个橄榄枝，飞速发展的机会...",
      "publish_time": "编辑于 2025-12-16 15:42"
    },
    {
      "author": "闻号说经济",
      "author_badge": "CFA 注册金融分析师资格证持证人",
      "content": "2025年12月18日，海南自贸港将正式启动全岛封关运作...",
      "publish_time": "发布于 2025-12-16 12:31"
    },
    {
      "other": "其他回答省略"
    }
  ]
}
```

✨ **自动识别并提取**：标题、作者、话题标签、统计数据、**回答列表**（包含嵌套的作者信息、内容、时间等）

### 🚀 适用场景

- **批量爬虫开发** - 快速为博客、产品页、新闻等同类型页面生成解析器
- **数据采集项目** - 减少手动编写解析器的重复劳动
- **原型验证** - 快速验证数据提取可行性，再优化细节
- **学习参考** - 生成的代码可作为学习 BeautifulSoup 和 XPath 的参考示例

### 🔧 工作流程

```
提供示例HTML → AI自动分析 → 生成解析器代码
    (2-5个)      (1-2分钟)      (可直接使用)
```

**内部流程**：双重分析（HTML + 视觉）→ Schema 提取 → 智能合并 → 代码生成

---

## 🚀 快速开始

选择以下任一方式开始使用：

### 方式 1：通过 pip 安装（推荐）

适合**直接使用**工具的用户

```bash
# 1. 安装包
pip install web2json-agent

# 2. 初始化配置
web2json setup  # 交互式配置（推荐）
# 或手动配置：web2json init && vim .env

# 3. 准备HTML文件并生成解析器
mkdir html_samples  # 放入 2-5 个同类型HTML文件
web2json -d html_samples/ -o output/blog

# 4. 使用生成的解析器
python output/blog/final_parser.py example.html              # 解析HTML文件
python output/blog/final_parser.py https://example.com       # 解析URL
```

---

### 方式 2：克隆仓库开发

适合**开发者**和**贡献者**

```bash
# 1. 克隆项目并安装依赖
git clone https://github.com/ccprocessor/web2json-agent.git
cd web2json-agent
pip install -r requirements.txt

# 2. 配置 API 密钥
cp .env.example .env
vim .env  # 填入 OPENAI_API_KEY 和 OPENAI_API_BASE

# 3. 生成解析器（html_samples/ 目录已有示例）
python main.py -d html_samples/ -o output/blog

# 4. 使用生成的解析器
python output/blog/final_parser.py example.html              # 解析HTML文件
python output/blog/final_parser.py https://example.com       # 解析URL
```

---

## 💡 使用技巧

- **HTML 文件数量**：输入 2-5 个同类型页面即可得到比较好的解析效果
- **查看中间结果**：生成过程中的 Schema 和截图都保存在 `output/` 目录中
- **调整模型配置**：Schema 生成/代码生成阶段使用的模型可以在 `.env` 中修改

---

## 📁 项目结构

```
web2json-agent/
├── agent/                  # Agent 核心模块
│   ├── planner.py         # 任务规划
│   ├── executor.py        # 任务执行（含Schema迭代逻辑）
│   └── orchestrator.py    # Agent 编排
│
├── tools/                  # LangChain Tools
│   ├── webpage_source.py          # 读取本地HTML文件
│   ├── webpage_screenshot.py      # 截图（DrissionPage）
│   ├── schema_extraction.py       # Schema提取和合并
│   ├── html_simplifier.py         # HTML精简工具
│   └── code_generator.py          # 代码生成
│
├── prompts/                # Prompt 模板
│   ├── schema_extraction.py       # Schema提取Prompt（HTML+视觉）
│   ├── schema_merge.py            # Schema合并Prompt
│   └── code_generator.py          # 代码生成Prompt
│
├── config/                 # 配置
│   └── settings.py
│
├── utils/                  # 工具类
│   └── llm_client.py      # LLM 客户端
│
├── output/                 # 输出目录
│   └── [domain]/
│       ├── screenshots/       # 网页截图
│       ├── html_original/     # 原始HTML
│       ├── html_simplified/   # 精简HTML
│       ├── schemas/           # Schema文件
│       │   ├── html_schema_round_{N}.json     # HTML提取的Schema
│       │   ├── visual_schema_round_{N}.json   # 视觉提取的Schema
│       │   ├── merged_schema_round_{N}.json   # 合并后的Schema
│       │   └── final_schema.json              # 最终Schema
│       ├── parsers/           # 生成的解析器
│       │   └── parser_round_{N}.py            # 每轮生成的解析器
│       ├── result/            # 解析结果JSON
│       └── final_parser.py    # 最终解析器（可直接运行）
│
├── main.py                # 命令行入口
└── requirements.txt       # 依赖列表
```

---

## 📋 Schema格式说明

### 最终Schema结构

生成的`final_schema.json`包含每个字段的完整信息：

```json
{
  "title": {
    "type": "string",
    "description": "文章标题",
    "value_sample": "关于人工智能的未来",
    "xpaths": [
      "//h1[@class='article-title']/text()",
      "//div[@class='title']/text()"
    ],
    "visual_features": "位于页面上部中央区域，字体非常大且加粗，颜色为深色..."
  },
  "comments": {
    "type": "array",
    "description": "评论列表",
    "value_sample": [{"user": "用户A", "text": "评论内容"}],
    "xpaths": [
      "//div[@class='comment-list']//div[@class='comment']",
      "//ul[@class='comments']//li"
    ],
    "visual_features": "位于正文下方，多个评论项垂直排列..."
  }
}
```

### 字段说明

- **type**: 数据类型（string, number, array, object等）
- **description**: 字段的语义描述
- **value_sample**: 实际值示例（字符串截取前50字符）
- **xpaths**: 数组形式，包含多个可用的xpath提取路径（增强鲁棒性）
- **visual_features**: 视觉特征描述，包括位置、字体、颜色、布局等

---

## 📤 返回值说明

`generate_parser()` 返回：

```python
{
    'success': bool,              # 是否成功
    'plan': dict,                 # 执行计划
    'execution_result': dict,     # 执行结果（包含两阶段迭代详情）
    'summary': str,               # 执行总结
    'parser_path': str,           # 解析器路径
    'config_path': str            # 配置文件路径
}
```

---

## 📄 许可证

MIT License

---

**最后更新**: 2025-12-18
**版本**: 1.0.2