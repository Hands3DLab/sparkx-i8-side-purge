# 同色跨层出现侧边冲刷

## 用户反馈

同一耗材通道在不同层连续打印时仍观察到侧边冲刷。预期是只在实际切换耗材通道时执行侧刷。

## 排查与修复

换料模板已有 previous_extruder 与 next_extruder 不同的判断。旧预设同时保留了官方 Time flush G-code，构成独立的冲刷路径。手动安装时仅替换换料模板，也可能保留官方的定时冲刷设置。

本次将带塔与无塔 JSON 及两份 3MF 中的 Time flush interval 固定为 0，清空 Time flush G-code，并同步更新双语安装说明。独立换料模板继续保留通道切换条件及 15 mm 送丝。

Creality Print 7.3.2 的定时冲刷逻辑检查时间间隔和脚本内容，非换料节点也能触发。因此同时关闭间隔和脚本，避免这条路径触发同通道冲刷。[上游 GCode.cpp](https://github.com/CrealityOfficial/CrealityPrint/blob/v7.3.2/src/libslic3r/GCode.cpp)

## 验证状态

自动检查已通过，覆盖两份 JSON、两份 3MF 的两处内嵌设置，以及独立换料模板与预设的一致性。

尚需用发生问题的原始项目或导出的 G-code 确认这次异常的具体触发路径，并完成重新切片与实机验证。同色但映射到不同料槽时，模板仍按通道变化执行冲刷。
