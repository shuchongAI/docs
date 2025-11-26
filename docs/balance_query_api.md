# 余额查询接口文档

本文档介绍用于查询用户余额和令牌余额的API接口。这些接口使用Token认证，返回统一格式的余额信息。

## 目录

- [1. 查询令牌余额](#1-查询令牌余额)
- [2. 查询用户余额](#2-查询用户余额)

---

## 1. 查询令牌余额

获取当前令牌的剩余余额和已使用余额。

### 接口信息

- **接口地址**: `GET /v1/balance` 或 `GET /balance`
- **认证方式**: Bearer Token (在请求头中传递令牌key)
- **跨域支持**: ✅ 支持 (CORS)
- **限流**: 全局API限流

### 请求示例

```bash
curl -X GET 'https://your-domain.com/v1/balance' \
  -H 'Authorization: Bearer sk-xxxxxxxxxxxxxxxxxxxxxx'
```

### 请求头

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| Authorization | string | 是 | Bearer + 令牌key，格式：`Bearer sk-xxxxx` |

### 响应示例

**成功响应 (200)**:

```json
{
  "success": true,
  "remain_balance": 10.5,
  "used_balance": 2.3,
  "unlimited_quota": false
}
```

**无限额度的令牌响应 (200)**:

```json
{
  "success": true,
  "remain_balance": -1,
  "used_balance": 2.3,
  "unlimited_quota": true
}
```

**失败响应 (200)**:

```json
{
  "success": false,
  "message": "获取令牌信息失败: record not found"
}
```

### 响应字段说明

| 字段名 | 类型 | 说明 |
|--------|------|------|
| success | boolean | 请求是否成功 |
| message | string | 错误信息（仅失败时返回） |
| remain_balance | float | 剩余余额，无限额度时为 -1 |
| used_balance | float | 已使用余额 |
| unlimited_quota | boolean | 是否为无限额度的令牌 |

### 余额单位说明

余额数值的单位取决于系统配置的 `QuotaDisplayType`：

| 显示类型 | 说明 | 计算方式 |
|----------|------|----------|
| USD | 美元 | `quota / QuotaPerUnit` |
| CNY | 人民币 | `quota / QuotaPerUnit * USDExchangeRate` |
| Tokens | Token数量 | 原始quota值 |

> **注意**: 当令牌为无限额度时，`remain_balance` 返回 -1，`unlimited_quota` 返回 true。

---

## 2. 查询用户余额

获取当前用户的剩余余额和已使用余额。该接口返回用户级别的余额信息，与具体令牌无关。

### 接口信息

- **接口地址**: `GET /v1/user/balance` 或 `GET /user/balance`
- **认证方式**: Bearer Token (在请求头中传递令牌key)
- **跨域支持**: ✅ 支持 (CORS)
- **限流**: 全局API限流

### 请求示例

```bash
curl -X GET 'https://your-domain.com/v1/user/balance' \
  -H 'Authorization: Bearer sk-xxxxxxxxxxxxxxxxxxxxxx'
```

### 请求头

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| Authorization | string | 是 | Bearer + 令牌key，格式：`Bearer sk-xxxxx` |

### 响应示例

**成功响应 (200)**:

```json
{
  "success": true,
  "remain_balance": 100.0,
  "used_balance": 25.5
}
```

**失败响应 (200)**:

获取用户额度失败：
```json
{
  "success": false,
  "message": "获取用户额度失败: record not found"
}
```

获取已使用额度失败：
```json
{
  "success": false,
  "message": "获取已使用额度失败: record not found"
}
```

### 响应字段说明

| 字段名 | 类型 | 说明 |
|--------|------|------|
| success | boolean | 请求是否成功 |
| message | string | 错误信息（仅失败时返回） |
| remain_balance | float | 剩余余额 |
| used_balance | float | 已使用余额 |

### 余额单位说明

余额数值的单位取决于系统配置的 `QuotaDisplayType`：

| 显示类型 | 说明 | 计算方式 |
|----------|------|----------|
| USD | 美元 | `quota / QuotaPerUnit` |
| CNY | 人民币 | `quota / QuotaPerUnit * USDExchangeRate` |
| Tokens | Token数量 | 原始quota值 |

---

## 令牌余额 vs 用户余额

| 对比项 | 令牌余额 (`/v1/balance`) | 用户余额 (`/v1/user/balance`) |
|--------|--------------------------|-------------------------------|
| 作用范围 | 单个令牌 | 整个用户账户 |
| 数据来源 | Token表的RemainQuota和UsedQuota | User表的quota和used_quota |
| 使用场景 | 监控单个令牌的使用情况 | 查看用户账户总体余额 |
| 受限于 | 令牌级别的额度限制 | 用户级别的额度限制 |

---

## 使用示例

### JavaScript/TypeScript

```typescript
const API_BASE = 'https://your-domain.com';
const API_KEY = 'sk-xxxxxxxxxxxxxxxxxxxxxx';

// 查询令牌余额
async function getTokenBalance() {
  const response = await fetch(`${API_BASE}/v1/balance`, {
    headers: {
      'Authorization': `Bearer ${API_KEY}`
    }
  });

  const data = await response.json();

  if (data.success) {
    console.log(`令牌剩余余额: ${data.remain_balance}`);
    console.log(`令牌已使用: ${data.used_balance}`);
  } else {
    console.error('查询失败:', data.message);
  }

  return data;
}

// 查询用户余额
async function getUserBalance() {
  const response = await fetch(`${API_BASE}/v1/user/balance`, {
    headers: {
      'Authorization': `Bearer ${API_KEY}`
    }
  });

  const data = await response.json();

  if (data.success) {
    console.log(`用户剩余余额: ${data.remain_balance}`);
    console.log(`用户已使用: ${data.used_balance}`);
  } else {
    console.error('查询失败:', data.message);
  }

  return data;
}
```

### Python

```python
import requests

API_BASE = 'https://your-domain.com'
API_KEY = 'sk-xxxxxxxxxxxxxxxxxxxxxx'

headers = {
    'Authorization': f'Bearer {API_KEY}'
}

# 查询令牌余额
def get_token_balance():
    response = requests.get(f'{API_BASE}/v1/balance', headers=headers)
    data = response.json()

    if data.get('success'):
        print(f"令牌剩余余额: {data['remain_balance']}")
        print(f"令牌已使用: {data['used_balance']}")
    else:
        print(f"查询失败: {data.get('message')}")

    return data

# 查询用户余额
def get_user_balance():
    response = requests.get(f'{API_BASE}/v1/user/balance', headers=headers)
    data = response.json()

    if data.get('success'):
        print(f"用户剩余余额: {data['remain_balance']}")
        print(f"用户已使用: {data['used_balance']}")
    else:
        print(f"查询失败: {data.get('message')}")

    return data
```

### cURL

```bash
# 查询令牌余额
curl -X GET 'https://your-domain.com/v1/balance' \
  -H 'Authorization: Bearer sk-xxxxxxxxxxxxxxxxxxxxxx'

# 查询用户余额
curl -X GET 'https://your-domain.com/v1/user/balance' \
  -H 'Authorization: Bearer sk-xxxxxxxxxxxxxxxxxxxxxx'
```

---

## 错误处理

### 常见错误

| 错误信息 | 原因 | 解决方案 |
|----------|------|----------|
| 无Authorization头 | 未提供Authorization请求头 | 添加 `Authorization: Bearer sk-xxxxx` 请求头 |
| 获取令牌信息失败 | 令牌不存在或已删除 | 检查令牌key是否正确 |
| 获取用户额度失败 | 用户不存在 | 检查令牌关联的用户是否存在 |
| 获取已使用额度失败 | 数据库查询错误 | 联系管理员检查系统状态 |

---

## 安全注意事项

1. **令牌保密**: 令牌key相当于密码，请妥善保管，不要泄露
2. **HTTPS**: 生产环境建议使用HTTPS，防止令牌被窃取
3. **限流**: 接口有全局API限流限制，避免频繁请求

---

## 技术支持

如有问题，请查看系统文档或联系技术支持。
