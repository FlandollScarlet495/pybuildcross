# pybuildcross 🚀

**pybuildcross** は、Python スクリプト (`.py`) や Web アプリ (`.html`) を、Go 言語製の軽量バックエンドエンジンを通じて各 OS 向け（Windows / macOS / Linux）の単体実行ファイルへクロスコンパイルするための Python ライブラリです。

---

## 📦 特徴

* ⚡ **簡単な API**: Python から `pbc()` 関数を呼ぶだけでクロスコンパイルが可能
* 🌍 **マルチプラットフォーム対応**: Windows (x86/x64/ARM64)、macOS (x64/ARM64)、Linux (x86/x64/ARM) へのビルドに対応
* 🐍 **Python / HTML 両対応**: Python の標準環境・埋め込み実行モードに加え、HTML 形式のスタンドアロン起動にも対応

---

## 🔧 使い方

```python
from pybuildcross import pybuildcross as pbc

...
```

### 基本的なビルド方法

```python
from pybuildcross import pybuildcross as pbc

# Windows (64bit) 向けにコンパイル
pbc("app.py", target="win-amd64")

# macOS (Apple Silicon / ARM64) 向けにコンパイル
pbc("app.py", target="mac-arm64")

# Linux 向けにコンパイル
pbc("index.html", target="linux/amd64")

```

---

## 🛠️ オプション指定

`pbc()` 関数には以下のパラメータを指定できます：

* `input_file`: 対象ファイル（`.py` または `.html`）
* `target`: ターゲットプラットフォーム (`win-amd64`, `mac-arm64`, `linux/amd64` など)
* `python_mode`: Python の実行モード (`system` または `embed`)
* `output`: 生成される実行ファイルの出力パス指定

---

## 📜 ライセンス

MIT License

```LICENSE
MIT License

Copyright (c) 2026 Kirishima Aoi

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
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR A PARTICULAR PURPOSE AND LIABLE FOR
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
USE OR OTHER DEALINGS IN THE SOFTWARE.

```

---
