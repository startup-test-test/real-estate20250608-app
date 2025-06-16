# 大家DX - 不動産投資シミュレーター

不動産投資の収益性を分析・シミュレーションするWebアプリケーションです。

## プロジェクト構成

```
project-root/
├── backend/            # Pythonバックエンド（Streamlit）
│   ├── app.py         # メインアプリケーション
│   ├── requirements.txt
│   └── .env.example   # 環境変数のテンプレート
├── saas/              # （将来）React/Viteフロントエンド
├── lp/                # （将来）ランディングページ
├── run.sh             # 実行スクリプト
├── .gitignore
└── README.md
```

## セットアップ

### 1. リポジトリのクローン

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. 環境変数の設定

```bash
cp backend/.env.example backend/.env
# backend/.env を編集して必要な値を設定
```

### 3. 依存関係のインストール

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 実行方法

### 方法1: 実行スクリプトを使用（推奨）

```bash
./run.sh
```

### 方法2: 直接実行

```bash
cd backend && streamlit run app.py
```

### 方法3: ルートから実行

```bash
streamlit run backend/app.py
```

## 機能

- 不動産投資の収益性シミュレーション
- キャッシュフロー分析
- AI診断機能（OpenAI API使用）
- インタラクティブなグラフ表示

## 環境変数

`backend/.env` ファイルに以下の環境変数を設定してください：

- `OPENAI_API_KEY`: OpenAI APIキー（AI診断機能用）
- `APP_ENV`: アプリケーション環境（development/production）
- `DEBUG`: デバッグモード（true/false）

## 開発

### コードスタイル

- Python 3.8以上を使用
- PEP 8に準拠

### テスト

```bash
cd backend
python -m pytest tests/
```

## ライセンス

[ライセンス情報を記載]