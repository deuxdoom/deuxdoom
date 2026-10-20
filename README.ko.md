<a id="top"></a>

<p align="right">
  <a href="README.md" title="Read in English"><img src="assets/ui/btn-language-en.svg" width="96" height="32" alt="English"></a>
  <a href="#top" title="한국어"><img src="assets/ui/btn-language-ko-active.svg" width="96" height="32" alt="한국어 — 현재 언어"></a>
</p>

<div align="center">

<picture>
  <source media="(max-width: 640px)" srcset="assets/hero-compact.svg">
  <img src="assets/hero.svg" width="100%" alt="DEUXDOOM — 독립 소프트웨어 개발. 데스크톱 애플리케이션, 자동화, 개발자 유틸리티. 실용적인 소프트웨어와 세심한 설계.">
</picture>

<p><br><img src="assets/typing-ko.svg" alt="실용적인 소프트웨어 개발 · Windows 데스크톱 앱 제작 · 자동화와 개발자 유틸리티 · 더 나은 데스크톱 경험"></p>

<p>
  <a href="#about"><b>소개</b></a> &nbsp;·&nbsp;
  <a href="#software"><b>프&#8288;로&#8288;젝&#8288;트</b></a> &nbsp;·&nbsp;
  <a href="#toolbox"><b>기술</b></a> &nbsp;·&nbsp;
  <a href="#insights"><b>활&#8288;동&nbsp;통&#8288;계</b></a> &nbsp;·&nbsp;
  <a href="#releases"><b>릴&#8288;리&#8288;스</b></a> &nbsp;·&nbsp;
  <a href="#engineering"><b>구&#8288;현&nbsp;사&#8288;례</b></a> &nbsp;·&nbsp;
  <a href="#connect"><b>연락</b></a>
</p>

</div>

<a id="about"></a>

## 02 · 소개

안정적인 기능, 세심한 인터페이스, 일상에서의 사용성을 중심으로 실용적인 데스크톱 애플리케이션과 개발자 유틸리티를 만듭니다.

앱의 설계부터 구현, 디버깅, 배포, 유지보수까지 독립적으로 진행합니다. 2025년 8월부터 영상 다운로더, 컨트롤러 화면용 GIF 도구, 하드웨어 진단, 이미지 뷰어·편집기, 업스케일러, 트레이 유틸리티 등 Windows 앱 8개를 배포했습니다. 각 앱에는 GitHub Releases 배포본, 프로젝트 사이트, 변경 기록이 있습니다.

| 원&#8288;칙 | 소프트웨어에 반영한 방식 |
|:--|:--|
| **사&#8288;용&#8288;성** | 적절한 기본값, 드래그 앤 드롭 입력, 다국어 인터페이스(최대 13개 언어) |
| **안&#8288;정&#8288;성** | SHA-256 검증과 복구 기능을 갖춘 앱 내 업데이트, 실패를 숨기지 않고 알려 주는 오류 처리 |
| **성&#8288;능** | NVENC·Vulkan GPU 처리, 폴링 레이트 측정용 C++ 전용 스레드, 기록 검색을 1,143 ms에서 56 ms로 줄인 측정 기반 개선 |
| **유&#8288;지&#8288;보&#8288;수** | 설정과 백업 파일을 문서화한 포터블 앱, 프로젝트별 변경 기록 |
| **지&#8288;속&#8288;개&#8288;선** | 실제 사용과 이슈 제보를 반영한 작은 단위의 잦은 배포. 아래 [릴리스 활동](#insights)에서 확인할 수 있습니다. |

<a id="software"></a>

## 03 · 주요 소프트웨어

우선순위에 따라 번호를 붙인 Windows 앱 8개입니다. 7개는 무료로 배포하는 소스 비공개 앱으로, 저장소에는 문서·변경 기록·배포 파일을 공개합니다. 나머지 1개는 MIT 라이선스의 오픈소스 포크입니다.

<a id="tver-downloader"></a>

### 01 · TVer Downloader

**일본 TVer 스트리밍 서비스를 위한 Windows 다운로더**

