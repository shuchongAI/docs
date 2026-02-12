# 可灵（Kling）视频生成 API 参数文档

## 接口地址

| 功能 | 方法 | 路径 |
|------|------|------|
| 提交视频生成任务 | POST | `/v1/videos/generations` |
| 查询任务状态 | GET | `/v1/tasks/{task_id}` |

---

## 支持模型

| 模型名称 | 说明 |
|----------|------|
| `kling-v2-6` | 可灵 v2.6（推荐） |

---

## 请求参数

### 基础参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `model` | string | 是 | - | 模型名称，如 `kling-v2-6` |
| `prompt` | string | 是 | - | 生成提示词 |
| `mode` | string | 否 | `std` | 生成模式：`std`（标准，720P，仅无声视频）/ `pro`（专业，1080P） |
| `duration` | int | 否 | `5` | 视频时长（秒）：`5` 或 `10` |
| `aspect_ratio` | string | 否 | `16:9` | 宽高比：`16:9` / `9:16` / `1:1` |
| `negative_prompt` | string | 否 | - | 负面提示词（排除不想要的内容） |

### 图像输入参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `image_urls` | string[] | 否 | 图片 URL 数组，**最多 2 张**。传 1 张作为首帧；传 2 张自动分配首帧 + 尾帧。首尾帧需 `mode: "pro"` |

### 音频参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `audio` | bool | 否 | `false` | 是否自动生成音频（需 `mode: "pro"`） |
| `voice_list` | array | 否 | - | 音色列表，格式 `[{"voice_id":"xxx"}]`，最多 2 个（需 `mode: "pro"` + `audio: true`） |

#### 查询可用音色列表

通过以下接口查询可灵支持的预设音色 ID：

| 功能 | 方法 | 路径 |
|------|------|------|
| 查询预设音色 | GET | `/v1/kling/general/presets-voices` |

**Query 参数**：

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `pageNum` | int | 否 | 1 | 页码 |
| `pageSize` | int | 否 | 10 | 每页条数 |

**请求示例**：

```bash
curl -X GET 'https://api.apimart.ai/v1/kling/general/presets-voices?pageNum=1&pageSize=10' \
  -H 'Authorization: Bearer sk-your-api-key'
```

**响应示例**：

```json
{
  "code": 0,
  "message": "SUCCEED",
  "request_id": "31a72582-cce3-48ca-ab72-9eab256dc322",
  "data": [
    { "voice_id": "829824295735410756", "voice_name": "钓系女友", "trial_url": "https://..." },
    { "voice_id": "829826751244537879", "voice_name": "温柔女声", "trial_url": "https://..." },
    { "voice_id": "829826792415842333", "voice_name": "播报男声", "trial_url": "https://..." },
    { "voice_id": "829826834144964676", "voice_name": "盐系少年", "trial_url": "https://..." },
    { "voice_id": "829826884271091753", "voice_name": "撒娇女友", "trial_url": "https://..." }
  ]
}
```

### 其他参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `watermark` | bool | 否 | 是否添加水印 |

---

## 官方功能支持矩阵（kling-v2-6）

| 类型 | 功能 | std 5s | std 10s | pro 5s | pro 10s |
|------|------|--------|---------|--------|---------|
| 文生视频 | 视频生成 | ✅（仅无声） | ✅（仅无声） | ✅ | ✅ |
| 图生视频 | 视频生成 | ✅（仅无声） | ✅（仅无声） | ✅ | ✅ |
| 图生视频 | 首尾帧 | - | - | ✅ | ✅ |
| 图生视频 | 声音控制 | - | - | ✅ | ✅ |

> **注意**：`std` 模式仅支持无声视频，`audio`/`voice_list` 需在 `pro` 模式下使用。首尾帧仅支持 `pro` 模式。

---

## 文生视频 vs 图生视频参数区别

系统通过是否传入 `image_urls` 自动判断模式：不传图片为文生视频，传图片为图生视频。

| 参数 | 文生视频 | 图生视频 |
|------|---------|---------|
| `prompt` | ✅ 必填 | ✅ 必填 |
| `image_urls` | ❌ 不传 | ✅ 必填（1-2 张，尾帧需 `pro`） |
| `negative_prompt` | ✅ 可选 | ✅ 可选 |
| `mode` | ✅ 可选 | ✅ 可选 |
| `duration` | ✅ 可选 | ✅ 可选 |
| `aspect_ratio` | ✅ 可选 | ⚠️ 可能被图片比例覆盖 |
| `audio` / `voice_list` | ✅ 可选（需 `pro`） | ✅ 可选（需 `pro`） |
| `watermark` | ✅ 可选 | ✅ 可选 |

