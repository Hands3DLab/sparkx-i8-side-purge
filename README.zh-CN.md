# SPARKX i8 侧边冲刷

[English](README.md) · [Hands3DLab 软件](https://hands3dlab.com/soft)

## 1. 为什么会串色，侧边冲刷有什么效果

在 **Creality Print 7.3.2** 和 SPARKX i8 现有的四通道快速换料方案下，换料后热端仍可能残留上一种颜色。如果恢复打印前的冲刷量不足，尤其是深色换浅色时，残色可能混入新料并出现在模型上。这个模板在喷嘴回到模型或擦料塔之前，先到侧刷处送丝 **15 mm（10 + 5 mm）**，减少换色初段的串色。

<img src="docs/images/result-effect.jpg" alt="默认换料与侧边冲刷试片并排对照，下方显示各自废料" width="768">

**图 1　双色试片。** 左侧是默认换料，黄色顶层网格可见粉色残留和不规则线条。右侧是替换换料 G-code 后的试片，黄色网格更连续。下方是各自排出的废料。

<img src="docs/images/flush.jpg" alt="手持一小段黄橙色侧边冲刷废料" width="768">

**图 2　侧刷废料近照。** 换色初段挤出的耗材在侧刷处被刮下。模板里的 **15 mm** 指送入热端的耗材长度。擦料塔的冲刷体积由当前工艺和耗材预设控制。

## 2. 安装与验证

适用配置为 **SPARKX i8、0.4 mm 喷嘴、PLA**。随附试片已用 Creality Print 7.3.2 切片检查。[Creality Print 7.3.2](https://github.com/CrealityOfficial/CrealityPrint/releases/tag/v7.3.2)

**强烈建议直接粘贴 G-code，只替换「换料 G-code」字段。** 从当前官方机型预设另存副本，可保留该版本的运动、温控和其他机器默认值。升级后，从新版官方预设重新建副本，再核对模板和切片结果，可减少旧预设覆盖新版设置的风险。

1. 在 **Prepare** 选择官方 **SPARKX i8 0.4 mm**，点击机型旁的铅笔，进入 **Machine G-code → Change filament G-code**。先备份原字段内容。
2. 按 **Prime tower** 开关选模板：[带擦料塔 G-code](gcode/sparkx-i8-with-tower-change-filament.txt) · [无擦料塔 G-code](gcode/sparkx-i8-no-tower-change-filament.txt)。复制文件全文，替换字段，并用 **Save as** 保存为新的用户机型预设。

   <img src="docs/images/machine-gcode.png" alt="标出的换料 G-code 字段和设为 0 秒的 Time flush interval" width="768">

   **图 3　换料 G-code 设置。** 上方红框是粘贴位置。下方显示随附预设的 **Time flush interval 为 0 秒**。若定时冲刷接管换料，此模板会跳过侧刷。

3. 用新预设切片，在 **Preview** 核对换色及擦料塔，再通过 **Export G-code** 检查实际换色段是否含有单独一行 `; I8_SIDE_PURGE_BEGIN`，以及之后的 `G1 E10` 和 `G1 E5`。随附试片应有五段侧刷代码。无塔模式取决于切片器是否调用换料模板。

[带塔试片和预设](presets/with-tower/) · [无塔试片和预设](presets/no-tower/) · [图文操作与冲刷量调整](docs/guide.zh-CN.md)

## 3. 风险与注意事项

- **上机前检查侧刷路径和料槽映射。** 自定义移动会到达 `X266` 和 `X277`，预览可能无法显示完整动作。更换固件或升级切片器后，重新切片并检查导出的代码。
- **首印用小试片，全程看护。** 清理侧刷及废料区，遇到碰撞、异响或换料失败时立即停机。恢复默认行为时，选回原预设并重新切片。
- 项目按现状提供。使用前请阅读[完整注意事项与免责说明](docs/safety.zh-CN.md)。

## MIT License

Copyright © 2026 Hands3DLab。原创内容采用 [MIT 许可证](https://opensource.org/license/mit)。随附的上游 G-code 沿用原许可。[Creality Print 上游源码](https://github.com/CrealityOfficial/CrealityPrint/tree/v7.3.2)
