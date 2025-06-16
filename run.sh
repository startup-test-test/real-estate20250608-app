#!/bin/bash

# 大家DX - 実行スクリプト

# カラー出力用の設定
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}大家DX - 不動産投資シミュレーター${NC}"
echo "Starting application..."

# backend ディレクトリに移動
cd backend

# 仮想環境が存在するかチェック
if [ -d "venv" ]; then
    echo -e "${YELLOW}仮想環境を有効化しています...${NC}"
    source venv/bin/activate
fi

# .env ファイルの存在チェック
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}警告: .env ファイルが見つかりません${NC}"
    echo "backend/.env.example をコピーして .env を作成してください"
    echo "cp .env.example .env"
fi

# Streamlit アプリケーションを起動
echo -e "${GREEN}アプリケーションを起動しています...${NC}"
streamlit run app.py --server.port 8501