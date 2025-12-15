# 豆包图片生成 API 文档

## 接口地址

```
POST /v1/images/generations
```

## 支持模型

| 模型名 | 说明 | 支持分辨率 |
|--------|------|-----------|
| `doubao-seedance-4-0` | 豆包 Seedream 4.0 | 1K, 2K, 4K |
| `doubao-seedance-4-5` | 豆包 Seedream 4.5 | 2K, 4K（不支持1K） |

## 请求参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `model` | string | 是 | 模型名称 |
| `prompt` | string | 是 | 图片描述提示词 |
| `size` | string | 否 | 图片比例，默认 `1:1` |
| `resolution` | string | 否 | 分辨率，默认 `2K` |
| `n` | int | 否 | 生成数量，默认 1 |
| `image_urls` | array | 否 | 参考图片 URL（图生图） |
| `watermark` | bool | 否 | 是否添加水印，默认 `false` |
| `sequential_image_generation` | string | 否 | 组图模式：`auto`/`disabled` |
| `optimize_prompt_options_mode` | string | 否 | 提示词优化：`standard`/`fast` |

### size 参数（图片比例）

支持以下比例值：

| 比例 | 说明 |
|------|------|
| `1:1` | 正方形（默认） |
| `4:3` | 横向 4:3 |
| `3:4` | 纵向 3:4 |
| `16:9` | 横向宽屏 |
| `9:16` | 纵向竖屏 |
| `3:2` | 横向 3:2 |
| `2:3` | 纵向 2:3 |
| `21:9` | 超宽屏 |
| `9:21` | 超竖屏 |

### resolution 参数（分辨率）

| 分辨率 | 1:1 尺寸 | 16:9 尺寸 | 说明 |
|--------|----------|-----------|------|
| `1K` | 1024x1024 | 1280x720 | 仅 4.0 支持 |
| `2K` | 2048x2048 | 2560x1440 | 默认值 |
| `4K` | 4096x4096 | 5404x3040 | 高清 |

> 注意：`doubao-seedance-4-5` 不支持 1K 分辨率

### 分辨率+比例 完整像素映射表

#### 1K 分辨率
| 比例 | 像素 |
|------|------|
| 1:1 | 1024x1024 |
| 4:3 | 1152x864 |
| 3:4 | 864x1152 |
| 16:9 | 1280x720 |
| 9:16 | 720x1280 |
| 3:2 | 1248x832 |
| 2:3 | 832x1248 |
| 21:9 | 1512x648 |
| 9:21 | 648x1512 |

#### 2K 分辨率
| 比例 | 像素 |
|------|------|
| 1:1 | 2048x2048 |
| 4:3 | 2304x1728 |
| 3:4 | 1728x2304 |
| 16:9 | 2560x1440 |
| 9:16 | 1440x2560 |
| 3:2 | 2496x1664 |
| 2:3 | 1664x2496 |
| 21:9 | 3024x1296 |
| 9:21 | 1296x3024 |

#### 4K 分辨率
| 比例 | 像素 |
|------|------|
| 1:1 | 4096x4096 |
| 4:3 | 4694x3520 |
| 3:4 | 3520x4694 |
| 16:9 | 5404x3040 |
| 9:16 | 3040x5404 |
| 3:2 | 4992x3328 |
| 2:3 | 3328x4992 |
| 21:9 | 6198x2656 |
| 9:21 | 2656x6198 |

## 请求示例

### 基础文生图

```bash
curl -X POST "https://api.example.com/v1/images/generations" \
  -H "Authorization: Bearer sk-your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "doubao-seedance-4-0",
    "prompt": "一只可爱的猫咪在阳光下",
    "size": "1:1",
    "resolution": "2K"
  }'
```

### 多图生成

```bash
curl -X POST "https://api.example.com/v1/images/generations" \
  -H "Authorization: Bearer sk-your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "doubao-seedance-4-5",
    "prompt": "星空下的古老城堡",
    "size": "16:9",
    "resolution": "4K",
    "n": 2
  }'
```

### 图生图（单图参考）

```bash
curl -X POST "https://api.example.com/v1/images/generations" \
  -H "Authorization: Bearer sk-your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "doubao-seedance-4-0",
    "prompt": "将图片转换为油画风格",
    "size": "1:1",
    "resolution": "2K",
    "image_urls": ["https://example.com/image.jpg"]
  }'
```

### 多图融合

```bash
curl -X POST "https://api.example.com/v1/images/generations" \
  -H "Authorization: Bearer sk-your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "doubao-seedance-4-0",
    "prompt": "融合两张图片的风格",
    "size": "1:1",
    "resolution": "2K",
    "image_urls": [
      "https://example.com/image1.jpg",
      "https://example.com/image2.jpg"
    ]
  }'
```

### 完整参数示例

```bash
curl -X POST "https://api.example.com/v1/images/generations" \
  -H "Authorization: Bearer sk-your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "doubao-seedance-4-0",
    "prompt": "美丽的山水风景画",
    "size": "16:9",
    "resolution": "2K",
    "n": 2,
    "watermark": false,
    "sequential_image_generation": "auto",
    "optimize_prompt_options_mode": "standard"
  }'
```

## 响应格式

### 提交成功响应

```json
{
  "code": 200,
  "data": [
    {
      "task_id": "task_01JFXYZ123456789ABCDEF",
      "status": "submitted"
    }
  ]
}
```

### 查询任务结果

```
GET /v1/tasks/{task_id}
```

#### 处理中响应

```json
{
  "code": 200,
  "data": {
    "task_id": "task_01JFXYZ123456789ABCDEF",
    "status": "processing",
    "progress": "50%"
  }
}
```

#### 完成响应

```json
{
  "code": 200,
  "data": {
    "task_id": "task_01JFXYZ123456789ABCDEF",
    "status": "completed",
    "progress": "100%",
    "result": {
      "urls": [
        "https://r2.example.com/images/image_task_xxx_0.png",
        "https://r2.example.com/images/image_task_xxx_1.png"
      ]
    }
  }
}
```

## 计费说明

- 按**张数**计费，支持 `n` 参数指定生成数量
- 预扣费：按请求的 `n` 张数预先扣费
- 退款机制：如果实际生成数量少于请求数量，自动退还差额
- 日志格式：`固定价格 $0.0700/张，请求 2 张，生成 2 张`

## 注意事项

1. `doubao-seedance-4-5` 模型不支持 1K 分辨率，请使用 2K 或 4K
2. 使用 `n > 1` 时会自动启用组图模式，并在提示词末尾追加 `, generate {n} images`
3. 图片 URL 支持 Base64 格式（会自动转换为临时 URL）
4. 生成的图片会自动镜像到 R2 存储，返回的 URL 为 R2 地址
