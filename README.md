# IP Library Workflow

> 一套完整的IP角色库管理与AI生图工作流，供AI Agent/用户快速建立IP库、生成角色设定图、组合风格生图。

## 仓库结构

```
ip-library-workflow/
├── README.md              # 本文件
├── workflow.md            # 完整工作流程（核心文件）
├── templates/
│   ├── README.md          # IP的README模板
│   └── 设定集.md           # 角色设定集模板
├── scripts/
│   └── reference.py       # 参考图处理脚本（裁剪/白边填充）
└── ip-character-sheet/    # 角色设定图生成模板（子模块）
    ├── template.md        # 设定图prompt模板
    └── variables.md       # 变量速查手册
```

## 快速开始

1. 阅读 `workflow.md` 了解完整流程
2. 参照 `templates/` 下的模板创建IP
3. 用 `ip-character-sheet/template.md` 生成角色设定图

## 关键路径

- **IP库路径**：`~/Desktop/ip_library/`（桌面IP文件夹）
- **风格库路径**：`repo_style_source/`（仓库内的风格库）
- **在线图库**：https://yy12321-bay.github.io/style-source/ip_gallery/index.html
