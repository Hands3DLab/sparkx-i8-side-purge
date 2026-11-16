# SPARKX i8 侧边冲刷 · Hands3DLab

![SPARKX i8 多色打印试片及冲刷废料](docs/images/efact.jpg)

SPARKX i8 的四通道热端主打快速换料。如果切换后冲刷不足，旧颜色可能混进新颜色，刚恢复打印时也可能出现出料不均或起笔缺料。这套预设在回到模型前先做侧边冲刷，给颜色过渡和出料稳定留出余量。[Creality 换色说明](https://wiki.creality.com/en/sparkx/i8/no-prime-tower-mode)

适用于 **SPARKX i8、0.4 mm 喷嘴、PLA** 的实验性 Creality Print 预设。随附试片的每次有效换色会在侧刷处送丝 **15 mm**。可选[带擦料塔](presets/with-tower/)或[无擦料塔](presets/no-tower/)。

[English](README.md) · [图文操作指南](docs/guide.zh-CN.md) · [设计原理](docs/guide.zh-CN.md#4-为什么这样做) · [打印前注意事项](docs/safety.zh-CN.md) · [Hands3DLab 软件](https://hands3dlab.com/soft)

> **仅作开源分享，按现状提供。** 本项目不提供担保、官方技术支持或赔偿承诺。使用者自行判断并承担风险。在适用法律允许的范围内，作者及贡献者不承担设备损坏、人身伤害、打印失败、耗材浪费或其他损失。上机前请阅读[注意事项与免责说明](docs/safety.zh-CN.md)。

两份试片已用 [Creality Print 7.3.2](https://github.com/CrealityOfficial/CrealityPrint/releases/tag/v7.3.2) 切片检查。实际表现取决于设备、固件和耗材。

## 1. 打开试片或导入配置

最快的方法是把[带塔](presets/with-tower/)或[无塔](presets/no-tower/)文件夹里的 `.3mf` **作为项目打开**。试片有六段色带，顶部开放，便于观察内部填充。切片前核对载入的预设。

使用自己的模型时，先打开模型，再选 **File → Import → Import Configs**。导入同一组的 `*-machine.json` 和 `*-process.json`，带塔组还要导入 `*-filament.json`。导入后还需要到 **Prepare** 选择对应预设，尤其是打开了带旧预设的 3MF 时。

![Import Configs 中选中无塔机型和工艺 JSON](docs/images/import-configs.jpg)

![Creality Print 英文准备界面，已打开无塔试片](docs/images/prepare-no-tower.jpg)

![带塔项目的 Prepare 页面](docs/images/prepare-with-tower.jpg)

| 界面控件 | 操作 |
| --- | --- |
| **Printer（打印机）** | 选择后缀为 `PLA Fast` 的 Hands3DLab SPARKX i8 机型，核对 `With Tower` 或 `No Tower` 和 0.4 mm 喷嘴。 |
| **Filament（耗材）** | 核对颜色与料槽映射。带塔时，每个参与换色的槽位选择 `Hands3DLab - SPARKX i8 Generic PLA - Side Purge`，以应用减少塔上冲刷的设置。无塔可用随附项目的 Generic PLA。 |
| **Process（工艺）** | 选择同组、后缀为 `PLA Fast` 的工艺，确认 **Prime tower** 开关符合带塔或无塔方案。 |
| **Slice plate（切片单盘）** | 核对三项预设后执行切片。 |

![Printer 列表中的带塔、无塔和原厂机型](docs/images/select-printer-preset.jpg)

## 2. 核对切片结果

1. 打开 **Preview**，用滑块查看换色层。带塔应看到擦料塔，无塔应只有试片。自定义侧刷动作可能位于常规打印区域外，预览不一定完整显示。

   ![无塔试片 Preview，显示层滑块和 5 次换料](docs/images/preview-no-tower.jpg)


   ![带塔试片 Preview，显示擦料塔和 5 次换料](docs/images/preview-with-tower.jpg)
2. 通过 **Export G-code** 导出，在文本编辑器中找单独一行的 `I8_SIDE_PURGE_BEGIN`，避免把文件设置里的模板副本计入。随附试片应有 **五个**代码块。每段的 `T` 换料后，在 `M83` 相对挤出模式下有 `G1 E10` 和 `G1 E5` 两段送丝。实际进给速度随耗材预设变化。带塔版还应在 `I8_TOWER_RETURN` 后看到带 `F24000` 的 XY 移动。

   ![导出 G-code 时的文件命名栏](docs/images/export-gcode.jpg)
3. 少了侧刷块时，先检查当前机型和工艺。无塔路径取决于 Creality Print 如何安排换色。换模型或固件后，根据实际导出的 G-code 重新核对再上机。

![带塔 G-code 节选，带塔试片的实际切片节选，标出换料、两段送丝和回塔指令。](docs/images/gcode-check.svg)

## 3. 调整侧边冲刷或恢复原配置

1. 在 **Prepare** 点击机型旁的铅笔，进入 **Machine gcode → Change filament G-code**。对应的 `*-change-filament.txt` 可以整段粘贴到这个字段，末尾的 `STOCK` 注释区用于对照。

   ![Printer settings 中的 Machine G-code 标签](docs/images/machine-gcode.jpg)
2. 搜索活动代码中的 `EDIT SIDE_PURGE_MM`，把 `G1 E{15 - 10}` 里的 `15` 改为所需的总送丝长度，单位是毫米。第一段固定送 10 mm，因此总量要大于 10。带塔耗材的塔上最小清理量 **12 mm³** 是独立的体积参数。

   ![侧边冲刷排出的废料示例](docs/images/flush.jpg)

3. 用 **Save as** 另存为新预设，再切片并重复核对。要恢复出厂行为，重新选择原机型、工艺和耗材预设，再生成新文件。

   ![Save preset 对话框](docs/images/save-preset-as.jpg)

## MIT License

Hands3DLab 原创内容采用 [MIT 许可证](https://opensource.org/license/mit)。Copyright © 2026 Hands3DLab。随附的上游 G-code 沿用原许可。 [Creality Print v7.3.2 上游源码](https://github.com/CrealityOfficial/CrealityPrint/tree/v7.3.2)
