# Dify 集成截图说明

此目录包含 Dify 集成文档所需的截图。请按照以下说明准备截图：

## 配置方式说明

Dify 中配置 APIMart 有两种方式，截图需要覆盖两种方式：

**方式一（推荐）：** 使用 OpenAI 提供商的自定义 API 功能
**方式二：** 添加为自定义模型提供商

建议优先准备方式一的截图，因为这是推荐方式且更简单。

## 需要的截图列表

### 通用截图

### 1. `main-interface.png`
**描述：** Dify 主界面
- 显示 Dify 的主页面
- 包含应用列表、创建应用按钮
- 建议尺寸：1920x1080 或更高
- **使用位置：** 第一步 - 登录和主界面介绍

### 2. `settings-page.png`
**描述：** 设置页面入口
- 显示右上角头像菜单
- 突出显示"设置"选项
- 建议尺寸：1920x1080
- **使用位置：** 第一步 - 进入设置页面

### 3. `model-provider-menu.png`
**描述：** 模型提供商菜单
- 显示左侧菜单中的"模型提供商"选项
- 可以看到部分已配置的提供商
- 建议尺寸：1200x800
- **使用位置：** 第一步 - 导航到模型提供商设置

### 4. `openai-custom-api.png`（新增 - 推荐方式）
**描述：** OpenAI 自定义 API 配置
- 显示 OpenAI 提供商的设置页面
- 包含 API Key 和 Base URL 配置字段
- Base URL 填写 `https://api.apimart.ai/v1`
- 建议尺寸：1200x800
- **使用位置：** 第二步 - 方式一配置步骤 1-4（推荐）

### 4.5 `openai-custom-setting.png`（新增）
**描述：** OpenAI 自定义 API 配置界面（补充截图）
- 显示 OpenAI 提供商的配置详细界面或模型列表预览
- 可以是配置保存后的界面或设置面板的另一个视角
- 建议尺寸：1200x800
- **使用位置：** 第二步 - 方式一配置步骤 1-4（补充说明）

### 4.6 `openai-model-list.png`（新增 - 重要）
**描述：** OpenAI 模型列表和启用界面
- 显示 OpenAI 提供商的模型列表页面
- 包含多个模型（如 gpt-5, gpt-4.1, gpt-4o, gpt-4o-mini 等）
- 每个模型右侧有开关按钮（蓝色表示已启用）
- 显示模型类型标签（LLM, CHAT）和上下文长度（如 128K, 400K）
- 顶部显示 API KEY 和额度信息
- 右上角有"+ 添加模型"按钮
- 建议尺寸：1920x1080
- **使用位置：** 第二步 - 方式一配置步骤 5-7（启用模型）

### 5. `custom-model-section.png`
**描述：** 自定义模型部分（方式二）
- 显示模型提供商页面
- 向下滚动到"自定义模型"或"Custom Model"部分
- 显示"+ 添加模型"按钮
- 建议尺寸：1920x1080
- **使用位置：** 第二步 - 方式二添加自定义提供商入口

### 5. `add-provider-dialog.png`
**描述：** 添加模型对话框
- 显示"添加模型"配置对话框
- 包含以下字段：
  - 模型名称：填写 `APIMart` 或自定义名称
  - 模型类型：下拉选择（LLM、Rerank、Text Embedding、Speech2text、TTS）
  - API Key：填写 APIMart API 密钥
  - API endpoint URL：填写 `https://api.apimart.ai/v1`
  - API endpoint中的模型名称：填写具体模型名（如 `gpt-4o`）
- 建议尺寸：800x900
- **使用位置：** 第二步 - 配置 APIMart 提供商（方式二）

### 6. `add-model-form.png`
**描述：** 添加具体模型表单
- 显示添加模型的表单
- 包含模型 ID、模型名称、上下文长度等字段
- 可以展示添加 `gpt-4o` 的示例
- 建议尺寸：800x600
- **使用位置：** 第二步 - 添加具体模型

### 7. `model-list.png`
**描述：** 已添加的模型列表
- 显示 APIMart 提供商下已添加的多个模型
- 至少包含 2-3 个模型（gpt-4o, gpt-4o-mini, claude-sonnet-4-5 等）
- 建议尺寸：1200x800
- **使用位置：** 第二步 - 模型配置完成展示（方式二，可选）

### 8. `create-app.png`
**描述：** 创建应用页面
- 显示创建应用的入口
- 包含不同应用类型的选项（聊天助手、文本生成、Agent、工作流）
- 建议尺寸：1920x1080
- **使用位置：** 第三步 - 创建新应用

