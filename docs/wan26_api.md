# 阿里云万相 Wan2.6 视频生成 API

## 概述

Wan2.6 是阿里云万相（Wanxiang）视频生成模型，支持**文生视频 (Text-to-Video)** 和**图生视频 (Image-to-Video)** 两种模式。系统会根据请求中是否包含图片自动选择模式。

---

## 提交任务

**POST** `/v1/videos/generations`

### 请求头

```
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

### 请求体

#### 文生视频（最简请求）

```json
{
  "model": "wan2.6",
  "prompt": "一只可爱的猫咪在草地上奔跑"
}
```

#### 文生视频（完整参数）

```json
{
  "model": "wan2.6",
  "prompt": "一只可爱的猫咪在草地上奔跑",
  "negative_prompt": "模糊, 低质量, 变形",
  "size": "16:9",
  "resolution": "720p",
  "duration": 5,
  "seed": 12345,
  "prompt_extend": true,
  "audio": true,
  "shot_type": "single",
  "watermark": false
}
```

#### 图生视频

```json
{
  "model": "wan2.6",
  "prompt": "让图片中的人物挥手",
  "image_urls": ["https://example.com/image.jpg"],
  "resolution": "1080p",
  "duration": 10,
  "template": "模板名称"
}
```

#### 图生视频（Base64 图片）

```json
{
  "model": "wan2.6",
  "prompt": "让猫咪站起来走动",
  "image_urls": ["data:image/png;base64,iVBORw0KGgo..."],
  "duration": 5
}
```

### 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `model` | string | 是 | - | 模型名称，固定为 `wan2.6` |
| `prompt` | string | t2v必填 | - | 视频生成提示词 |
| `image_urls` | array | i2v必填 | - | 参考图片 URL 数组（仅支持 1 张） |
| `negative_prompt` | string | 否 | - | 负面提示词，描述不希望出现的内容 |
| `size` | string | 否 | `16:9` | 宽高比 |
| `resolution` | string | 否 | `720p` | 分辨率 |
| `duration` | int | 否 | 5 | 视频时长（秒） |
| `seed` | int | 否 | - | 随机种子，用于复现结果 |
| `prompt_extend` | bool | 否 | - | 是否自动扩展提示词 |
| `audio` | bool | 否 | - | 是否自动添加音频 |
| `audio_url` | string | 否 | - | 指定音频 URL（优先级高于 audio） |
| `shot_type` | string | 否 | - | 镜头类型：`single`（单镜头）/ `multi`（多镜头） |
| `watermark` | bool | 否 | - | 是否添加水印 |
| `template` | string | 否 | - | i2v 模板名称（仅图生视频） |

### 参数限制

#### 时长 (duration)

仅支持以下三种时长：

| 时长 | 说明 |
|------|------|
| 5 秒 | 默认值 |
| 10 秒 | - |
| 15 秒 | - |

#### 分辨率 (resolution)

| 分辨率 | 说明 |
|--------|------|
| `720p` | 默认值，标清 |
| `1080p` | 高清 |

> 注意：不支持 480p

#### 宽高比 (size)

| 宽高比 | 说明 | 720p 尺寸 | 1080p 尺寸 |
|--------|------|-----------|------------|
| `16:9` | 横屏（默认） | 1280×720 | 1920×1080 |
| `9:16` | 竖屏 | 720×1280 | 1080×1920 |
| `1:1` | 方形 | 960×960 | 1440×1440 |
| `4:3` | 横屏 | 1088×832 | 1632×1248 |
| `3:4` | 竖屏 | 832×1088 | 1248×1632 |

### 响应示例

```json
{
  "id": "task_01J9HA7JPQ9A0Z6JZ3V8M9W6PZ",
  "status": "pending"
}
```

---

## 查询任务

**GET** `/v1/tasks/{task_id}`

### 请求头

```
Authorization: Bearer YOUR_API_KEY
```

### 响应示例

#### 排队中

```json
{
  "id": "task_01J9HA7JPQ9A0Z6JZ3V8M9W6PZ",
  "status": "pending",
  "progress": "10%"
}
```

#### 处理中

```json
{
  "id": "task_01J9HA7JPQ9A0Z6JZ3V8M9W6PZ",
  "status": "processing",
  "progress": "50%"
}
```

#### 成功

```json
{
  "id": "task_01J9HA7JPQ9A0Z6JZ3V8M9W6PZ",
  "status": "success",
  "progress": "100%",
  "result_url": "https://cdn.example.com/video.mp4"
}
```

#### 失败

```json
{
  "id": "task_01J9HA7JPQ9A0Z6JZ3V8M9W6PZ",
  "status": "failed",
  "progress": "100%",
  "reason": "Task failed with unknown reason"
}
```

---

## cURL 示例

### 文生视频

```bash
curl --request POST \
  --url https://your-api-domain.com/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "wan2.6",
    "prompt": "一只可爱的猫咪在阳光下伸懒腰",
    "resolution": "720p",
    "duration": 5,
    "size": "16:9"
  }'
```

### 图生视频

```bash
curl --request POST \
  --url https://your-api-domain.com/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "wan2.6",
    "prompt": "让图中的人物微笑挥手",
    "image_urls": ["https://example.com/person.jpg"],
    "resolution": "1080p",
    "duration": 5
  }'
```

### 查询任务

```bash
curl --request GET \
  --url https://your-api-domain.com/v1/tasks/task_01J9HA7JPQ9A0Z6JZ3V8M9W6PZ \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

---

## 状态说明

| 状态 | 说明 |
|------|------|
| `pending` | 排队中 |
| `processing` | 生成中 |
| `success` | 生成成功 |
| `failed` | 生成失败 |

---

## 计费说明

按**视频时长**和**分辨率**计费：

| 分辨率 | 单价 |
|--------|------|
| 720p | $0.2 / 秒 |
| 1080p | $0.4 / 秒 |

### 计费示例

| 时长 | 分辨率 | 费用 |
|------|--------|------|
| 5 秒 | 720p | $1.0 |
| 10 秒 | 720p | $2.0 |
| 15 秒 | 720p | $3.0 |
| 5 秒 | 1080p | $2.0 |
| 10 秒 | 1080p | $4.0 |
| 15 秒 | 1080p | $6.0 |

---

## 模式说明

### 文生视频 (Text-to-Video)

- 上游模型：`wan2.6-t2v`
- 必须提供 `prompt` 参数
- 不需要 `image_urls` 参数

### 图生视频 (Image-to-Video)

- 上游模型：`wan2.6-i2v`
- 必须提供 `image_urls` 参数（仅支持 1 张图片）
- `prompt` 参数可选，用于描述期望的动作

> 系统会根据请求中是否包含 `image_urls` 自动选择模式。

---

## 错误码

| 错误码 | 说明 |
|--------|------|
| `missing_prompt` | 文生视频模式下未提供 prompt |
| `invalid_request` | 请求参数无效 |
| `invalid_duration` | 不支持的时长（仅支持 5/10/15 秒） |
| `upstream_error` | 上游服务错误 |

---

## 注意事项

1. **图片格式**：支持公网可访问的 URL 或 Base64 编码（`data:image/jpeg;base64,...`）
2. **图片数量**：图生视频仅支持 1 张参考图片
3. **时长限制**：仅支持 5、10、15 秒三种时长
4. **分辨率**：不支持 480p，仅支持 720p 和 1080p
5. **异步处理**：视频生成为异步任务，需轮询查询状态
