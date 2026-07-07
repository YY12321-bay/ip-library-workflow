# {IP名称}

> {品牌名称} 品牌IP形象 | {风格定位}

---

## 📋 IP信息

| 项目 | 内容 |
|------|------|
| **角色名** | {IP名称} |
| **品牌** | {品牌名称} |
| **产品场景** | {产品场景} |
| **风格** | {风格定位} |
| **参考图** | `reference_square.jpg`（方形800×800，API传参用） |

## 📝 生图规范

### Prompt必备句式
```
Maintain IP identity and consistency throughout.
```

### 参考图传参
- 读取 `reference_square.jpg` → base64 → 放在 `image[0]`
- 风格参考图放在 `image[1]`

### 避免写的特征（有参考图时）
- ❌ 五官位置/形状
- ❌ 体型比例
- ❌ 主色调/颜色
- ❌ 轮廓形状