### 9. `app-orchestration.png`
**描述：** 应用编排页面
- 显示应用的编排界面
- 包含左侧工具栏、中间编辑区、右侧预览区
- 建议尺寸：1920x1080
- **使用位置：** 第三步 - 应用编排界面

### 10. `model-selection.png`
**描述：** 模型选择下拉菜单
- 显示模型选择下拉菜单展开状态
- 可以看到 APIMart 提供商和其下的模型列表
- 建议尺寸：800x600
- **使用位置：** 第三步 - 选择 APIMart 模型

### 11. `model-parameters.png`
**描述：** 模型参数配置
- 显示模型参数设置区域
- 包含 Temperature, Max Tokens, Top P 等参数滑块
- 建议尺寸：800x600
- **使用位置：** 第三步 - 配置模型参数

### 14. `prompt-editor.png`
**描述：** 提示词编辑器
- 显示系统提示词编辑区域
- 可以看到示例提示词和变量使用（如 `{{variable_name}}`）
- 建议尺寸：1200x800
- **使用位置：** 第四步 - 添加提示词

### 15. `knowledge-base.png`
**描述：** 知识库配置（可选）
- 显示知识库管理界面
- 可以看到上传文档、知识库列表等
- 建议尺寸：1200x800
- **使用位置：** 第四步 - 添加知识库

### 16. `app-preview.png`
**描述：** 应用预览和测试
- 显示右侧预览面板
- 包含测试对话的示例
- 显示用户输入和 AI 响应
- 建议尺寸：600x800
- **使用位置：** 第四步 - 测试应用

### 17. `publish-options.png`
**描述：** 发布应用选项
- 显示发布按钮和发布选项
- 包含 API 调用、嵌入网站、公开链接等选项
- 建议尺寸：800x600
- **使用位置：** 第四步 - 发布应用

### 18. `app-logs.png`
**描述：** 应用日志页面
- 显示应用的日志标签页
- 可以看到对话历史记录
- 建议尺寸：1920x1080
- **使用位置：** 第五步 - 查看应用日志

### 19. `workflow-example.png`（可选）
**描述：** 工作流示例
- 显示 Dify 的工作流编排界面
- 包含多个节点和连接线
- 建议尺寸：1920x1080
- **使用位置：** 高级功能 - 工作流编排

### 20. `chat-interface.png`
**描述：** 最终对话界面
- 显示完成配置后的实际对话界面
- 用户与 AI 的完整对话示例
- 建议尺寸：1200x800
- **使用位置：** 文档结尾 - 使用效果展示

## 截图要求

### 通用要求
- 所有截图应为 PNG 格式
- 保持界面整洁，关闭不必要的弹窗和通知
- 使用高分辨率（至少 1920x1080 for 全屏截图）
- 建议使用浅色主题（如果 Dify 支持）以保持一致性

### 隐私保护
- 隐藏或模糊真实的 API Key（可使用 `sk-xxxxxxxxxxxxxxxx` 示例）
- 隐藏个人邮箱、用户名等敏感信息
- 使用测试数据而非真实业务数据

### 标注建议
- 对于关键操作位置，可以使用红色框或箭头标注
- 保持标注风格一致
- 标注应清晰但不过于突兀

## 优先级

### 必需的截图（P0）
1. `main-interface.png`
2. `model-provider-menu.png`
3. `openai-custom-api.png`（新增 - 推荐方式）
4. `openai-model-list.png`（新增 - 重要）⭐
5. `add-provider-dialog.png`（方式二）
6. `model-selection.png`
7. `prompt-editor.png`
8. `app-preview.png`

### 推荐的截图（P1）
9. `settings-page.png`
10. `custom-model-section.png`
11. `add-model-form.png`
12. `model-list.png`
13. `create-app.png`
14. `app-orchestration.png`
15. `model-parameters.png`
16. `publish-options.png`
17. `app-logs.png`

### 可选的截图（P2）
18. `knowledge-base.png`
19. `workflow-example.png`
20. `chat-interface.png`

## 文件命名规范

- 使用小写字母和连字符（kebab-case）
- 文件名应简洁且描述性强
- 例如：`model-selection.png`, `api-config.png`

## 提交说明

截图完成后，请：
1. 将所有截图放入 `images/integrations/dify/` 目录
2. 确保文件名与文档中引用的名称一致
3. 检查图片大小，单张截图建议不超过 2MB
4. 如果图片较大，可以适当压缩（推荐使用 TinyPNG 等工具）

## 参考

可以参考其他集成文档的截图风格：
- `images/integrations/cursor/` - Cursor 集成截图
- `images/integrations/cherry-studio/` - Cherry Studio 集成截图
- `images/integrations/cline/` - Cline 集成截图

