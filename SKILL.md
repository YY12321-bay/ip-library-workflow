# IP Library 全流程技能

## 一、IP库结构

### 桌面源（用户操作处）
```
~/Desktop/ip_library/
├── _index.md                    # 索引表格
├── auto_sync_ip.bat             # 手动同步批处理
├── auto_sync.log                # 同步日志
├── 喜猫/                        # 每个IP一个文件夹
│   ├── reference.jpg            # 原图（最长边1200px，保持比例）
│   ├── reference_square.jpg     # 方形图（800×800，白边填充不裁剪，API传参用）
│   ├── reference_thumb.jpg      # 缩略图（400×400，白边填充）
│   ├── character_sheet.jpg      # 角色设定图（可选，AI生成的多角度设定板）
│   ├── README.md                # IP描述+prompt规范
│   └── 设定集.md                 # 角色设定文档（6章节）
├── 电视/
│   └── ... (同上)
└── 迅雷/
    └── ... (同上)
```

### 仓库镜像（GitHub Pages部署用）
```
repo_style_source/ip_gallery/
├── index.html                   # 在线图库页面
├── 喜猫/ → 镜像自桌面源
├── 电视/ → 镜像自桌面源
└── 迅雷/ → 镜像自桌面源
```

## 二、IP字段定义

每个IP有5个关键字段，存储在 `README.md` 的表格中：

| 字段 | 说明 | 示例 |
|------|------|------|
| **品牌** | 所属品牌 | 喜马拉雅 |
| **产品场景** | 业务场景标签 | 音频内容、播客、有声书 |
| **风格** | 视觉风格定位 | 3D可爱卡通 |
| **参考图** | 图片路径 | `reference_square.jpg` |
| **角色名** | 文件夹名 | 喜猫 |

`设定集.md` 包含6章节：基础信息、视觉设定(含色值表)、角色性格、常用姿态、场景适应性、生图规范

## 三、完整工作流程

### 阶段A：新增IP

```
用户放入图片 → 自动/手动处理 → 同步上线
```

**方式一：自动（推荐）**
1. 把图片放入 `~/Desktop/ip_library/新IP名\`
2. 定时任务 `AutoSyncIPGallery`（每5分钟）自动检测：
   - 检测到新文件夹 → 裁剪图片（白边填充）→ 生成README → 更新索引
   - 同步到repo → git push → GitHub Pages 部署

**方式二：脚本**
```bash
cd repo_style_source
python scripts/add_ip.py <IP名> <品牌> <风格> <图片路径>
```

**方式三：手动（由我处理）**
1. 读取图片 → 裁剪三张图：
   - `reference.jpg`：最长边1200px，保持比例，quality 85
   - `reference_square.jpg`：800×800，白边填充不裁剪，quality 85
   - `reference_thumb.jpg`：400×400，白边填充，quality 75
2. 创建 `README.md`（含品牌、产品场景、风格、参考图片段）
3. 创建 `设定集.md`（6章节角色文档）
4. 更新 `_index.md` 索引表格
5. 运行同步脚本上线

### 阶段B：生成角色设定图（Character Sheet）

```
读取template → 替换IP名 → 传参考图 → gpt-image-2生图 → 处理入库
```

**模板来源**：`skills/ip-character-sheet/template.md`
或 GitHub raw：`https://raw.githubusercontent.com/malongan/ip-character-sheet-template/main/template.md`

**Prompt结构**：
```
Cinematic, art book style character identity sheet for [IP_NAME].

不对称构图：大全身正面 + 多视角环绕（背面、侧面、坐姿、俯仰等）
锁定一致性：same face, same proportions, same costume
艺术元素：剪影区 + 表情区 + 细节区
风格：极简主义，纯白/米白背景，无环境无道具
标注：角色ID信息块 + 手写标签
[Aspect_ratio]

Maintain IP identity and consistency: strictly follow the reference character...
```

**调用参数**：
| 参数 | 值 |
|------|-----|
| model | `gpt-image-2`（**不可换**） |
| size | `960x1280`（3:4） |
| image | `reference_square.jpg` 的 base64 |
| image_strength | 0.3 |

**API断连处理**：报告用户"API不可用"，等用户说继续再试。不重试、不换模型。

**生成后处理**：
1. 下载PNG → 转RGB → 最长边≤1200px → 存为JPG quality 90
2. 复制到 `ip_gallery/{IP}/character_sheet.jpg` 和桌面 `ip_library/{IP}/`
3. 更新 `设定集.md` 顶部添加角色设定图章节
4. 运行同步脚本上线

### 阶段C：IP × 风格组合生图

**公式**：
```
{风格描述}，{产品场景}，{角色动作表情}，{道具/元素}
Maintain IP identity and consistency throughout.
```

**步骤**：
1. 从IP库读取 `reference_square.jpg` → base64 → `image[0]`
2. 从IP的README获取**产品场景**字段
3. 从 `repo_style_source/styles/` 找到风格模板，填写变量
4. 组合prompt + 固定句
5. 调用 gpt-image-2

## 四、关键脚本

| 脚本 | 路径 | 功能 |
|------|------|------|
| `sync_ip_library.py` | `scripts/sync_ip_library.py` | 桌面IP库 → repo 镜像同步，生成 JSON 数据 |
| `auto_sync_ip.py` | `scripts/auto_sync_ip.py` | 自动巡检新IP，处理图片+推送 |
| `add_ip.py` | `scripts/add_ip.py` | 一键添加新IP |

## 五、部署

```
1. cd repo_style_source
2. git add -A && git commit -m "..."
3. git push origin main
4. git checkout style-source
5. git merge main --no-edit
6. git push origin style-source
7. git checkout main
```

在线图库：https://yy12321-bay.github.io/style-source/ip_gallery/index.html
风格画廊：https://yy12321-bay.github.io/style-source/gallery.html

## 六、铁律（不可违反）

1. **模型只能用 `gpt-image-2`**，不得换任何其他模型
2. **API断连就停**，等用户说继续再重试，不擅自重试或换模型
3. **禁止本地文案排版**，所有文字交给API生成
4. **禁止擅自做决定**，偏离常规的操作先问用户

## 七、经验教训

### JSON数据同步
- `sync_ip_library.py` 新增字段后，必须重新运行生成JSON，再commit
- GitHub Pages 部署有延迟（1-3分钟），部署失败可重新触发（empty commit）

### 路径编码
- Windows路径含中文时，Python脚本需 `set PYTHONIOENCODING=utf-8`
- 图库链接需用 `encodeURIComponent()` 处理中文文件夹名

### 卡片交互
- 卡片内有下拉菜单时，外层容器不能设 `overflow: hidden`
- 圆角裁剪改到子容器（如 `.img-wrap`）上
