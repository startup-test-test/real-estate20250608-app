# 不動産投資シミュレーター Streamlit版

## 概要
不動産投資の収益性を分析するWebアプリケーションです。物件情報を入力すると、IRR、CCR、ROIなどの投資指標を自動計算し、AI診断や市場分析も行えます。

## 機能
- 📊 **投資シミュレーション**: IRR、CCR、ROI、DSCRなど主要指標の自動計算
- 📈 **キャッシュフロー分析**: 10年間の収支予測とグラフ表示
- 🏠 **市場分析**: 類似物件との価格比較（国土交通省API使用）
- 🤖 **AI診断**: ChatGPTによる投資判断アドバイス
- 📄 **レポート出力**: 分析結果のダウンロード機能

## セットアップ

### 1. リポジトリのクローン
```bash
git clone [your-repository-url]
cd real-estate-simulator
```

### 2. 仮想環境の作成（推奨）
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 4. 環境変数の設定
`.env.example`をコピーして`.env`を作成し、APIキーを設定します：
```bash
cp .env.example .env
```

`.env`ファイルを編集：
```
OPENAI_API_KEY=your-openai-api-key
REAL_ESTATE_API_KEY=your-real-estate-api-key
```

### 5. アプリケーションの起動
```bash
streamlit run app.py
```

ブラウザで `http://localhost:8501` にアクセスします。

## 使い方

### 1. 物件情報の入力
- **物件基本情報**: 所在地、築年数、面積など
- **取得費用**: 購入価格、諸経費、改装費など
- **収支条件**: 家賃、管理費、空室率など
- **借入条件**: ローン金額、金利、返済年数
- **出口戦略**: 保有年数、売却時の想定価格

### 2. シミュレーション実行
「シミュレーション実行」ボタンをクリックすると：
- 主要投資指標の計算
- 年次キャッシュフロー表の作成
- 投資判断の表示

### 3. 市場分析（オプション）
国土交通省のAPIを使用して類似物件を検索し、価格の妥当性を評価します。

### 4. AI診断（オプション）
ChatGPTを使用して、より詳細な投資アドバイスを生成します。

### 5. レポート出力
分析結果をJSON/CSV形式でダウンロードできます。

## APIキーの取得方法

### OpenAI APIキー
1. [OpenAI Platform](https://platform.openai.com/)にアクセス
2. アカウントを作成/ログイン
3. API keysページでキーを生成

### 不動産取引価格情報APIキー
1. [国土交通省 不動産情報ライブラリAPI](https://www.reinfolib.mlit.go.jp/)にアクセス
2. 利用登録を行い、APIキーを取得

## トラブルシューティング

### エラー: ModuleNotFoundError
```bash
pip install -r requirements.txt
```

### エラー: APIキーが無効
- `.env`ファイルのAPIキーが正しく設定されているか確認
- APIキーの前後に余計なスペースがないか確認

### Streamlitが起動しない
- ポート8501が使用されていないか確認
- ファイアウォールの設定を確認

## 開発者向け情報

### ディレクトリ構造
```
real-estate-simulator/
├── app.py              # メインアプリケーション
├── requirements.txt    # 依存パッケージ
├── .env.example       # 環境変数の例
├── .env              # 環境変数（gitignore）
├── README.md         # このファイル
└── .gitignore       # Git除外設定
```

### カスタマイズ
- `app.py`の各タブセクションを編集して機能を追加/変更
- カスタムCSSは`st.markdown()`内で調整可能

## ライセンス
MIT License

## 貢献
プルリクエストを歓迎します。大きな変更の場合は、まずissueを作成して変更内容を議論してください。