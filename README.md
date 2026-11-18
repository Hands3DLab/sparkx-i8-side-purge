# SPARKX i8 Side Purge

[简体中文](README.zh-CN.md) · [Hands3DLab Software](https://hands3dlab.com/soft)

**[v0.1 for Creality Print 7.3.2](https://github.com/Hands3DLab/sparkx-i8-side-purge/releases/download/v0.1-for-CrealityPrint-7.3.2/Hands3DLab-SPARKX-i8-Side-Purge-v0.1-for-CrealityPrint-7.3.2.zip)** · Download ZIP

## 1. Why color bleed can occur and how side flushing helps

With **Creality Print 7.3.2** and the SPARKX i8’s current four-channel filament-change design, some of the previous color can remain in the hotend after a switch. If too little filament is flushed before printing resumes, the old color can show on the model, especially when switching from dark to light. To reduce color bleed, this template feeds **15 mm of filament (10 + 5 mm)** at the side wiper before the nozzle returns to the model or prime tower.

> [!WARNING]
> **Time cost.** Side flushing adds roughly **6 seconds per color change** when it runs, including about **1 extra second** for the improved wipe compared with the previous template. These are estimates; actual time varies. The extra time adds up on prints with frequent changes. If print time is a priority, skip both the preset import and the side-flush template.

<img src="docs/images/result-effect.jpg" alt="Default and side-flush test prints side by side, with the corresponding waste below" width="768">

**Figure 1. Two-color test prints.** The default filament change on the left leaves more pink and irregular lines in the yellow top grid. The coupon on the right uses the replacement G-code and shows a more continuous yellow grid. The corresponding waste is shown below each coupon.

<img src="docs/images/flush.jpg" alt="A small piece of yellow and orange flush waste held in front of the printer" width="768">

**Figure 2. Side flush waste.** The wiper removes the filament extruded at the start of the color transition. The template’s **15 mm** refers to filament feed length. The selected process and filament presets still control the flush volume at the prime tower.

## 2. Install and verify

For the **SPARKX i8 with a 0.4 mm nozzle and PLA**. The supplied test projects were sliced in Creality Print 7.3.2. [Creality Print 7.3.2](https://github.com/CrealityOfficial/CrealityPrint/releases/tag/v7.3.2)

### Option A · Manual replacement (recommended)

Save a copy of the current official printer preset and replace the **Change filament G-code** field. This preserves the current motion, temperature, and other machine defaults. After a slicer upgrade, start with a fresh copy of the updated official preset and verify the template with a new slice.

1. In **Prepare**, select the official **SPARKX i8 0.4 mm** preset. Click the pencil next to it and open **Machine G-code → Change filament G-code**. Back up the existing field.
2. Choose the template that matches **Prime tower**: [With-tower G-code](gcode/sparkx-i8-with-tower-change-filament.txt) · [No-tower G-code](gcode/sparkx-i8-no-tower-change-filament.txt). Copy the whole file into the field, then use **Save as** to create a user printer preset.

   <img src="docs/images/machine-gcode.png" alt="Highlighted Change filament G-code field and Time flush interval set to 0 seconds" width="768">

   **Figure 3. Filament-change G-code settings.** Paste into the upper highlighted field. The lower box shows the supplied preset’s **Time flush interval of 0 seconds**. The template skips the side flush when timed flushing handles the tool change.

**Recommended settings.** To reproduce the supplied test setup, set **Time flush interval** to **0 seconds** in the printer preset copy and match **Prime tower** to the template you chose. The bundled with-tower filament preset uses **0 mm³ extra pre-flush** and a **12 mm³ minimum tower flush**. With manual replacement, start with your existing filament preset and adjust tower flushing only after checking the slice.

### Option B · One-click import

For a quick test, open the `.3mf` in the [with-tower](presets/with-tower/) or [no-tower](presets/no-tower/) folder as a project to load the bundled settings. For your own model, use **File → Import → Import Configs** to select the matching printer and process JSON files together. Include the filament JSON for the with-tower setup. In **Prepare**, select the imported presets and check the prime tower and filament slots.

<img src="docs/images/import-configs-menu.png" alt="Creality Print File → Import menu with Import Configs highlighted" width="768">

**Figure 4. Import presets.** Choose **Import Configs…** from **File → Import**.

### Verify the slice

Reslice after either setup. Check the color changes and prime tower in **Preview**. Use **Export G-code** and check the actual tool changes for a standalone `; I8_SIDE_PURGE_BEGIN` line followed by `G1 E10` and `G1 E5`. The supplied coupons should show five side flush blocks. Without a tower, side flushing depends on the slicer invoking the filament-change template.

[With-tower test project and presets](presets/with-tower/) · [No-tower test project and presets](presets/no-tower/) · [Illustrated steps and flush adjustments](docs/guide.en.md)

**v0.1** includes the improved wipe in both templates and all bundled presets: pressure relief after flushing, 1.8 seconds of PLA cooling, three wipes, and a slower final departure. The with-tower template restores the retracted filament at the tower; the no-tower template leaves recovery to the slicer. The maintainer reports reduced waste pickup in a print test; results vary with filament and wiper condition.

## 3. Risks and precautions

- **Unify assignments before slicing when regions use the same physical filament.** The template detects changes using logical filament IDs at slice time. Mapping multiple logical filaments to one physical slot only when sending the print can still leave side-flush moves in the generated G-code. Assign those regions to the same logical filament in **Prepare**, then reslice.
- **Check the wiper path and filament-slot mapping before printing.** The custom moves reach `X266` and `X277`. Preview may omit some of these moves. Reslice and inspect the exported code after a firmware or slicer upgrade.
- **Supervise the first small test.** Clear the side wiper and waste area. Stop if you notice a collision, unusual noise, or a failed filament change. To restore default behavior, select the original presets and slice again.
- The project is provided as is. Read the [full safety and liability notice](docs/safety.en.md) before printing.

## MIT License

Copyright © 2026 Hands3DLab. Original contributions are available under the [MIT License](https://opensource.org/license/mit). Bundled upstream G-code retains its original license. [Creality Print upstream source](https://github.com/CrealityOfficial/CrealityPrint/tree/v7.3.2)
