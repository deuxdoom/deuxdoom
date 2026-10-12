<a id="top"></a>

<div align="center">

<picture>
  <source media="(max-width: 640px)" srcset="assets/hero-compact.svg">
  <img src="assets/hero.svg" width="100%" alt="DEUXDOOM — Independent Software Engineering. Desktop Applications, Automation, Developer Utilities. Practical software. Thoughtful engineering.">
</picture>

<p><br><img src="assets/typing.svg" alt="Engineering practical software · Building Windows desktop applications · Automation & developer utilities · Shipping better desktop experiences"></p>

<p>
  <a href="#about"><b>About</b></a> &nbsp;·&nbsp;
  <a href="#software"><b>Software</b></a> &nbsp;·&nbsp;
  <a href="#toolbox"><b>Toolbox</b></a> &nbsp;·&nbsp;
  <a href="#insights"><b>Insights</b></a> &nbsp;·&nbsp;
  <a href="#releases"><b>Releases</b></a> &nbsp;·&nbsp;
  <a href="#connect"><b>Connect</b></a>
</p>

</div>

<a id="about"></a>

## 02 · About

I build practical desktop applications and developer utilities, focusing on reliable functionality, thoughtful interfaces, and everyday usability.

I work independently and take each app from design through implementation, debugging, release and maintenance. Since August 2025 that has produced seven Windows applications, from media downloaders and a GIF tool for controller screens to hardware diagnostics, an image upscaler and tray utilities. Each one ships through GitHub Releases with its own project site, a changelog and a built-in updater.

