import os
import platform
import subprocess
import sys


def pybuildcross(input_file, target=None, python_mode="system", output=None):
    """Python / HTMLスクリプトをGo製ビルダー経由でクロスコンパイルする関数

    :param input_file: ビルドする対象のファイルパス (.py または .html)
    :param target: ターゲットプラットフォーム (例: 'win-amd64', 'linux/amd64', 'mac-arm64')
                    省略した場合は現在のマシンのOS/アーキテクチャになります。
    :param python_mode: Pythonの実行モード ('system'/'py' または 'embed'/'no')
    :param output: 出力ファイルのパス (省略した場合は dist/ 内に自動生成されます)
    """
    # 1. 現在のOSとアーキテクチャからデフォルトのターゲットを決定
    current_os = platform.system().lower()
    if current_os == "darwin":
        default_os = "mac"
    elif current_os == "windows":
        default_os = "windows"
    else:
        default_os = "linux"

    current_arch = platform.machine().lower()
    if current_arch in ["x86_64", "amd64"]:
        default_arch = "amd64"
    elif current_arch in ["arm64", "aarch64"]:
        default_arch = "arm64"
    else:
        default_arch = "386"

    if target is None:
        target = f"{default_os}/{default_arch}"

    # 2. ターゲット文字列の解析とビルダーバイナリの選択
    target_lower = target.lower()
    if "/" in target_lower:
        os_part, arch_part = target_lower.split("/", 1)
    elif "-" in target_lower:
        os_part, arch_part = target_lower.split("-", 1)
    else:
        raise ValueError(
            f"無効なターゲット形式です: '{target}'. 'os/arch' または 'os-arch'"
            " で指定してください。"
        )

        # OS名の正規化
    if os_part in ["win", "windows"]:
        os_dir = "windows"
        os_name = "windows"
    elif os_part in ["mac", "darwin"]:
        os_dir = "mac"
        os_name = "darwin"
    elif os_part in ["lin", "linux"]:
        os_dir = "linux"
        os_name = "linux"
    else:
        raise ValueError(f"サポートされていないOSです: {os_part}")

    # アーキテクチャ名の正規化とバイナリ名の決定
    if arch_part in ["32", "386", "amd32"]:
        arch_name = "386"
        if os_name == "windows":
            builder_exe_name = "python_builder_win_amd32.exe"
        elif os_name == "linux":
            builder_exe_name = "python_builder_linux_amd32"
        else:
            raise ValueError("Macには386(32bit)版はありません。")
    elif arch_part in ["64", "amd64"]:
        arch_name = "amd64"
        if os_name == "windows":
            builder_exe_name = "python_builder_win_amd64.exe"
        elif os_name == "mac" or os_name == "darwin":
            builder_exe_name = "python_builder_mac_amd64"
        elif os_name == "linux":
            builder_exe_name = "python_builder_linux_amd64"
    elif arch_part in ["arm64", "aarch64"]:
        arch_name = "arm64"
        if os_name == "windows":
            builder_exe_name = "python_builder_win_arm64.exe"
        elif os_name == "mac" or os_name == "darwin":
            builder_exe_name = "python_builder_mac_arm64"
        elif os_name == "linux":
            builder_exe_name = "python_builder_linux_arm64"
    elif arch_part in ["arm", "arm32"]:
        arch_name = "arm"
        if os_name == "linux":
            builder_exe_name = "python_builder_linux_arm32"
        else:
            raise ValueError(
            f"{os_name}向けのARM32ビルドはサポートされていません。"
            )
    else:
        raise ValueError(f"サポートされていないアーキテクチャです: {arch_part}")

    # ビルダールートバイナリのパス
    base_dir = os.path.dirname(os.abspath(__file__))
    builder_path = os.path.join(base_dir, "python_builder", os_dir, builder_exe_name)
    if not os.path.exists(builder_path):
        raise FileNotFoundError(
            f"ビルダーのバイナリが見つかりません: {builder_path}\n先に"
            " `build.bat` または `build.sh` を実行してビルダーをコンパイルしてください。"
        )

    # 3. 引数の組み立て
    cmd = [builder_path, "-i", input_file, "-t", f"{os_name}/{arch_name}"]

    if output:
        cmd.extend(["-o", output])

    if python_mode:
        cmd.extend(["-p", python_mode])

    # 4. バックエンドのGoビルダーを実行
    print(f"🚀 [Pythonライブラリ] ビルド実行中: {input_file} -> ターゲット: {target}")
    result = subprocess.run(cmd)

    if result.returncode != 0:
        raise RuntimeError("ビルドに失敗しました。")
    print("✨ ビルドが正常に完了しました！")
