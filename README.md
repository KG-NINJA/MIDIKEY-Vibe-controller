# MIDI IDE Controller

MIDIキーボードを使用して、IDE（Cursor, VS Code 等）のAI提案を瞬時に「承認」または「却下」するためのツールです。指先一つで爆速開発を実現します。

## 🚀 特徴
- **MIDI対応**: 鍵盤を叩くだけでアクションを実行。
- **直感的操作**: 高い音で「承認(Alt+Enter)」、低い音で「却下(Esc)」。
- **カスタマイズ可能**: 音域や鍵盤ごとの設定を簡単に変更可能。

## 🛠 セットアップ

### 1. 依存関係のインストール
Pythonがインストールされている環境で、以下のコマンドを実行してください。
```bash
pip install -r requirements.txt
```

### 2. MIDIデバイスの確認
使用しているMIDIキーボードの名前を確認します。
```bash
python list_midi_devices.py
```

### 3. 設定
`controller.py` の `MIDI_PORT_NAME` を、手順2で確認したデバイス名に書き換えます。

## 🎮 使い方
プログラムを起動し、IDE（Cursorなど）をアクティブにした状態でMIDIキーボードを叩いてください。
```bash
python controller.py
```

- **C4 以上の音**: 承認 (Alt+Enter)
- **C4 未満の音**: 却下 (Esc)

## 📄 ライセンス
MIT License