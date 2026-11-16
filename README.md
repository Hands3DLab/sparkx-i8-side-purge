# SPARKX i8 Side Purge · Hands3DLab

![SPARKX i8 multicolor test prints and purge waste](docs/images/efact.png)

The SPARKX i8's four-channel hotend is designed for fast filament changes. If the purge is too short for a given change, the previous color can bleed into the next one and extrusion can restart unevenly or leave gaps. These presets purge at the side before printing resumes on the model, giving the color and flow time to settle. [Creality's color change guide](https://wiki.creality.com/en/sparkx/i8/no-prime-tower-mode)

Experimental Creality Print presets for the **SPARKX i8 with a 0.4 mm nozzle and PLA**. Each eligible color change on the supplied test plates purges **15 mm of filament** at the side wiper. Choose [With tower](presets/with-tower/) or [No tower](presets/no-tower/).

[简体中文](README.zh-CN.md) · [Illustrated guide](docs/guide.en.md) · [Design rationale](docs/guide.en.md#4-why-it-works-this-way) · [Before printing](docs/safety.en.md) · [Hands3DLab Software](https://hands3dlab.com/soft)

> **Open-source release, provided as is.** No warranty, official support, or compensation is offered. Use is at your own risk. To the extent permitted by applicable law, the authors and contributors are not liable for equipment damage, injury, failed prints, wasted material, or other loss. Read the [safety and liability notice](docs/safety.en.md) before printing.

1. **Try it:** Open the matching `.3mf` as a project in Creality Print, then click **Slice plate**.
2. **Use your own model:** Use **File → Import → Import Configs**. In **Prepare**, select the matching printer and process presets. With tower also requires the included PLA filament preset on each participating slot.
3. **Verify:** Review **Preview** and the exported G-code. Start with a small, supervised test.

Both test plates were checked in [Creality Print 7.3.2](https://github.com/CrealityOfficial/CrealityPrint/releases/tag/v7.3.2). Hardware behavior depends on the printer, firmware, and filament.

## MIT License

Hands3DLab’s original contributions are under the MIT License. The presets include upstream Creality Print G-code under its original license. [Creality Print v7.3.2 upstream source](https://github.com/CrealityOfficial/CrealityPrint/tree/v7.3.2)

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
