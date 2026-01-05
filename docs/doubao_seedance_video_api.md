# Doubao Seedance 视频生成 API 文档

## 支持的模型

| 模型名称 | 说明 |
|---------|------|
| `doubao-seedance-1-0-pro-fast` | 1.0 快速模式 |
| `doubao-seedance-1-0-pro-quality` | 1.0 质量模式（支持首尾帧） |
| `doubao-seedance-1-5-pro` | 1.5 Pro（支持音频、多参考图） |

---

## 请求格式

### 基础请求

```bash
POST /v1/videos/generations
Content-Type: application/json
Authorization: Bearer YOUR_API_KEY
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `model` | string | ✅ | - | 模型名称 |
| `prompt` | string | ✅ | - | 视频描述提示词 |
| `size` | string | ❌ | `16:9` | 宽高比 |
| `resolution` | string | ❌ | 见下表 | 分辨率 |
| `duration` | int | ❌ | `5` | 时长（秒） |
| `framespersecond` | int | ❌ | `24` | 帧率 |
| `seed` | int64 | ❌ | 随机 | 随机种子 |
| `camerafixed` | bool | ❌ | `false` | 固定摄像头 |
| `watermark` | bool | ❌ | `false` | 添加水印 |
| `audio` | bool | ❌ | `false` | 生成音频（仅1.5 Pro） |
| `image_urls` | string[] | ❌ | - | 图片URL数组（自动分配角色）⚠️ 与 `image_with_roles` 二选一 |
| `image_with_roles` | object[] | ❌ | - | 带角色的图片数组 ⚠️ 与 `image_urls` 二选一 |

### 模型参数差异

| 参数 | 1.0 fast | 1.0 quality | 1.5 Pro |
|------|----------|-------------|---------|
| 默认分辨率 | 1080p | 1080p | **720p** |
| 支持分辨率 | 480p/720p/1080p | 480p/720p/1080p | **480p/720p** |
| 时长范围 | 2-12秒 | 2-12秒 | **4-12秒** |
| 首帧 | ✅ | ✅ | ✅ |
| 尾帧 | ❌ | ✅ | ✅ |
| 参考图 | `reference` (1张) | `reference` (1张) | **`reference_image` (1-4张)** |
| 音频 | ❌ | ❌ | **✅** |

### 支持的宽高比

```
16:9, 9:16, 1:1, 4:3, 3:4, 21:9, keep_ratio, adaptive
```

---

## 图片参数

> **注意**：`image_urls` 和 `image_with_roles` 二选一，不能同时使用。

### 方式一：`image_urls`（字符串数组，自动分配角色）

```json
// 1张 = 首帧
"image_urls": ["https://example.com/first.png"]

// 2张 = 首帧 + 尾帧
"image_urls": ["https://example.com/first.png", "https://example.com/last.png"]

// 3+张 = 首帧 + 尾帧 + 参考图
"image_urls": [
  "https://example.com/first.png",
  "https://example.com/last.png",
  "https://example.com/ref1.png",
  "https://example.com/ref2.png"
]
```

### 方式二：`image_with_roles`（对象数组，明确指定角色）

```json
"image_with_roles": [
  {"url": "https://example.com/first.png", "role": "first_frame"},
  {"url": "https://example.com/last.png", "role": "last_frame"},
  {"url": "https://example.com/ref.png", "role": "reference"}
]
```

### 图片角色说明

| 角色 | 1.0 模型 | 1.5 Pro | 数量限制 |
|------|----------|---------|----------|
| `first_frame` | ✅ | ✅ | 1张 |
| `last_frame` | ✅ (仅quality) | ✅ | 1张 |
| `reference` | ✅ | ❌ | 1张 |
| `reference_image` | ❌ | ✅ | 1-4张 |

---

## 请求示例

### 1. 基础文生视频

```bash
curl -X POST "https://your-api.com/v1/videos/generations" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "doubao-seedance-1-5-pro",
    "prompt": "一只猫在草地上奔跑"
  }'
```

### 2. 完整参数（1.5 Pro）

```bash
curl -X POST "https://your-api.com/v1/videos/generations" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "doubao-seedance-1-5-pro",
    "prompt": "一只猫在草地上奔跑，阳光明媚",
    "size": "16:9",
    "resolution": "720p",
    "duration": 5,
    "framespersecond": 24,
    "camerafixed": false,
    "audio": true
  }'
```

### 3. 图生视频（字符串数组）

```bash
curl -X POST "https://your-api.com/v1/videos/generations" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "doubao-seedance-1-0-pro-quality",
    "prompt": "让画面动起来",
    "image_urls": [
      "https://example.com/first.png",
      "https://example.com/last.png"
    ]
  }'
```

### 4. 带参考图（对象数组）

```bash
curl -X POST "https://your-api.com/v1/videos/generations" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "doubao-seedance-1-5-pro",
    "prompt": "参考风格生成视频",
    "audio": true,
    "image_with_roles": [
      {"url": "https://example.com/first.png", "role": "first_frame"},
      {"url": "https://example.com/ref1.png", "role": "reference_image"},
      {"url": "https://example.com/ref2.png", "role": "reference_image"}
    ]
  }'
```

---

## 响应格式

### 成功响应

```json
{
  "id": "task_01JXXXXXXXXXXXXXX",
  "status": "pending"
}
```

### 查询任务状态

```bash
GET /v1/videos/generations/{task_id}
```

### 任务完成响应

```json
{
  "id": "task_01JXXXXXXXXXXXXXX",
  "status": "completed",
  "video_url": "https://example.com/video.mp4"
}
```

---

## 计费规则

**计费公式**：`价格 = 分辨率单价 × 秒数`

| 分辨率 | 说明 |
|--------|------|
| 480p | 最低价格 |
| 720p | 中等价格 |
| 1080p | 最高价格（仅1.0支持） |

---

## 备用渠道说明

系统支持 Replicate 作为备用渠道，以下情况**自动使用官方渠道**：

1. 分辨率为 `480p`（Replicate 不支持）
2. 图片数量超过 2 张（Replicate 不支持参考图）

---

## 错误码

| 错误码 | 说明 |
|--------|------|
| `invalid_request` | 请求参数格式错误 |
| `model_not_support_first_last_frame` | 模型不支持首尾帧 |
| `invalid_image_urls` | 图片参数格式错误 |
| `duration_out_of_range` | 时长超出范围 |
| `resolution_not_supported` | 分辨率不支持 |