| Principle | How it shows up in the software |
|:--|:--|
| **Usability** | Sensible defaults, drag-and-drop input, and localized interfaces (up to 13 languages) |
| **Reliability** | SHA-256 verified in-app updates with rollback, and failures that are reported instead of silently papered over |
| **Performance** | GPU paths where they matter (NVENC, Vulkan), a dedicated C++ timing thread for polling-rate tests, and measured UI work such as a history search cut from 1,143 ms to 56 ms |
| **Maintainability** | Portable apps with documented settings and backup files, and a changelog kept for every project |
| **Iterative improvement** | Small, frequent releases shaped by real use and issue reports, visible in the [release activity](#insights) below |

<a id="software"></a>

## 03 · Featured Software

Seven Windows applications, numbered in priority order. Six are free, closed-source releases whose repositories hold documentation, changelogs and binaries; one is an open-source (MIT) fork.

<a id="tver-downloader"></a>

### 01 · TVer Downloader

**Windows downloader for Japan's TVer streaming service**

<a href="https://github.com/deuxdoom/TVerDownloader"><img align="right" width="440" src="assets/projects/01-tver-downloader.png" alt="TVer Downloader main window in dark theme, showing the download queue and log panel"></a>

A PyQt6 desktop app that saves TVer episodes, and YouTube videos, through yt-dlp and FFmpeg, built around a resumable, series-aware download queue.

- Single, multi-URL and whole-series downloads with 1–20 concurrent jobs and parallel fragment fetching
- Keeps yt-dlp and FFmpeg up to date; optional AVC / HEVC re-encoding with NVIDIA NVENC
- Japanese subtitles embedded or saved as VTT / SRT; favorites, history and tray progress
- Region check that re-runs when the network changes, and 7 UI languages that switch without a restart

<b>Stack</b>&nbsp; `Python` `PyQt6` `yt-dlp` `FFmpeg` `NVENC`<br>
<b>Distribution</b>&nbsp; Freeware · Windows 10/11 x64 · source not published<br>
<b>Latest</b>&nbsp; <a href="https://github.com/deuxdoom/TVerDownloader/releases/latest"><img align="absmiddle" src="assets/generated/release-tver-downloader.svg" alt="Latest stable release of TVer Downloader"></a>

[![Repository](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/TVerDownloader) [![Download](assets/ui/btn-download.svg)](https://github.com/deuxdoom/TVerDownloader/releases/latest) [![Website](assets/ui/btn-website.svg)](https://deuxdoom.github.io/TVerDownloader/)

<br clear="right">

<a id="chzzk-downloader"></a>

### 02 · ChzzkDownloader

**Multi-site video downloader built around CHZZK**

<a href="https://github.com/deuxdoom/ChzzkDownloader"><img align="right" width="440" src="assets/projects/02-chzzk-downloader.png" alt="ChzzkDownloader channel view with selectable VOD thumbnails"></a>

Saves CHZZK VODs and clips, as well as YouTube, Instagram, TVer and other supported sites, as MP4, with channel-centric browsing for CHZZK.

- Batch queue with up to 4 videos at once and 16 fragments per video, restored across restarts
- Channel favorites with thumbnail browsing; followed channels imported from a linked account
- Cookie-based account linking with encrypted local storage (no ID or password entry) and multiple profiles
- Keeps the original by default, with optional H.264 / H.265 on CPU or NVENC, and SHA-256 verified self-updates

<b>Stack</b>&nbsp; `Python` `PySide6` `yt-dlp` `FFmpeg` `NVENC`<br>
<b>Distribution</b>&nbsp; Free for personal use · Windows 10/11 x64 · source not published<br>
<b>Latest</b>&nbsp; <a href="https://github.com/deuxdoom/ChzzkDownloader/releases/latest"><img align="absmiddle" src="assets/generated/release-chzzk-downloader.svg" alt="Latest stable release of ChzzkDownloader"></a>

[![Repository](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/ChzzkDownloader) [![Download](assets/ui/btn-download.svg)](https://github.com/deuxdoom/ChzzkDownloader/releases/latest) [![Website](assets/ui/btn-website.svg)](https://deuxdoom.github.io/ChzzkDownloader/)

<br clear="right">

<a id="shadowplay-notifier"></a>

### 03 · ShadowPlay Notifier

**Recording status display for a second monitor**

<a href="https://github.com/deuxdoom/Shadowplay-Notifier"><img align="right" width="440" src="assets/projects/03-shadowplay-notifier.png" alt="ShadowPlay Notifier recording screen with elapsed time, file size and bitrate"></a>

Shows NVIDIA ShadowPlay recording status in large type on a secondary monitor, and turns into a clock, weather and now-playing wallpaper while idle.

- Detects recording by watching file growth and write handles in the capture folder: read-only, with no hooks into the recorder
- Elapsed time, file size, bitrate and file name, updated within one polling interval (0.5 s by default)
- Idle wallpaper with clock, Open-Meteo weather, Spotify now-playing, a 24-band audio visualizer and the moon phase
- Single portable EXE that pauses rendering while hidden in the tray, with SHA-256 checked in-app updates

<b>Stack</b>&nbsp; `Python` `Tkinter` `PyInstaller` `Open-Meteo`<br>
<b>Distribution</b>&nbsp; Freeware · Windows 10/11 · source not published<br>
<b>Latest</b>&nbsp; <a href="https://github.com/deuxdoom/Shadowplay-Notifier/releases/latest"><img align="absmiddle" src="assets/generated/release-shadowplay-notifier.svg" alt="Latest stable release of ShadowPlay Notifier"></a>

[![Repository](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/Shadowplay-Notifier) [![Download](assets/ui/btn-download.svg)](https://github.com/deuxdoom/Shadowplay-Notifier/releases/latest) [![Website](assets/ui/btn-website.svg)](https://deuxdoom.github.io/Shadowplay-Notifier/)

<br clear="right">

<a id="apex-gif-maker"></a>

### 04 · APEX GIF MAKER

**MP4-to-GIF studio for Flydigi APEX controller screens**

<a href="https://github.com/deuxdoom/APEXGIFMAKER"><img align="right" width="440" src="assets/projects/04-apex-gif-maker.png" alt="APEX GIF MAKER with start and end previews, a range timeline and GIF output options"></a>

Turns a moment from any video into an animated GIF sized for the built-in screen of Flydigi APEX-series controllers such as the APEX 4, 5 and 6, processed entirely on the local PC.

- Precise range selection with trim handles, a zoomable timeline and typed timestamps
- Screen-ready output: 160×80 at 12 fps by default, with fill, letterbox or stretch scaling and a crop preview
- GIF quality controls: adaptive palette, dithering, and uniform or duplicate-dropping frame modes
- Auto-managed FFmpeg, SHA-256 verified updates, 6 UI languages and dark / light themes

<b>Stack</b>&nbsp; `Python` `PySide6` `FFmpeg`<br>
<b>Distribution</b>&nbsp; Freeware · Windows 10/11 x64 · source not published<br>
<b>Latest</b>&nbsp; <a href="https://github.com/deuxdoom/APEXGIFMAKER/releases/latest"><img align="absmiddle" src="assets/generated/release-apex-gif-maker.svg" alt="Latest stable release of APEX GIF MAKER"></a>

[![Repository](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/APEXGIFMAKER) [![Download](assets/ui/btn-download.svg)](https://github.com/deuxdoom/APEXGIFMAKER/releases/latest) [![Website](assets/ui/btn-website.svg)](https://deuxdoom.github.io/APEXGIFMAKER/)

<br clear="right">

<a id="gamepad-tester"></a>

### 05 · GamePadTester

**Precision gamepad diagnostics for Windows**

<a href="https://github.com/deuxdoom/GamePadTester"><img align="right" width="440" src="assets/projects/05-gamepad-tester.png" alt="GamePadTester overview with a controller diagram, stick plots and trigger bars"></a>

Measures stick circularity and polling rate with the same methods as gamepad-tester.com and Gamepadla, so results compare directly, and checks buttons, triggers, haptics, gyro and touchpad.

- Stick circularity (RMS error over 32 sectors), drift, resolution and snapback, measured on raw values without an imposed deadzone
- Polling rate timed on a dedicated C++ thread from XInput packets, raw HID reports or SDL, exportable as JSON, CSV or TXT
- Up to four controllers, with layouts for Xbox, DualSense and Switch Pro / ProCon 2, plus adaptive-trigger and rumble tests
- One-click 1000 Hz USB polling for DualSense, 800×400 result cards and SHA-256 verified updates

<b>Stack</b>&nbsp; `Python` `PySide6` `C++20` `SDL3` `XInput` `HID`<br>
<b>Distribution</b>&nbsp; Freeware · Windows 10/11 · source not published<br>
<b>Latest</b>&nbsp; <a href="https://github.com/deuxdoom/GamePadTester/releases/latest"><img align="absmiddle" src="assets/generated/release-gamepad-tester.svg" alt="Latest stable release of GamePadTester"></a>

[![Repository](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/GamePadTester) [![Download](assets/ui/btn-download.svg)](https://github.com/deuxdoom/GamePadTester/releases/latest) [![Website](assets/ui/btn-website.svg)](https://deuxdoom.github.io/GamePadTester/)

<br clear="right">

<a id="image-upscaler"></a>

### 06 · ImageUpscaler

**Portable, offline AI image upscaler**

<a href="https://github.com/deuxdoom/ImageUpscaler"><img align="right" width="440" src="assets/projects/06-image-upscaler.png" alt="ImageUpscaler with an image list, a before/after comparison slider and upscale settings"></a>

Enlarges photos, illustrations, transparent images and pixel art up to 8× on the local PC. One portable EXE bundles the Real-ESRGAN models, codecs and runtime.

- Four modes: Photo AI (Real-ESRGAN x4plus), Image AI (x4plus-anime), linear-light Lanczos, and integer nearest-neighbor for pixel art
- PNG, JPG, WebP and AVIF at 2×, 4× or 8×, with alpha preserved and scaled separately
- Batch list with a before / after comparison slider and zoom
- Vulkan capability check with explicit fallbacks, and SHA-256 verified updates

<b>Stack</b>&nbsp; `C#` `.NET 8` `Windows Forms` `SkiaSharp` `Magick.NET` `Real-ESRGAN (ncnn / Vulkan)`<br>
<b>Distribution</b>&nbsp; Free download · Windows 10/11 x64 · source not published<br>
<b>Latest</b>&nbsp; <a href="https://github.com/deuxdoom/ImageUpscaler/releases/latest"><img align="absmiddle" src="assets/generated/release-image-upscaler.svg" alt="Latest stable release of ImageUpscaler"></a>

[![Repository](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/ImageUpscaler) [![Download](assets/ui/btn-download.svg)](https://github.com/deuxdoom/ImageUpscaler/releases/latest) [![Website](assets/ui/btn-website.svg)](https://deuxdoom.github.io/ImageUpscaler/)

<br clear="right">

<a id="ai-agents-usage-monitor"></a>

### 07 · AI Agents Usage Monitor

**Claude and Codex usage limits in the Windows tray**

<a href="https://github.com/deuxdoom/usage-monitor-for-claude"><img align="right" width="440" src="assets/projects/07-ai-agents-usage-monitor.png" alt="AI Agents Usage Monitor detail popup for Claude and Codex, and the one-line bar mode"></a>

A lightweight tray app that shows Claude and Codex usage limits in real time. It is an extended fork of [jens-duttke/usage-monitor-for-claude](https://github.com/jens-duttke/usage-monitor-for-claude) that adds Codex support, a one-line bar mode and a verified in-app updater.

- Live tray icon for session and weekly limits; detail popup with reset times, plan, credits and per-model token breakdowns from local session logs
- Codex limits read through the official Codex App Server, side by side with Claude
- One-line bar mode next to the clock, time-aware usage colors and threshold alerts
- Portable single EXE, 13 languages, event commands and an in-app updater with rollback

<b>Stack</b>&nbsp; `Python` `pywebview` `pystray` `PyInstaller` `C#`<br>
<b>Distribution</b>&nbsp; Open source (MIT) · fork of jens-duttke/usage-monitor-for-claude · Windows 10/11 x64<br>
<b>Latest</b>&nbsp; <a href="https://github.com/deuxdoom/usage-monitor-for-claude/releases/latest"><img align="absmiddle" src="assets/generated/release-ai-agents-usage-monitor.svg" alt="Latest stable release of AI Agents Usage Monitor"></a>

[![Repository](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/usage-monitor-for-claude) [![Download](assets/ui/btn-download.svg)](https://github.com/deuxdoom/usage-monitor-for-claude/releases/latest) [![Website](assets/ui/btn-website.svg)](https://deuxdoom.github.io/usage-monitor-for-claude/)

<br clear="right">

<sub>TVer, CHZZK, NVIDIA ShadowPlay, Flydigi APEX, DualSense, Claude and Codex are trademarks of their respective owners. These are independent projects, not affiliated with or endorsed by them.</sub>

<a id="toolbox"></a>

## 04 · Engineering Toolbox

Technologies that ship in the releases above, grouped by area. The numbers refer to the Featured projects.

| Area | Stack |
|:--|:--|
| **Languages** | ![Python](https://img.shields.io/badge/Python-172440?style=flat-square&logo=python&logoColor=65D6E6) ![C#](https://img.shields.io/badge/C%23-172440?style=flat-square) ![C++](https://img.shields.io/badge/C%2B%2B-172440?style=flat-square&logo=cplusplus&logoColor=65D6E6) ![JavaScript](https://img.shields.io/badge/JavaScript-172440?style=flat-square&logo=javascript&logoColor=65D6E6)<br><sub>Python 01–05, 07 · C# 06, 07 · C++20 measurement core 05 · JavaScript / HTML / CSS for project sites and the 07 popup UI</sub> |
| **Desktop & runtime** | ![PySide6](https://img.shields.io/badge/PySide6-172440?style=flat-square&logo=qt&logoColor=65D6E6) ![PyQt6](https://img.shields.io/badge/PyQt6-172440?style=flat-square&logo=qt&logoColor=65D6E6) ![Tkinter](https://img.shields.io/badge/Tkinter-172440?style=flat-square) ![Windows Forms](https://img.shields.io/badge/Windows_Forms-172440?style=flat-square) ![pywebview](https://img.shields.io/badge/pywebview-172440?style=flat-square) ![.NET 8](https://img.shields.io/badge/.NET_8-172440?style=flat-square&logo=dotnet&logoColor=65D6E6) ![PyInstaller](https://img.shields.io/badge/PyInstaller-172440?style=flat-square)<br><sub>PySide6 02, 04, 05 · PyQt6 01 · Tkinter 03 · Windows Forms on .NET 8 06 · pywebview and pystray 07 · single-EXE builds with PyInstaller 03, 07</sub> |
| **Media & imaging** | ![FFmpeg](https://img.shields.io/badge/FFmpeg-172440?style=flat-square&logo=ffmpeg&logoColor=65D6E6) ![yt-dlp](https://img.shields.io/badge/yt--dlp-172440?style=flat-square) ![NVIDIA NVENC](https://img.shields.io/badge/NVIDIA_NVENC-172440?style=flat-square&logo=nvidia&logoColor=65D6E6) ![Real-ESRGAN](https://img.shields.io/badge/Real--ESRGAN-172440?style=flat-square) ![Vulkan](https://img.shields.io/badge/Vulkan-172440?style=flat-square&logo=vulkan&logoColor=65D6E6) ![SkiaSharp](https://img.shields.io/badge/SkiaSharp-172440?style=flat-square) ![Magick.NET](https://img.shields.io/badge/Magick.NET-172440?style=flat-square)<br><sub>FFmpeg 01, 02, 04 · yt-dlp 01, 02 · NVENC hardware encoding 01, 02 · Real-ESRGAN through ncnn / Vulkan, SkiaSharp and Magick.NET 06</sub> |
| **Input & hardware** | ![SDL3](https://img.shields.io/badge/SDL3-172440?style=flat-square) ![XInput](https://img.shields.io/badge/XInput-172440?style=flat-square) ![Raw HID](https://img.shields.io/badge/Raw_HID-172440?style=flat-square)<br><sub>Controller input, polling-rate timing and haptics in 05</sub> |
| **Delivery & workflow** | ![Git](https://img.shields.io/badge/Git-172440?style=flat-square&logo=git&logoColor=65D6E6) ![GitHub Releases](https://img.shields.io/badge/GitHub_Releases-172440?style=flat-square&logo=github&logoColor=65D6E6) ![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-172440?style=flat-square&logo=githubpages&logoColor=65D6E6) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-172440?style=flat-square&logo=githubactions&logoColor=65D6E6) ![VS Code](https://img.shields.io/badge/VS_Code-172440?style=flat-square)<br><sub>Every app ships through GitHub Releases with a GitHub Pages site and an in-app updater · GitHub Actions refreshes the data on this profile</sub> |

<a id="insights"></a>

## 05 · GitHub Activity & Insights

<p align="center">
  <img src="assets/generated/insights.svg" width="760" alt="Release insights from public GitHub data: releases published, release downloads, first and latest release, and releases per month for the last 12 months, stacked by project">
</p>

<sub>Generated from the public GitHub REST API by a scheduled workflow (<a href=".github/workflows/refresh-data.yml">refresh-data.yml</a>). Download counts cover GitHub Release assets only.</sub>

<a id="releases"></a>

## 06 · Latest Software Releases

| Project | Latest stable release · date (UTC) |
|:--|:--|
| **01 · [TVer Downloader](https://github.com/deuxdoom/TVerDownloader)** | <a href="https://github.com/deuxdoom/TVerDownloader/releases/latest"><img src="assets/generated/release-tver-downloader.svg" alt="TVer Downloader latest release"></a> |
| **02 · [ChzzkDownloader](https://github.com/deuxdoom/ChzzkDownloader)** | <a href="https://github.com/deuxdoom/ChzzkDownloader/releases/latest"><img src="assets/generated/release-chzzk-downloader.svg" alt="ChzzkDownloader latest release"></a> |
| **03 · [ShadowPlay Notifier](https://github.com/deuxdoom/Shadowplay-Notifier)** | <a href="https://github.com/deuxdoom/Shadowplay-Notifier/releases/latest"><img src="assets/generated/release-shadowplay-notifier.svg" alt="ShadowPlay Notifier latest release"></a> |
| **04 · [APEX GIF MAKER](https://github.com/deuxdoom/APEXGIFMAKER)** | <a href="https://github.com/deuxdoom/APEXGIFMAKER/releases/latest"><img src="assets/generated/release-apex-gif-maker.svg" alt="APEX GIF MAKER latest release"></a> |
| **05 · [GamePadTester](https://github.com/deuxdoom/GamePadTester)** | <a href="https://github.com/deuxdoom/GamePadTester/releases/latest"><img src="assets/generated/release-gamepad-tester.svg" alt="GamePadTester latest release"></a> |
| **06 · [ImageUpscaler](https://github.com/deuxdoom/ImageUpscaler)** | <a href="https://github.com/deuxdoom/ImageUpscaler/releases/latest"><img src="assets/generated/release-image-upscaler.svg" alt="ImageUpscaler latest release"></a> |
| **07 · [AI Agents Usage Monitor](https://github.com/deuxdoom/usage-monitor-for-claude)** | <a href="https://github.com/deuxdoom/usage-monitor-for-claude/releases/latest"><img src="assets/generated/release-ai-agents-usage-monitor.svg" alt="AI Agents Usage Monitor latest release"></a> |

<sub>Read from each repository's GitHub Releases: the newest published release that is not a draft or pre-release. A newer pre-release, if one exists, appears as an extra segment, and a project without a release shows “No published release”. Refreshed every six hours.</sub>

<a id="connect"></a>

## 07 · Connect

- **GitHub** · [@deuxdoom](https://github.com/deuxdoom) · [all repositories](https://github.com/deuxdoom?tab=repositories)
- **Mastodon** · [@deuxdoom@mastodon.social](https://mastodon.social/@deuxdoom)
- **Support** · [GitHub Sponsors](https://github.com/sponsors/deuxdoom)
- **Feedback** · Bug reports and feature requests are welcome in each project's Issues tab.

**Project sites** · [TVer Downloader](https://deuxdoom.github.io/TVerDownloader/) · [ChzzkDownloader](https://deuxdoom.github.io/ChzzkDownloader/) · [ShadowPlay Notifier](https://deuxdoom.github.io/Shadowplay-Notifier/) · [APEX GIF MAKER](https://deuxdoom.github.io/APEXGIFMAKER/) · [GamePadTester](https://deuxdoom.github.io/GamePadTester/) · [ImageUpscaler](https://deuxdoom.github.io/ImageUpscaler/) · [AI Agents Usage Monitor](https://deuxdoom.github.io/usage-monitor-for-claude/)

<br>

<div align="center">

<img src="assets/footer.svg" width="100%" alt="DEUXDOOM — Practical software. Thoughtful engineering.">

<sub><a href="#top">Back to top ↑</a></sub>

</div>
