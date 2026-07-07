# 替换变量速查手册

## 变量一览

| 变量 | 位置 | 必填 | 说明 |
|------|------|------|------|
| [IP_NAME] | prompt 正文中 | ✅ | 角色名称，直接替换 |
| [Aspect_ratio] | prompt 末尾 | ❌ | 画面比例，默认 16:9 |

## 参考图说明

参考图 URL 不在 prompt 文本中替换，而是在调用生图 API 时作为 image 参数传入。

建议放在 `image[0]` 位置，并在 prompt 后附加一致性提示：
> Maintain IP identity and consistency: strictly follow the reference character's face, hairstyle, proportions and costume.