<a href="https://github.com/deuxdoom/TVerDownloader"><img align="right" width="440" src="assets/projects/01-tver-downloader.png" alt="다운로드 대기열과 로그 패널을 보여 주는 TVer Downloader 다크 테마 화면"></a>

yt-dlp와 FFmpeg로 TVer 에피소드와 YouTube 영상을 저장하는 PyQt6 앱입니다. 이어받기와 시리즈 단위 처리를 지원하는 다운로드 대기열을 중심으로 구성했습니다.

- 단일 URL·여러 URL·시리즈 전체 다운로드, 동시 작업 1–20개와 영상 조각 병렬 다운로드
- yt-dlp·FFmpeg 최신 버전 유지, NVIDIA NVENC를 이용한 AVC / HEVC 재인코딩 옵션
- 일본어 자막 내장 또는 VTT / SRT 저장, 즐겨찾기·기록·트레이 진행률
- 네트워크 변경 시 지역 확인 재실행, 재시작 없이 전환하는 7개 UI 언어

<b>기술</b>&nbsp; `Python` `PyQt6` `yt-dlp` `FFmpeg` `NVENC`<br>
<b>배포</b>&nbsp; 프리웨어 · Windows 10/11 x64 · 소스 비공개<br>
<b>최신 버전</b>&nbsp; <a href="https://github.com/deuxdoom/TVerDownloader/releases/latest"><img align="absmiddle" src="assets/generated/release-tver-downloader.svg" alt="TVer Downloader 최신 정식 릴리스"></a>

