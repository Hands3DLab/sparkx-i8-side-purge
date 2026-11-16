# SPARKX i8 侧边冲刷 · Hands3DLab

![SPARKX i8 多色打印试片及冲刷废料](docs/images/efact.png)

SPARKX i8 的四通道热端主打快速换料。如果切换后冲刷不足，旧颜色可能混进新颜色，刚恢复打印时也可能出现出料不均或起笔缺料。这套预设在回到模型前先做侧边冲刷，给颜色过渡和出料稳定留出余量。[Creality 换色说明](https://wiki.creality.com/en/sparkx/i8/no-prime-tower-mode)

适用于 **SPARKX i8、0.4 mm 喷嘴、PLA** 的实验性 Creality Print 预设。随附试片的每次有效换色会在侧刷处送丝 **15 mm**。可选[带擦料塔](presets/with-tower/)或[无擦料塔](presets/no-tower/)。

[English](README.md) · [图文操作指南](docs/guide.zh-CN.md) · [设计原理](docs/guide.zh-CN.md#4-为什么这样做) · [打印前注意事项](docs/safety.zh-CN.md) · [Hands3DLab 软件](https://hands3dlab.com/soft)

> **仅作开源分享，按现状提供。** 本项目不提供担保、官方技术支持或赔偿承诺。使用者自行判断并承担风险。在适用法律允许的范围内，作者及贡献者不承担设备损坏、人身伤害、打印失败、耗材浪费或其他损失。上机前请阅读[注意事项与免责说明](docs/safety.zh-CN.md)。

1. **试打：** 在 Creality Print 中将对应 `.3mf` 作为项目打开，点击 **Slice plate（切片单盘）**。
2. **用于自己的模型：** 用 **File → Import → Import Configs** 导入配置，在 **Prepare** 分别选中同组机型和工艺。带塔方案还需为每个参与换色的槽位选择随附的 PLA 耗材预设。
3. **核对：** 查看 **Preview** 并检查导出的 G-code。首次使用请现场看护小样打印。

两份试片已用 [Creality Print 7.3.2](https://github.com/CrealityOfficial/CrealityPrint/releases/tag/v7.3.2) 切片检查。实际表现取决于设备、固件和耗材。

## MIT License

Hands3DLab 的原创内容采用 MIT 许可。随附的预设含 Creality Print 上游 G-code，其原有许可继续适用。 [Creality Print v7.3.2 上游源码](https://github.com/CrealityOfficial/CrealityPrint/tree/v7.3.2)

Copyright (c) 2026 Hands3DLab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
