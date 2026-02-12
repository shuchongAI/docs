# 海螺 2.3 视频生成 API（MiniMax-Hailuo-2.3）

## 模型简介

`MiniMax-Hailuo-2.3` 是 MiniMax 海螺最新一代视频生成模型。传入 `first_frame_image` 参数即可以指定图片作为视频起始帧。

## 提交任务

**POST** `/v1/videos/generations`

### 请求头

```
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

### 最简请求

```json
{
  "model": "MiniMax-Hailuo-2.3",
  "prompt": "一只可爱的猫咪在草地上奔跑"
}
```

### 完整参数

```json
{
  "model": "MiniMax-Hailuo-2.3",
  "prompt": "一只可爱的猫咪在草地上奔跑",
  "duration": 6,
  "resolution": "768p",
  "prompt_optimizer": true,
  "fast_pretreatment": false,
  "watermark": false
}
```

### 指定首帧图片

```json
{
  "model": "MiniMax-Hailuo-2.3",
  "prompt": "小猫跑向镜头，微笑着眨眼",
  "first_frame_image": "https://example.com/cat.jpg",
  "duration": 6,
  "resolution": "1080p"
}
```

### 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `model` | string | 是 | - | 固定为 `MiniMax-Hailuo-2.3` |
| `prompt` | string | 是 | - | 视频描述（最多 2000 字符），支持运镜指令 |
| `first_frame_image` | string | 否 | - | 视频起始帧图片（公网 URL 或 Base64） |
| `duration` | int | 否 | 6 | 视频时长，支持 `6` 或 `10` 秒 |
| `resolution` | string | 否 | `768p` | 分辨率：`768p`、`1080p` |
| `prompt_optimizer` | bool | 否 | true | 是否自动优化 prompt |
| `fast_pretreatment` | bool | 否 | false | 是否缩短 prompt 优化耗时 |
| `watermark` | bool | 否 | false | 是否添加水印 |

### 参数限制

| 分辨率 | 支持时长 |
|--------|----------|
| 768p | 6 秒、10 秒 |
| 1080p | 仅 6 秒 |

### 运镜指令

在 prompt 中使用 `[指令]` 语法控制运镜，支持以下 15 种：

| 类别 | 指令 |
|------|------|
| 平移 | `[左移]` `[右移]` |
| 左右摇 | `[左摇]` `[右摇]` |
| 推拉 | `[推进]` `[拉远]` |
| 升降 | `[上升]` `[下降]` |
| 上下摇 | `[上摇]` `[下摇]` |
| 变焦 | `[变焦推近]` `[变焦拉远]` |
| 其他 | `[晃动]` `[跟随]` `[固定]` |

**示例：**

```json
{
  "model": "MiniMax-Hailuo-2.3",
  "prompt": "[推进]一只猫咪在花园中奔跑，镜头缓缓推进特写"
}
```

### 响应示例

```json
{
  "id": "task_01J9HA7JPQ9A0Z6JZ3V8M9W6PZ",
  "status": "pending"
}
```

---

## 查询任务

**GET** `/v1/videos/generations/{task_id}`

### 请求头

```
Authorization: Bearer YOUR_API_KEY
```

### 响应示例

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

### 提交任务

```bash
curl --request POST \
  --url https://your-api-domain.com/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "MiniMax-Hailuo-2.3",
    "prompt": "一只可爱的猫咪在草地上奔跑",
    "duration": 6,
    "resolution": "768p"
  }'
```

### 指定首帧图片

```bash
curl --request POST \
  --url https://your-api-domain.com/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "MiniMax-Hailuo-2.3",
    "prompt": "小猫跑向镜头，微笑着眨眼",
    "first_frame_image": "https://example.com/cat.jpg",
    "duration": 6,
    "resolution": "1080p"
  }'
```

### 查询任务

```bash
curl --request GET \
  --url https://your-api-domain.com/v1/videos/generations/task_01J9HA7JPQ9A0Z6JZ3V8M9W6PZ \
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
