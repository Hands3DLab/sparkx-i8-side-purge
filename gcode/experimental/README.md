# PLA 擦料试验 / PLA wipe trial

适用于 SPARKX i8、0.4 mm 喷嘴和 PLA。用于试验减少侧刷废料被喷嘴带回擦料塔或模型的情况。已通过 Creality Print 7.3.2 切片检查，实机效果待验证。

在机型副本的 **Machine G-code → Change filament G-code** 中粘贴对应 TXT 的全文，另存并重新切片，先用小试片观察数次换色。

- [带擦料塔 / With tower](sparkx-i8-with-tower-wipe-trial.txt)
- [无擦料塔 / No tower](sparkx-i8-no-tower-wipe-trial.txt)

冲刷后按当前预设的换料回抽长度卸压，PLA 风冷由 1.2 秒延长到 1.8 秒，擦拭由两次增加到三次，末次离开擦片的速度为 100 mm/s。风扇在擦拭结束后恢复原先的 70。带塔版在回到塔上后补回等量回抽，无塔版由切片器后续恢复出料。随附预设的回抽为 0.8 mm，设为 0 时回抽部分不会起作用。

这些动作会增加换色时间。试打时同时观察挂料是否减少，以及回塔或回模型的第一条线是否缺料。擦片上的废料堆积也应检查。

For SPARKX i8, a 0.4 mm nozzle, and PLA. These templates are intended to reduce flush waste being carried back to the tower or model. They have passed slicing checks in Creality Print 7.3.2. Physical print results are pending.

Paste the matching TXT into **Machine G-code → Change filament G-code** in a copy of your printer preset, save it, and reslice. Start with a small test and observe several color changes.

After flushing, the template retracts by the preset tool-change retract length, extends PLA cooling from 1.2 to 1.8 seconds, adds a third wipe, and makes the final departure from the wiper at 100 mm/s. The fan returns to 70 after wiping. With a tower, the same retract length is restored after reaching the tower. Without a tower, the slicer handles the subsequent recovery. The supplied presets use a 0.8 mm retract; a setting of zero disables this part of the trial.

The extra moves increase change time. Check both waste pickup and the first line after returning for under-extrusion. Check the wiper for accumulated waste as well.