---



---

## curl 请求示例

### 1. 文生视频（标准模式）

```bash
curl -X POST https://api.apimart.ai/v1/videos/generations \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kling-v2-6",
    "prompt": "一只金色的猫咪在阳光下的草地上奔跑，慢动作，电影质感",
    "mode": "std",
    "duration": 5,
    "aspect_ratio": "16:9"
  }'
```

### 2. 文生视频（专业模式 + 负面提示词）

```bash
curl -X POST https://api.apimart.ai/v1/videos/generations \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kling-v2-6",
    "prompt": "东京涩谷十字路口，雨夜霓虹灯倒映在湿漉漉的地面上，行人撑伞穿行",
    "negative_prompt": "模糊, 低画质, 变形",
    "mode": "pro",
    "duration": 10,
    "aspect_ratio": "16:9"
  }'
```

### 3. 图生视频（首帧图片）

```bash
curl -X POST https://api.apimart.ai/v1/videos/generations \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kling-v2-6",
    "prompt": "让画面中的人物转头微笑",
    "image_urls": ["https://example.com/portrait.jpg"],
    "mode": "std",
    "duration": 5,
    "aspect_ratio": "16:9"
  }'
```

### 4. 图生视频（首帧 + 尾帧控制）

```bash
curl -X POST https://api.apimart.ai/v1/videos/generations \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kling-v2-6",
    "prompt": "从白天过渡到黑夜的城市延时摄影",
    "image_urls": ["https://example.com/day-city.jpg", "https://example.com/night-city.jpg"],
    "mode": "pro",
    "duration": 5
  }'
```

### 5. 专业模式 + 自动音频

```bash
curl -X POST https://api.apimart.ai/v1/videos/generations \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kling-v2-6",
    "prompt": "海浪拍打礁石，海鸥在空中盘旋，远处有灯塔",
    "mode": "pro",
    "duration": 10,
    "audio": true,
    "aspect_ratio": "16:9"
  }'
```

### 6. 专业模式 + 指定音色

```bash
curl -X POST https://api.apimart.ai/v1/videos/generations \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kling-v2-6",
    "prompt": "一位主持人面对镜头播报新闻",
    "image_urls": ["https://example.com/anchor.jpg"],
    "mode": "pro",
    "duration": 10,
    "audio": true,
    "voice_list": [{"voice_id": "your-voice-id-here"}],
    "aspect_ratio": "16:9"
  }'
```

### 7. 全参数示例

```bash
curl -X POST https://api.apimart.ai/v1/videos/generations \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kling-v2-6",
    "prompt": "一位女歌手在舞台上演唱",
    "negative_prompt": "模糊, 变形, 低画质",
    "image_urls": ["https://example.com/singer.jpg"],
    "mode": "pro",
    "duration": 5,
    "aspect_ratio": "16:9",
    "audio": true,
    "voice_list": [{"voice_id": "singer-voice-id"}],
    "watermark": false
  }'
```

---

## 响应格式

### 提交成功

```json
{
  "code": 200,
  "data": [
    {
      "task_id": "task_xxxxxxxxxx",
      "status": "submitted"
    }
  ]
}
```

### 查询任务状态

```bash
curl -X GET https://api.apimart.ai/v1/tasks/task_xxxxxxxxxx \
  -H "Authorization: Bearer sk-your-api-key"
```

#### 处理中

```json
{
  "code": 200,
  "data": {
    "task_id": "task_xxxxxxxxxx",
    "status": "processing",
    "progress": "50%"
  }
}
```

#### 完成

```json
{
  "code": 200,
  "data": {
    "task_id": "task_xxxxxxxxxx",
    "status": "completed",
    "urls": [
      "https://cdn.example.com/videos/result.mp4"
    ]
  }
}
```

---



`voice_list` 也支持通过 `metadata` 字段传递（旧格式），但推荐直接使用一级参数。

旧格式示例（仍然有效，但不推荐）：

```bash
curl -X POST https://api.apimart.ai/v1/videos/generations \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kling-v2-6",
    "prompt": "一位主持人面对镜头播报新闻",
    "mode": "pro",
    "audio": true,
    "metadata": {
      "voice_list": [{"voice_id": "your-voice-id"}]
    }
  }'
```

> 当一级参数和 `metadata` 同时存在同名字段时，**一级参数优先**。