[![저장소](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/TVerDownloader) [![다운로드](assets/ui/btn-download.svg)](https://github.com/deuxdoom/TVerDownloader/releases/latest) [![웹사이트](assets/ui/btn-website.svg)](https://deuxdoom.github.io/TVerDownloader/)

<br clear="right">

<a id="chzzk-downloader"></a>

### 02 · ChzzkDownloader

**치지직을 중심으로 여러 사이트를 지원하는 영상 다운로더**

<a href="https://github.com/deuxdoom/ChzzkDownloader"><img align="right" width="440" src="assets/projects/02-chzzk-downloader.png" alt="VOD 썸네일을 선택할 수 있는 ChzzkDownloader 채널 화면"></a>

치지직 VOD·클립과 YouTube, Instagram, TVer 등 지원 사이트의 영상을 MP4로 저장합니다. 치지직은 채널별 탐색 화면에서 영상을 골라 받을 수 있습니다.

- 동시 영상 4개·영상 조각 16개를 처리하는 일괄 대기열, 재실행 후 작업 복원
- 썸네일로 탐색하는 채널 즐겨찾기, 연결한 계정의 팔로우 채널 가져오기
- 암호화한 로컬 쿠키 저장과 여러 프로필 지원. 아이디·비밀번호 입력 없이 계정 연결
- 기본값은 원본 유지, CPU / NVENC H.264·H.265 변환 옵션과 SHA-256 검증 업데이트

<b>기술</b>&nbsp; `Python` `PySide6` `yt-dlp` `FFmpeg` `NVENC`<br>
<b>배포</b>&nbsp; 개인·비상업용 무료 · Windows 10/11 x64 · 소스 비공개<br>
<b>최신 버전</b>&nbsp; <a href="https://github.com/deuxdoom/ChzzkDownloader/releases/latest"><img align="absmiddle" src="assets/generated/release-chzzk-downloader.svg" alt="ChzzkDownloader 최신 정식 릴리스"></a>

[![저장소](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/ChzzkDownloader) [![다운로드](assets/ui/btn-download.svg)](https://github.com/deuxdoom/ChzzkDownloader/releases/latest) [![웹사이트](assets/ui/btn-website.svg)](https://deuxdoom.github.io/ChzzkDownloader/)

<br clear="right">

<a id="shadowplay-notifier"></a>

### 03 · ShadowPlay Notifier

**보조 모니터에 크게 표시하는 녹화 상태**

<a href="https://github.com/deuxdoom/Shadowplay-Notifier"><img align="right" width="440" src="assets/projects/03-shadowplay-notifier.png" alt="시계·날씨·재생 중인 음악을 보여 주는 ShadowPlay Notifier 일반 화면"></a>

NVIDIA ShadowPlay 녹화 상태를 보조 모니터에 큰 글자로 표시합니다. 대기 중에는 시계·날씨·재생 중인 음악을 보여 주는 월페이퍼 화면으로 바뀝니다.

- 녹화 폴더의 파일 증가와 쓰기 핸들로 녹화를 감지. 녹화 프로그램에 개입하지 않는 읽기 전용 방식
- 경과 시간·파일 크기·비트레이트·파일 이름 표시, 기본 폴링 주기 0.5초 이내 갱신
- 시계, Open-Meteo 날씨, Spotify 음악, 24밴드 오디오 시각화, 달 위상을 표시하는 대기 화면
- 포터블 EXE 하나로 실행, 트레이에 숨긴 동안 렌더링 중단, SHA-256 검증 앱 내 업데이트

<b>기술</b>&nbsp; `Python` `Tkinter` `PyInstaller` `Open-Meteo`<br>
<b>배포</b>&nbsp; 프리웨어 · Windows 10/11 · 소스 비공개<br>
<b>최신 버전</b>&nbsp; <a href="https://github.com/deuxdoom/Shadowplay-Notifier/releases/latest"><img align="absmiddle" src="assets/generated/release-shadowplay-notifier.svg" alt="ShadowPlay Notifier 최신 정식 릴리스"></a>

[![저장소](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/Shadowplay-Notifier) [![다운로드](assets/ui/btn-download.svg)](https://github.com/deuxdoom/Shadowplay-Notifier/releases/latest) [![웹사이트](assets/ui/btn-website.svg)](https://deuxdoom.github.io/Shadowplay-Notifier/)

<br clear="right">

<a id="apex-gif-maker"></a>

### 04 · APEX GIF MAKER

**Flydigi APEX 컨트롤러 화면을 위한 MP4-to-GIF 도구**

<a href="https://github.com/deuxdoom/APEXGIFMAKER"><img align="right" width="440" src="assets/projects/04-apex-gif-maker.png" alt="시작·끝 미리보기, 구간 타임라인, GIF 출력 옵션을 보여 주는 APEX GIF MAKER"></a>

영상의 원하는 순간을 APEX 4·5·6 등 Flydigi APEX 시리즈 컨트롤러의 내장 화면 크기에 맞는 GIF로 만듭니다. 모든 처리는 로컬 PC에서 이루어집니다.

- 트림 핸들, 확대 가능한 타임라인, 시간 직접 입력으로 정밀한 구간 선택
- 기본 출력 160×80·12 fps, 채우기·레터박스·늘리기와 자르기 미리보기
- 적응형 팔레트·디더링, 균일 프레임 또는 중복 프레임 제거 모드 등 GIF 품질 옵션
- FFmpeg 자동 관리, SHA-256 검증 업데이트, 6개 UI 언어와 다크 / 라이트 테마

<b>기술</b>&nbsp; `Python` `PySide6` `FFmpeg`<br>
<b>배포</b>&nbsp; 프리웨어 · Windows 10/11 x64 · 소스 비공개<br>
<b>최신 버전</b>&nbsp; <a href="https://github.com/deuxdoom/APEXGIFMAKER/releases/latest"><img align="absmiddle" src="assets/generated/release-apex-gif-maker.svg" alt="APEX GIF MAKER 최신 정식 릴리스"></a>

[![저장소](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/APEXGIFMAKER) [![다운로드](assets/ui/btn-download.svg)](https://github.com/deuxdoom/APEXGIFMAKER/releases/latest) [![웹사이트](assets/ui/btn-website.svg)](https://deuxdoom.github.io/APEXGIFMAKER/)

<br clear="right">

<a id="gamepad-tester"></a>

### 05 · GamePadTester

**Windows용 정밀 게임패드 진단 도구**

<a href="https://github.com/deuxdoom/GamePadTester"><img align="right" width="440" src="assets/projects/05-gamepad-tester.png" alt="컨트롤러 도식, 스틱 그래프, 트리거 막대를 보여 주는 GamePadTester 개요 화면"></a>

gamepad-tester.com·Gamepadla와 같은 방식으로 스틱 원형도와 폴링 레이트를 측정해 결과를 직접 비교할 수 있습니다. 버튼·트리거·진동·자이로·터치패드도 확인합니다.

- 강제 데드존 없이 원시 값으로 스틱 원형도(32구간 RMS 오차)·드리프트·해상도·스냅백 측정
- C++ 전용 스레드에서 XInput 패킷·원시 HID 보고서·SDL로 폴링 레이트 측정, JSON / CSV / TXT 내보내기
- 컨트롤러 최대 4개, Xbox·DualSense·Switch Pro / ProCon 2 레이아웃, 적응형 트리거·진동 테스트
- DualSense USB 1000 Hz 폴링 설정, 800×400 결과 카드, SHA-256 검증 업데이트

<b>기술</b>&nbsp; `Python` `PySide6` `C++20` `SDL3` `XInput` `HID`<br>
<b>배포</b>&nbsp; 프리웨어 · Windows 10/11 · 소스 비공개<br>
<b>최신 버전</b>&nbsp; <a href="https://github.com/deuxdoom/GamePadTester/releases/latest"><img align="absmiddle" src="assets/generated/release-gamepad-tester.svg" alt="GamePadTester 최신 정식 릴리스"></a>

[![저장소](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/GamePadTester) [![다운로드](assets/ui/btn-download.svg)](https://github.com/deuxdoom/GamePadTester/releases/latest) [![웹사이트](assets/ui/btn-website.svg)](https://deuxdoom.github.io/GamePadTester/)

<br clear="right">

<a id="picvium"></a>

### 06 · PICVIUM

**RAW 보기와 로컬 업스케일을 지원하는 이미지 뷰어·편집기**

<a href="https://github.com/deuxdoom/PICVIUM"><img align="right" width="440" src="assets/projects/06-picvium.png" alt="사진, 편집 도구 모음, EXIF 정보 사이드바를 보여 주는 PICVIUM 이미지 뷰어"></a>

사진·그래픽·카메라 RAW·문서 이미지를 한 창에서 보고, 로컬 편집·형식 변환·Real-ESRGAN 업스케일을 처리합니다. Windows 배포본에 .NET 런타임을 포함하며 포터블 설정을 지원합니다.

- 폴더 썸네일, 확대·축소·이동, 애니메이션 재생, 여러 페이지 이동, EXIF 사이드바
- 자르기·크기 변경·회전·반전과 실행 취소 / 다시 실행, 7개 이미지 형식 저장·일괄 변환
- Vulkan GPU에서 사진·일러스트 2×·4×·8× 업스케일, 취소와 결과 비교
- 도구 모음·아이콘 테마 사용자 지정, 명령 검색, Windows 파일 연결, 재시작 없이 전환하는 9개 UI 언어

<b>기술</b>&nbsp; `C#` `.NET 10` `Avalonia 12` `Magick.NET` `LibRaw` `PDFium` `Real-ESRGAN / Vulkan`<br>
<b>배포</b>&nbsp; 개인·비상업용 무료 · Windows 10/11 x64 · 소스 비공개<br>
<b>최신 버전</b>&nbsp; <a href="https://github.com/deuxdoom/PICVIUM/releases/latest"><img align="absmiddle" src="assets/generated/release-picvium.svg" alt="PICVIUM 최신 정식 릴리스"></a>

[![저장소](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/PICVIUM) [![다운로드](assets/ui/btn-download.svg)](https://github.com/deuxdoom/PICVIUM/releases/latest) [![웹사이트](assets/ui/btn-website.svg)](https://deuxdoom.github.io/PICVIUM/)

<br clear="right">

<a id="image-upscaler"></a>

### 07 · ImageUpscaler

**포터블·오프라인 AI 이미지 업스케일러**

<a href="https://github.com/deuxdoom/ImageUpscaler"><img align="right" width="440" src="assets/projects/07-image-upscaler.png" alt="이미지 목록, 전후 비교 슬라이더, 확대 설정을 보여 주는 ImageUpscaler"></a>

사진·일러스트·투명 이미지·픽셀 아트를 로컬 PC에서 최대 8×로 확대합니다. 포터블 EXE 하나에 Real-ESRGAN 모델, 코덱, 런타임을 포함합니다.

- 사진 AI(Real-ESRGAN x4plus), 이미지 AI(x4plus-anime), 선형광 Lanczos, 픽셀 아트용 정수배 최근접 보간의 4가지 모드
- PNG·JPG·WebP·AVIF 2×·4×·8× 출력, 알파를 별도로 확대해 투명도 보존
- 일괄 처리 목록, 확대 가능한 전후 비교 슬라이더
- Vulkan 지원 여부 확인과 명시적인 대체 처리, SHA-256 검증 업데이트

<b>기술</b>&nbsp; `C#` `.NET 8` `Windows Forms` `SkiaSharp` `Magick.NET` `Real-ESRGAN (ncnn / Vulkan)`<br>
<b>배포</b>&nbsp; 무료 배포 · Windows 10/11 x64 · 소스 비공개<br>
<b>최신 버전</b>&nbsp; <a href="https://github.com/deuxdoom/ImageUpscaler/releases/latest"><img align="absmiddle" src="assets/generated/release-image-upscaler.svg" alt="ImageUpscaler 최신 정식 릴리스"></a>

[![저장소](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/ImageUpscaler) [![다운로드](assets/ui/btn-download.svg)](https://github.com/deuxdoom/ImageUpscaler/releases/latest) [![웹사이트](assets/ui/btn-website.svg)](https://deuxdoom.github.io/ImageUpscaler/)

<br clear="right">

<a id="ai-agents-usage-monitor"></a>

### 08 · AI Agents Usage Monitor

**Windows 트레이에서 확인하는 Claude·Codex 사용 한도**

<a href="https://github.com/deuxdoom/usage-monitor-for-claude"><img align="right" width="440" src="assets/projects/08-ai-agents-usage-monitor.png" alt="Claude·Codex 상세 팝업과 한 줄 바 모드를 보여 주는 AI Agents Usage Monitor"></a>

Claude와 Codex 사용 한도를 실시간으로 보여 주는 가벼운 트레이 앱입니다. [jens-duttke/usage-monitor-for-claude](https://github.com/jens-duttke/usage-monitor-for-claude)를 확장한 포크로, Codex 지원·한 줄 바 모드·검증형 앱 내 업데이터를 추가했습니다.

- 세션·주간 한도를 표시하는 트레이 아이콘, 초기화 시각·플랜·크레딧·로컬 세션 기록의 모델별 토큰 상세 팝업
- 공식 Codex App Server로 조회한 Codex 한도를 Claude와 함께 표시
- 시계 옆 한 줄 바 모드, 시간 흐름을 반영한 사용량 색상, 임계값 알림
- 포터블 단일 EXE, 13개 언어, 이벤트 명령, 복구 기능을 갖춘 앱 내 업데이트

<b>기술</b>&nbsp; `Python` `pywebview` `pystray` `PyInstaller` `C#`<br>
<b>배포</b>&nbsp; 오픈소스(MIT) · jens-duttke/usage-monitor-for-claude의 포크 · Windows 10/11 x64<br>
<b>최신 버전</b>&nbsp; <a href="https://github.com/deuxdoom/usage-monitor-for-claude/releases/latest"><img align="absmiddle" src="assets/generated/release-ai-agents-usage-monitor.svg" alt="AI Agents Usage Monitor 최신 정식 릴리스"></a>

[![저장소](assets/ui/btn-repository.svg)](https://github.com/deuxdoom/usage-monitor-for-claude) [![다운로드](assets/ui/btn-download.svg)](https://github.com/deuxdoom/usage-monitor-for-claude/releases/latest) [![웹사이트](assets/ui/btn-website.svg)](https://deuxdoom.github.io/usage-monitor-for-claude/)

<br clear="right">

<sub>TVer, CHZZK, NVIDIA ShadowPlay, Flydigi APEX, DualSense, Claude, Codex는 각 소유자의 상표입니다. 여기에 소개한 앱은 독립적으로 제작한 프로젝트이며, 해당 기업과 제휴하거나 공식 승인을 받은 제품이 아닙니다.</sub>

<a id="toolbox"></a>

## 04 · 사용 기술

위 배포본에 실제로 사용하는 기술을 분야별로 정리했습니다. 숫자는 주요 프로젝트 번호입니다.

| 분야 | 기술 |
|:--|:--|
| **언어** | ![Python](https://img.shields.io/badge/Python-172440?style=flat-square&logo=python&logoColor=65D6E6) ![C#](https://img.shields.io/badge/C%23-172440?style=flat-square) ![C++](https://img.shields.io/badge/C%2B%2B-172440?style=flat-square&logo=cplusplus&logoColor=65D6E6) ![JavaScript](https://img.shields.io/badge/JavaScript-172440?style=flat-square&logo=javascript&logoColor=65D6E6)<br><sub>Python 01–05, 08 · C# 06–08 · C++20 측정 코어 05 · 프로젝트 사이트와 08 팝업 UI의 JavaScript / HTML / CSS</sub> |
| **데&#8288;스&#8288;크&#8288;톱<br>런&#8288;타&#8288;임** | ![PySide6](https://img.shields.io/badge/PySide6-172440?style=flat-square&logo=qt&logoColor=65D6E6) ![PyQt6](https://img.shields.io/badge/PyQt6-172440?style=flat-square&logo=qt&logoColor=65D6E6) ![Tkinter](https://img.shields.io/badge/Tkinter-172440?style=flat-square) ![Avalonia](https://img.shields.io/badge/Avalonia-172440?style=flat-square) ![Windows Forms](https://img.shields.io/badge/Windows_Forms-172440?style=flat-square) ![pywebview](https://img.shields.io/badge/pywebview-172440?style=flat-square) ![.NET 8](https://img.shields.io/badge/.NET_8-172440?style=flat-square&logo=dotnet&logoColor=65D6E6) ![.NET 10](https://img.shields.io/badge/.NET_10-172440?style=flat-square&logo=dotnet&logoColor=65D6E6) ![PyInstaller](https://img.shields.io/badge/PyInstaller-172440?style=flat-square)<br><sub>PySide6 02, 04, 05 · PyQt6 01 · Tkinter 03 · Avalonia 12 / .NET 10 06 · Windows Forms / .NET 8 07 · pywebview·pystray 08 · PyInstaller 단일 EXE 03, 08</sub> |
| **미&#8288;디&#8288;어<br>이&#8288;미&#8288;지** | ![FFmpeg](https://img.shields.io/badge/FFmpeg-172440?style=flat-square&logo=ffmpeg&logoColor=65D6E6) ![yt-dlp](https://img.shields.io/badge/yt--dlp-172440?style=flat-square) ![NVIDIA NVENC](https://img.shields.io/badge/NVIDIA_NVENC-172440?style=flat-square&logo=nvidia&logoColor=65D6E6) ![Real-ESRGAN](https://img.shields.io/badge/Real--ESRGAN-172440?style=flat-square) ![Vulkan](https://img.shields.io/badge/Vulkan-172440?style=flat-square&logo=vulkan&logoColor=65D6E6) ![SkiaSharp](https://img.shields.io/badge/SkiaSharp-172440?style=flat-square) ![Magick.NET](https://img.shields.io/badge/Magick.NET-172440?style=flat-square) ![LibRaw](https://img.shields.io/badge/LibRaw-172440?style=flat-square) ![PDFium](https://img.shields.io/badge/PDFium-172440?style=flat-square)<br><sub>FFmpeg 01, 02, 04 · yt-dlp 01, 02 · NVENC 인코딩 01, 02 · Real-ESRGAN / Vulkan·Magick.NET 06, 07 · SkiaSharp·ncnn 07 · LibRaw·PDFium 06</sub> |
| **입&#8288;력<br>하&#8288;드&#8288;웨&#8288;어** | ![SDL3](https://img.shields.io/badge/SDL3-172440?style=flat-square) ![XInput](https://img.shields.io/badge/XInput-172440?style=flat-square) ![Raw HID](https://img.shields.io/badge/Raw_HID-172440?style=flat-square)<br><sub>05의 컨트롤러 입력·폴링 레이트 측정·진동 제어</sub> |
| **배&#8288;포<br>개&#8288;발&nbsp;도&#8288;구** | ![Git](https://img.shields.io/badge/Git-172440?style=flat-square&logo=git&logoColor=65D6E6) ![GitHub Releases](https://img.shields.io/badge/GitHub_Releases-172440?style=flat-square&logo=github&logoColor=65D6E6) ![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-172440?style=flat-square&logo=githubpages&logoColor=65D6E6) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-172440?style=flat-square&logo=githubactions&logoColor=65D6E6) ![VS Code](https://img.shields.io/badge/VS_Code-172440?style=flat-square)<br><sub>모든 앱을 GitHub Releases로 배포하고 GitHub Pages 사이트를 운영합니다. 프로필 데이터는 GitHub Actions로 갱신합니다.</sub> |

<a id="insights"></a>

## 05 · GitHub 활동 통계

<p align="center">
  <img src="assets/generated/insights.svg" width="760" alt="공개 GitHub 데이터 기반 릴리스 통계: 배포 횟수, 배포 파일 다운로드, 첫 배포와 최근 배포, 최근 12개월의 프로젝트별 월간 릴리스">
</p>

<sub>예약 워크플로(<a href=".github/workflows/refresh-data.yml">refresh-data.yml</a>)가 공개 GitHub REST API로 생성합니다. 다운로드 수는 GitHub Release 배포 파일만 집계합니다.</sub>

<a id="releases"></a>

## 06 · 최신 소프트웨어 릴리스

| 프로젝트 | 최신 정식 버전 · 배포일(UTC) |
|:--|:--|
| **01 · [TVer Downloader](https://github.com/deuxdoom/TVerDownloader)** | <a href="https://github.com/deuxdoom/TVerDownloader/releases/latest"><img src="assets/generated/release-tver-downloader.svg" alt="TVer Downloader 최신 릴리스"></a> |
| **02 · [ChzzkDownloader](https://github.com/deuxdoom/ChzzkDownloader)** | <a href="https://github.com/deuxdoom/ChzzkDownloader/releases/latest"><img src="assets/generated/release-chzzk-downloader.svg" alt="ChzzkDownloader 최신 릴리스"></a> |
| **03 · [ShadowPlay Notifier](https://github.com/deuxdoom/Shadowplay-Notifier)** | <a href="https://github.com/deuxdoom/Shadowplay-Notifier/releases/latest"><img src="assets/generated/release-shadowplay-notifier.svg" alt="ShadowPlay Notifier 최신 릴리스"></a> |
| **04 · [APEX GIF MAKER](https://github.com/deuxdoom/APEXGIFMAKER)** | <a href="https://github.com/deuxdoom/APEXGIFMAKER/releases/latest"><img src="assets/generated/release-apex-gif-maker.svg" alt="APEX GIF MAKER 최신 릴리스"></a> |
| **05 · [GamePadTester](https://github.com/deuxdoom/GamePadTester)** | <a href="https://github.com/deuxdoom/GamePadTester/releases/latest"><img src="assets/generated/release-gamepad-tester.svg" alt="GamePadTester 최신 릴리스"></a> |
| **06 · [PICVIUM](https://github.com/deuxdoom/PICVIUM)** | <a href="https://github.com/deuxdoom/PICVIUM/releases/latest"><img src="assets/generated/release-picvium.svg" alt="PICVIUM 최신 릴리스"></a> |
| **07 · [ImageUpscaler](https://github.com/deuxdoom/ImageUpscaler)** | <a href="https://github.com/deuxdoom/ImageUpscaler/releases/latest"><img src="assets/generated/release-image-upscaler.svg" alt="ImageUpscaler 최신 릴리스"></a> |
| **08 · [AI Agents Usage Monitor](https://github.com/deuxdoom/usage-monitor-for-claude)** | <a href="https://github.com/deuxdoom/usage-monitor-for-claude/releases/latest"><img src="assets/generated/release-ai-agents-usage-monitor.svg" alt="AI Agents Usage Monitor 최신 릴리스"></a> |

<sub>각 저장소의 GitHub Releases에서 초안·사전 배포를 제외한 최신 정식 릴리스를 읽습니다. 더 최신인 사전 배포가 있으면 배지에 함께 표시하고, 릴리스가 없으면 “No published release”로 표시합니다. 6시간마다 갱신합니다.</sub>

<a id="engineering"></a>

## 07 · 소프트웨어에 담은 설계

실제 배포한 앱의 구현 사례입니다. 입력을 측정하는 방식, 이미지를 처리하는 위치, 데스크톱 업데이트 실패 시 복구 흐름을 보여 줍니다.

<picture>
  <source media="(max-width: 640px)" srcset="assets/engineering-ko-compact.svg">
  <img src="assets/engineering-ko.svg" width="760" alt="구현 사례: GamePadTester의 C++20 전용 측정 스레드, PICVIUM의 로컬 Vulkan 이미지 처리, ShadowPlay Notifier의 SHA-256 검증과 업데이트 실패 시 복구.">
</picture>

**프로젝트 문서** · [네이티브 컨트롤러 측정](https://github.com/deuxdoom/GamePadTester/blob/main/readme.md) · [로컬 이미지 처리](https://github.com/deuxdoom/PICVIUM/blob/main/README.md) · [업데이트 검증과 복구](https://github.com/deuxdoom/Shadowplay-Notifier/blob/main/README.md)

<picture>
  <source media="(max-width: 640px)" srcset="assets/update-flow-ko-compact.svg">
  <img src="assets/update-flow-ko.svg" width="760" alt="ShadowPlay Notifier 업데이트 흐름: 다운로드, 크기·SHA-256 검증, 교체, 재실행. 설치나 재실행 실패 시 이전 앱을 복구하고 설정과 로그를 유지합니다.">
</picture>

<sub>업데이트 흐름은 ShadowPlay Notifier에 문서화한 동작입니다. 위 카드는 각 프로젝트의 사례를 보여 주며, 자세한 설명은 연결한 README에서 확인할 수 있습니다.</sub>

<a id="connect"></a>

## 08 · 연락과 지원

- **GitHub** · [@deuxdoom](https://github.com/deuxdoom) · [전체 저장소](https://github.com/deuxdoom?tab=repositories)
- **Mastodon** · [@deuxdoom@mastodon.social](https://mastodon.social/@deuxdoom)
- **후원** · [GitHub Sponsors](https://github.com/sponsors/deuxdoom)
- **피드백** · 버그 제보와 기능 제안은 각 프로젝트의 Issues에서 받습니다.

**프로젝트 사이트** · [TVer Downloader](https://deuxdoom.github.io/TVerDownloader/) · [ChzzkDownloader](https://deuxdoom.github.io/ChzzkDownloader/) · [ShadowPlay Notifier](https://deuxdoom.github.io/Shadowplay-Notifier/) · [APEX GIF MAKER](https://deuxdoom.github.io/APEXGIFMAKER/) · [GamePadTester](https://deuxdoom.github.io/GamePadTester/) · [PICVIUM](https://deuxdoom.github.io/PICVIUM/) · [ImageUpscaler](https://deuxdoom.github.io/ImageUpscaler/) · [AI Agents Usage Monitor](https://deuxdoom.github.io/usage-monitor-for-claude/)

<br>

<div align="center">

<img src="assets/footer.svg" width="100%" alt="DEUXDOOM — 실용적인 소프트웨어와 세심한 설계.">

<sub><a href="#top">맨 위로 ↑</a></sub>

</div>
