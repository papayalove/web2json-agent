"""
视觉理解 Prompt 模板
用于从网页截图提取结构化信息
"""


class VisualUnderstandingPrompts:
    """视觉理解 Prompt 模板类"""

    @staticmethod
    def _get_base_prompt() -> str:
        """
        获取基础 Prompt（两个任务共用的部分）

        Returns:
            基础 Prompt 字符串
        """
        return """你是一个专业的数据模型专家，擅长根据网页布局分析和设计JSON Schema。

## 核心原则

**仅对网页中的有价值正文信息进行Schema建模**，包括但不限于：
- 文章标题、文章作者、作者信息、发布时间
- 文章摘要、完整的正文内容（视为一个整体）
- 评论区
- 其他核心内容元素

## 明确排除

请忽略以下非核心元素：
- 广告、侧边栏、推荐位、导航栏
- 页眉、页脚、相关推荐
- 任何网站通用组件

## 关键要求

1. **将文章正文视为单一整体**，不要将其分割为摘要、段落等子部分
2. 仔细分析网页布局结构，识别核心内容区域
3. 对每个字段提供自然语言描述的视觉特征，帮助后续从HTML中定位该元素

## 输出格式

请严格按照以下JSON格式输出：

```json
{
  "title": {
    "type": "string",
    "description": "文章标题",
    "visual_features": "位于页面上部中央区域，字体非常大且加粗，颜色为深色，是页面中最显眼的文本元素，通常独占一行",
    "importance_score": 1.0
  },
  "author": {
    "type": "string",
    "description": "作者姓名",
    "visual_features": "位于标题正下方偏左的位置，字体较小，颜色为灰色，旁边可能有作者头像或图标装饰",
    "importance_score": 0.9
  },
  "publish_time": {
    "type": "string",
    "description": "发布时间",
    "visual_features": "位于标题下方，通常在作者信息旁边或右侧，字体较小，颜色为灰色，可能包含时间图标",
    "importance_score": 0.9
  },
  "content": {
    "type": "string",
    "description": "文章正文内容（完整内容）",
    "visual_features": "位于页面中心主要内容区域，占据页面主体部分，字体为常规大小，颜色为深色，行距适中，通常以段落形式组织",
    "importance_score": 1.0
  },
  // 其他字段
}
```

## 字段说明

- **type**: 数据类型（string, number, array, object等）
- **description**: 字段的语义描述
- **visual_features**: 用自然语言描述该元素的视觉特征，包括：
  - 在页面中的大致位置
  - 字体大小、粗细、颜色
  - 周围是否有图标、边框、背景色等装饰
  - 与其他元素的相对位置关系
  - 任何有助于定位该元素的视觉线索
- **importance_score**: 该元素与文章主题的相关程度（0.0-1.0）
  - 1.0: 核心内容（如标题、正文）
  - 0.8-0.9: 重要元数据（如作者、发布时间、摘要）
  - 0.5-0.7: 次要信息（如标签、分类、阅读量）
  - 0.0-0.4: 可选信息（如评论数、点赞数、分享按钮）

## 注意事项

- visual_features 应该足够详细，让开发者能够根据描述在HTML中准确定位到该元素
- 描述应该关注视觉特征而非具体的HTML标签或CSS类名
- description 和 visual_features 中只描述通用特征，不要包含具体页面的实际内容
- 如果某个字段在截图中不存在，可以不包含在输出中"""

    @staticmethod
    def get_extraction_prompt() -> str:
        """
        获取结构化信息提取 Prompt（首次生成）

        Returns:
            Prompt 字符串
        """
        base_prompt = VisualUnderstandingPrompts._get_base_prompt()
        return f"""{base_prompt}

请基于网页截图，识别核心内容区域并生成完整的Schema。
"""

    @staticmethod
    def get_schema_refinement_prompt(previous_schema: dict) -> str:
        """
        获取Schema迭代优化Prompt（后续迭代）

        Args:
            previous_schema: 上一轮的Schema

        Returns:
            Prompt字符串
        """
        import json
        schema_str = json.dumps(previous_schema, ensure_ascii=False, indent=2)
        base_prompt = VisualUnderstandingPrompts._get_base_prompt()

        return f"""## 当前任务

基于新的网页截图，对已有的JSON Schema进行优化和完善。

## 当前Schema

```json
{schema_str}
```

{base_prompt}

## 迭代优化要求

1. **保留所有已有字段**：当前Schema中的所有字段必须完整保留，**不得修改或删除**
2. **仅添加新字段**：如果新截图中发现当前Schema未覆盖的核心字段（除prompt中明确排除的元素外），添加到Schema中
3. **为新字段评分**：对每个新添加的字段标记importance_score（0.0-1.0），表示该元素与文章主题的相关程度
4. **输出完整Schema**：请输出优化后的**完整Schema**（包含所有旧字段和新字段）

**重要原则**：
- 获取除prompt中明确排除的元素（广告、侧边栏、导航栏等）外的所有页面元素
- 仅在原有基础上增加新字段，不修改已有字段
- 每个字段都必须有importance_score字段

请基于新的网页截图，输出优化后的完整Schema。
"""

    @staticmethod
    def get_system_message() -> str:
        """获取系统消息"""
        return "你是一个专业的网页截图分析助手，擅长识别网页中的结构化信息。"
