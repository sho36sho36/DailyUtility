# 🧰 Daily Utility

日常で使える便利な機能を、ひとつのアプリにまとめることを目指したPython製GUIアプリです。

Plugin方式を採用しており、必要な機能を後から追加できる設計になっています。

## ✨ Features

* 🖥️ GUIアプリ
* 🧩 Plugin方式による機能拡張
* 🔌 Pluginの自動検出
* 🐍 Python製
* 🪟 Windows向け `.exe` に対応
* 🚀 今後さまざまな日常便利機能を追加予定

## 📦 Project Structure

```text
DailyUtility/
├─ main.py
├─ config.py
├─ plugin_manager.py
├─ build.cmd
├─ requirements.txt
├─ gui/
│  ├─ __init__.py
│  └─ main_window.py
├─ plugins/
│  ├─ __init__.py
│  └─ example_plugin.py
└─ utils/
   ├─ __init__.py
   └─ paths.py
```

## 🚀 Run

Python 3.14以降を使用して起動できます。

```powershell
py -3.14 main.py
```

## 🔨 Build

Windows向けの `.exe` を作成する場合：

```powershell
.\build.cmd
```

ビルド後、以下に実行ファイルが生成されます。

```text
dist/DailyUtility.exe
```

## 🧩 Plugin

Daily Utilityでは、Pluginを追加することで機能を拡張できます。

Pluginは `plugins/` フォルダに配置します。

```text
plugins/
├─ example_plugin.py
├─ calculator.py
├─ timer.py
└─ ...
```

## 📌 Version

### v1.0.0

初回リリース。

* GUIの土台を作成
* Pluginシステムを実装
* Plugin自動検出を実装
* Windows `.exe` 化に対応

## 📄 License

Licenseは今後設定予定です。
