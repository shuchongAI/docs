# 豆包视频生成 API 文档

## 接口地址

```
POST /v1/videos/generations
```

## 支持的模型

| 模型名称 | 说明 |
|---------|------|
| `doubao-seedance-1-0-pro-fast` | 快速版，生成速度快（40-90秒），适合预览和迭代 |
| `doubao-seedance-1-0-pro-quality` | 高质量版，生成时间较长（90-300秒），画质更优 |

---

## 完整请求示例

```bash
curl -X POST "https://api.apimart.ai/v1/videos/generations" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "doubao-seedance-1-0-pro-fast",
    "prompt": "一只可爱的小猫在阳光下玩耍，毛发蓬松，眼睛明亮",
    "duration": 5,
    "aspect_ratio": "16:9",
    "resolution": "720p",
    "image_urls": ["https://example.com/cat.png"]
  }'
```

---

## 请求参数

| 参数 | 类型 | 必填 | 说明 | 可选值 | 示例 |
|------|------|------|------|--------|------|
| `model` | string | 是 | 模型版本，fast 版速度快，quality 版画质高 | `doubao-seedance-1-0-pro-fast`、`doubao-seedance-1-0-pro-quality` | `"doubao-seedance-1-0-pro-fast"` |
| `prompt` | string | 是 | 视频内容描述，建议详细描述场景、动作、风格等 | - | `"海边日落，金色阳光洒在海面上"` |
| `duration` | integer | 否 | 视频时长（秒），默认 5 秒 | `5`、`10` | `5` |
| `aspect_ratio` | string | 否 | 视频宽高比，默认 16:9 | `16:9`（横屏）、`9:16`（竖屏）、`1:1`（方形） | `"16:9"` |
| `resolution` | string | 否 | 视频分辨率，默认 720p | `480p`、`720p`、`1080p` | `"1080p"` |
| `image_urls` | array | 否 | 首帧图 URL 数组，基于图片生成视频 | - | `["https://example.com/cat.png"]` |
| `image_with_roles` | array | 否 | 带角色的图片数组，支持首帧/尾帧/参考图 | - | 见下方说明 |

### image_with_roles 参数说明

用于指定图片的角色，实现更精细的控制：

```json
{
  "image_with_roles": [
    {"url": "https://example.com/start.png", "role": "first_frame"},
    {"url": "https://example.com/end.png", "role": "last_frame"}
  ]
}
```

**role 可选值**：
- `first_frame`：首帧图，作为视频起始画面
- `last_frame`：尾帧图，作为视频结束画面
- `reference`：参考图，用于指导视频风格

> **注意**：`image_urls` 和 `image_with_roles` 不能同时使用。

---


## 使用场景示例

### 场景 1：快速生成横屏预览视频

```json
{
  "model": "doubao-seedance-1-0-pro-fast",
  "prompt": "海边日落，金色阳光洒在海面上，海浪轻轻拍打沙滩"
}
```

### 场景 2：生成高质量竖屏短视频

```json
{
  "model": "doubao-seedance-1-0-pro-quality",
  "prompt": "一位女孩在樱花树下旋转，花瓣随风飘落",
  "duration": 5,
  "aspect_ratio": "9:16",
  "resolution": "1080p"
}
```

### 场景 3：基于产品图生成动态展示视频

```json
{
  "model": "doubao-seedance-1-0-pro-fast",
  "prompt": "产品缓缓旋转展示，背景为纯白色，光线柔和",
  "image_urls": ["https://example.com/product.png"],
  "duration": 5,
  "aspect_ratio": "1:1"
}
```

### 场景 4：制作动态转场效果（首尾帧）

```json
{
  "model": "doubao-seedance-1-0-pro-quality",
  "prompt": "画面从白天逐渐过渡到夜晚，城市灯光逐渐亮起",
  "image_with_roles": [
    {"url": "https://example.com/day.png", "role": "first_frame"},
    {"url": "https://example.com/night.png", "role": "last_frame"}
  ],
  "duration": 5
}
```

---