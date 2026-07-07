---
type: ip-character-sheet
desc: IP 角色设定集图片生成提示词模板
---

# IP 角色设定集 Prompt 模板

Cinematic, art book style character identity sheet for [IP_NAME].

Design goal: Presented as an exclusive character study from a high-end animation studio, not a standard reference sheet.

Composition and layout: Bold asymmetric composition. A large hero full-body front view slightly off-center as the visual anchor. Surrounding it with clear spacing and breathing room, arranged smaller supporting views including: neutral full-body, back view, side view, sitting pose, tilted pose, crouching pose, top-down body angle, bottom-up angle, and an expressive close-up portrait. All images must be clearly separated, no overlapping, stacking or cropped body parts.

Identity consistency: Strictly lock character identity across all views: same face, same proportions, same hairstyle, same costume, same posture and visual personality, ensuring the character can be consistently recognized by the model.

Art study elements: Integrate a small silhouette study area (containing 2-3 simplified black character silhouettes), a small expression study area (presenting subtle emotional variations), and a small detail study area (close-up key visual features of face, hair and costume).

Aesthetic style: Extreme minimalism, cinematic, clean and expressive. Background is pure white or soft cream white, no environment, no props, no logos, no watermarks. Use large areas of white space and intentional imbalance to create a premium feel.

Text and annotations: Add a stylish, minimalist character ID info block with name, role, core mood and visual signature. Only use small handwritten style labels, subtle edit arrows and annotation markers where helpful, keeping the overall composition clean and elegant.

Final output should be an artistic identity sheet designed to help AI models deeply understand the character's uniqueness and full design.
[Aspect_ratio]

## 可替换变量

| 变量 | 必填 | 说明 | 示例 |
|------|------|------|------|
| [IP_NAME] | ✅ | 角色名称 | `莉莉` / `芒果仔` |
| [Aspect_ratio] | ❌ | 画面比例，不填默认 16:9 | `Aspect ratio 16:9.` |

## 使用流程

1. 读取 template.md
2. 将 [IP_NAME] 替换为角色名
3. 将 [Aspect_ratio] 替换为需要的比例（默认 16:9）
4. 组装参考图 URL 作为 image 参数
5. 调用生图 API

## 关键原则

- 不要描述五官/发型/肤色 — 这些由参考图负责，prompt 中写 "same face, same hairstyle" 即可
- 参考图必须传 — 否则无法保证角色一致性
- 固定模板段不要改 — 构图、一致性、风格的描述是反复验证过的
