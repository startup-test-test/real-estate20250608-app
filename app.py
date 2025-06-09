"""
大家DX - 不動産投資シミュレーターテストです。
6月9日 10:50
"""

import streamlit as st
import pandas as pd
import numpy as np
import numpy_financial as npf
from math import pow
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import json
import os
from typing import Dict, List, Optional, Tuple
import openai
from openai import OpenAI
import requests
import time
import re
import random
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

# ページ設定
st.set_page_config(
    page_title="大家DX - 不動産投資シミュレーター",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# カスタムCSS - モダンなデザイン
st.markdown("""
<style>
    /* メインコンテナ */
    .main {
        padding: 0;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* ヘッダー */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem 3rem;
        border-radius: 0 0 20px 20px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* カード */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        border: 1px solid #f0f0f0;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 20px rgba(0,0,0,0.12);
    }
    
    /* メトリクス */
    div[data-testid="metric-container"] {
        background: white;
        border: 1px solid #e0e0e0;
        padding: 1.2rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    div[data-testid="metric-container"] > div {
        font-size: 0.9rem;
        color: #666;
    }
    
    div[data-testid="metric-container"] > div:nth-child(2) {
        font-size: 1.8rem;
        font-weight: 700;
        color: #333;
    }
    
    /* ボタン */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1rem;
        font-weight: 600;
        border-radius: 10px;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* タブ */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 15px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: white;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        border: 2px solid transparent;
        font-weight: 600;
        color: #666;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* 入力フィールド */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > div {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 0.75rem;
        font-size: 1rem;
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
    }
    
    /* セクションヘッダー */
    .section-header {
        background: #f8f9fa;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        margin: 1.5rem 0 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .section-header h3 {
        margin: 0;
        color: #333;
        font-size: 1.3rem;
    }
    
    /* 結果ボックス */
    .result-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
    
    /* エラー/警告/成功メッセージ */
    .stAlert {
        border-radius: 10px;
        padding: 1rem 1.5rem;
    }
    
    /* プログレスバー */
    .stProgress > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* データフレーム */
    .dataframe {
        font-size: 0.9rem;
    }
    
    /* サイドバーを隠す */
    section[data-testid="stSidebar"] {
        display: none;
    }
    
    /* レスポンシブ */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 1.8rem;
        }
        .main-header {
            padding: 1.5rem 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# セッションステート初期化
if 'simulation_results' not in st.session_state:
    st.session_state.simulation_results = None
if 'market_analysis' not in st.session_state:
    st.session_state.market_analysis = None

# Streamlit Cloudでは.envは不要、Secretsから取得
openai_api_key = st.secrets["OPENAI_API_KEY"]
real_estate_api_key = st.secrets["REAL_ESTATE_API_KEY"]

# ヘッダー
st.markdown("""
<div class="main-header">
    <h1>🏢 大家DX</h1>
    <p>AI搭載 不動産投資シミュレーター - あなたの賃貸経営をスマートに</p>
</div>
""", unsafe_allow_html=True)

# APIキーの状態を確認（デバッグ用）
with st.expander("🔧 API設定状況", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        if openai_api_key and openai_api_key != "your-openai-api-key-here":
            st.success("✅ OpenAI API: 設定済み")
        else:
            st.error("❌ OpenAI API: 未設定")
    with col2:
        if real_estate_api_key and real_estate_api_key != "your-real-estate-api-key-here":
            st.success("✅ 不動産API: 設定済み")
        else:
            st.error("❌ 不動産API: 未設定")

# メインコンテンツ - タブ構成
tab1, tab2, tab3, tab4 = st.tabs([
    "📝 物件情報入力",
    "📊 収益シミュレーション", 
    "🏠 市場分析",
    "🤖 AI投資診断"
])

# Tab1: 物件情報入力
with tab1:
    # 2カラムレイアウト
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-header"><h3>🏠 物件基本情報</h3></div>', unsafe_allow_html=True)
        
        property_name = st.text_input("物件名", placeholder="例：東京都品川区投資物件")
        location = st.text_input("所在地", placeholder="例：東京都品川区東品川4-5-8")
        
        col1_1, col1_2 = st.columns(2)
        with col1_1:
            year_built = st.number_input("建築年", min_value=1900, max_value=2024, value=1987)
        with col1_2:
            property_type = st.selectbox("物件種別", ["戸建", "区分マンション", "一棟アパート", "一棟マンション"])
        
        col1_3, col1_4 = st.columns(2)
        with col1_3:
            land_area = st.number_input("土地面積(㎡)", min_value=0.0, value=135.0, step=0.1)
        with col1_4:
            building_area = st.number_input("建物面積(㎡)", min_value=0.0, value=150.0, step=0.1)
        
        road_price = st.number_input("路線価(円/㎡)", min_value=0, value=250000, step=1000, help="相続税評価の基準となる価格")
        
        st.markdown('<div class="section-header"><h3>💰 取得費用</h3></div>', unsafe_allow_html=True)
        
        purchase_price = st.number_input("購入価格(万円)", min_value=0.0, value=6980.0, step=10.0)
        
        col1_5, col1_6 = st.columns(2)
        with col1_5:
            building_price = st.number_input("建物価格(万円)", min_value=0.0, value=1000.0, step=10.0)
        with col1_6:
            other_costs = st.number_input("諸経費(万円)", min_value=0.0, value=300.0, step=10.0)
        
        renovation_cost = st.number_input("改装費(万円)", min_value=0.0, value=200.0, step=10.0)
    
    with col2:
        st.markdown('<div class="section-header"><h3>📈 収支条件</h3></div>', unsafe_allow_html=True)
        
        monthly_rent = st.number_input("月額賃料(円)", min_value=0, value=250000, step=1000)
        
        col2_1, col2_2 = st.columns(2)
        with col2_1:
            management_fee = st.number_input("管理費(月額円)", min_value=0, value=5000, step=100)
        with col2_2:
            fixed_cost = st.number_input("その他固定費(月額円)", min_value=0, value=0, step=100)
        
        property_tax = st.number_input("固定資産税(円/年)", min_value=0, value=100000, step=1000)
        
        col2_3, col2_4 = st.columns(2)
        with col2_3:
            vacancy_rate = st.number_input("空室率(%)", min_value=0.0, max_value=100.0, value=5.0, step=0.5)
        with col2_4:
            rent_decline = st.number_input("家賃下落率(%/年)", min_value=0.0, value=1.0, step=0.1)
        
        st.markdown('<div class="section-header"><h3>🏦 借入条件</h3></div>', unsafe_allow_html=True)
        
        loan_type = st.selectbox("借入形式", ["元利均等", "元金均等"])
        loan_amount = st.number_input("借入額(万円)", min_value=0.0, value=6500.0, step=10.0)
        
        col2_5, col2_6 = st.columns(2)
        with col2_5:
            interest_rate = st.number_input("金利(%)", min_value=0.0, max_value=10.0, value=0.7, step=0.1)
        with col2_6:
            loan_years = st.number_input("返済年数", min_value=1, max_value=35, value=35, step=1)
        
        st.markdown('<div class="section-header"><h3>🎯 出口戦略</h3></div>', unsafe_allow_html=True)
        
        col2_7, col2_8 = st.columns(2)
        with col2_7:
            holding_years = st.number_input("保有年数(年)", min_value=1, max_value=30, value=10, step=1)
        with col2_8:
            exit_cap_rate = st.number_input("売却CapRate(%)", min_value=0.0, value=6.0, step=0.1)
        
        market_value = st.number_input("想定売却価格(万円)", min_value=0.0, value=8000.0, step=10.0)

# 計算関数
def calculate_remaining_loan(loan_amount, interest_rate, loan_years, elapsed_years, loan_type="元利均等"):
    """ローン残高を計算"""
    r = interest_rate/100/12
    n = loan_years*12
    m = elapsed_years*12
    P = loan_amount*10000
    
    if loan_type == "元利均等":
        if r == 0:
            remaining = P * (n - m) / n
        else:
            remaining = P * (pow(1+r,n) - pow(1+r,m)) / (pow(1+r,n) - 1)
    else:
        monthly_principal = P / n
        remaining = P - (monthly_principal * m)
    
    return remaining / 10000

def calculate_irr(annual_cf, years, sale_profit, self_funding, annual_loan):
    """IRR計算"""
    try:
        annual_cf_after_debt = annual_cf - annual_loan
        cashflows = [-self_funding * 10000]
        
        for i in range(years - 1):
            cashflows.append(annual_cf_after_debt)
        cashflows.append(annual_cf_after_debt + sale_profit * 10000)
        
        irr = npf.irr(cashflows)
        return irr * 100 if irr is not None else None
    except:
        return None

def run_simulation():
    """シミュレーション実行"""
    # キャッシュフロー計算
    annual_rent = monthly_rent * 12 * (1 - vacancy_rate/100)
    monthly_cf = monthly_rent - management_fee - fixed_cost
    annual_cf = monthly_cf * 12
    
    # 自己資金
    self_funding = purchase_price - loan_amount + other_costs + renovation_cost
    
    # ローン返済
    if interest_rate > 0:
        r = interest_rate/100/12
        n = loan_years*12
        monthly_loan = loan_amount*10000 * (r*pow(1+r,n)) / (pow(1+r,n)-1)
    else:
        monthly_loan = loan_amount*10000 / (loan_years*12)
    annual_loan = monthly_loan * 12
    
    # NOI, 評価等
    noi = annual_rent - (management_fee*12 + fixed_cost*12 + property_tax)
    
    # 評価額計算
    if exit_cap_rate > 0:
        cap_rate_eval = noi / (exit_cap_rate/100) / 10000
    else:
        cap_rate_eval = 0
    
    land_eval = land_area * road_price / 10000
    building_eval = building_area * 20
    assessed_total = land_eval + building_eval
    sale_cost = market_value * 0.05
    
    # 売却時のローン残高
    remaining_loan = calculate_remaining_loan(
        loan_amount, interest_rate, loan_years, holding_years, loan_type
    )
    sale_profit = market_value - remaining_loan - sale_cost
    
    # IRR計算
    irr = calculate_irr(annual_cf, holding_years, sale_profit, self_funding, annual_loan)
    
    # 各種比率
    gross_yield = annual_rent / (purchase_price*10000) * 100
    ccr = ((annual_cf - annual_loan) / (self_funding*10000)) * 100 if self_funding > 0 else 0
    roi = (annual_cf / (self_funding*10000)) * 100 if self_funding > 0 else 0
    dscr = noi / annual_loan if annual_loan else 0
    ltv = loan_amount / assessed_total * 100 if assessed_total > 0 else 0
    
    # 結果
    results = {
        "年間家賃収入（円）": int(annual_rent),
        "表面利回り（%）": round(gross_yield, 2),
        "月間キャッシュフロー（円）": int(monthly_cf),
        "年間キャッシュフロー（円）": int(annual_cf),
        "CCR（%）": round(ccr, 2),
        "ROI（%）": round(roi, 2),
        "IRR（%）": round(irr, 2) if irr is not None else "N/A",
        "年間ローン返済額（円）": int(annual_loan),
        "NOI（円）": int(noi),
        "収益還元評価額（万円）": round(cap_rate_eval, 2),
        "実勢価格（万円）": market_value,
        "土地積算評価（万円）": round(land_eval, 2),
        "建物積算評価（万円）": round(building_eval, 2),
        "積算評価合計（万円）": round(assessed_total, 2),
        "売却コスト（万円）": round(sale_cost, 2),
        "残債（万円）": round(remaining_loan, 2),
        "売却益（万円）": round(sale_profit, 2),
        "LTV（%）": round(ltv, 2),
        "DSCR（返済余裕率）": round(dscr, 2),
        "自己資金（万円）": round(self_funding, 2)
    }
    
    # 年次キャッシュフロー表
    years_list = list(range(1, min(holding_years + 1, 11)))
    cum = 0
    cf_data = []
    
    for i in years_list:
        adjusted_monthly_rent = monthly_rent * (1 - (i-1) * rent_decline/100)
        full_annual_rent = adjusted_monthly_rent * 12
        eff = full_annual_rent * (1 - vacancy_rate/100)
        
        annual_expenses = (management_fee + fixed_cost) * 12 + property_tax
        
        repair = 0
        if i % 5 == 0:
            repair = building_area * 10000
        
        cf_i = eff - annual_expenses - annual_loan - repair
        cum += cf_i
        
        cf_data.append({
            "年次": f"{i}年目",
            "満室想定収入": int(full_annual_rent),
            "空室率（%）": vacancy_rate,
            "実効収入": int(eff),
            "経費": int(annual_expenses),
            "大規模修繕": int(repair),
            "ローン返済": int(annual_loan),
            "営業CF": int(cf_i),
            "累計CF": int(cum)
        })
    
    cf_df = pd.DataFrame(cf_data)
    
    return results, cf_df

# Tab2: シミュレーション結果
with tab2:
    if st.button("📊 シミュレーションを実行", type="primary", use_container_width=True):
        with st.spinner("計算中..."):
            results, cf_df = run_simulation()
            st.session_state.simulation_results = {
                'results': results,
                'cf_df': cf_df
            }
    
    if st.session_state.simulation_results:
        results = st.session_state.simulation_results['results']
        cf_df = st.session_state.simulation_results['cf_df']
        
        # 主要指標を大きく表示
        st.markdown('<div class="section-header"><h3>📊 投資パフォーマンス指標</h3></div>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="表面利回り",
                value=f"{results['表面利回り（%）']}%",
                delta="良好" if results['表面利回り（%）'] > 5 else "要検討"
            )
        
        with col2:
            irr_value = results['IRR（%）']
            if irr_value != "N/A":
                st.metric(
                    label="IRR（内部収益率）",
                    value=f"{irr_value}%",
                    delta="優良" if irr_value > 10 else "要検討"
                )
            else:
                st.metric(label="IRR（内部収益率）", value="計算不可")
        
        with col3:
            st.metric(
                label="CCR（自己資金回収率）",
                value=f"{results['CCR（%）']}%",
                delta="良好" if results['CCR（%）'] > 8 else None
            )
        
        with col4:
            st.metric(
                label="DSCR（返済余裕率）",
                value=f"{results['DSCR（返済余裕率）']:.2f}",
                delta="安全" if results['DSCR（返済余裕率）'] > 1.3 else "注意"
            )
        
        # キャッシュフロー情報
        st.markdown('<div class="section-header"><h3>💰 キャッシュフロー分析</h3></div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("月間キャッシュフロー", f"{results['月間キャッシュフロー（円）']:,}円")
            st.metric("年間キャッシュフロー", f"{results['年間キャッシュフロー（円）']:,}円")
            st.metric("NOI（純営業収益）", f"{results['NOI（円）']:,}円")
        
        with col2:
            st.metric("年間家賃収入", f"{results['年間家賃収入（円）']:,}円")
            st.metric("年間ローン返済額", f"{results['年間ローン返済額（円）']:,}円")
            st.metric("自己資金", f"{results['自己資金（万円）']:,.0f}万円")
        
        # グラフ表示
        st.markdown('<div class="section-header"><h3>📈 キャッシュフロー推移</h3></div>', unsafe_allow_html=True)
        
        fig = go.Figure()
        
        # 営業CFの棒グラフ
        fig.add_trace(go.Bar(
            x=cf_df['年次'],
            y=cf_df['営業CF'],
            name='営業CF',
            marker_color='rgba(102, 126, 234, 0.7)',
            text=cf_df['営業CF'].apply(lambda x: f'{x:,.0f}'),
            textposition='outside'
        ))
        
        # 累計CFの折れ線グラフ
        fig.add_trace(go.Scatter(
            x=cf_df['年次'],
            y=cf_df['累計CF'],
            name='累計CF',
            mode='lines+markers',
            line=dict(color='rgba(118, 75, 162, 0.9)', width=3),
            marker=dict(size=8),
            yaxis='y2'
        ))
        
        fig.update_layout(
            title='年次キャッシュフロー推移',
            xaxis_title='年次',
            yaxis=dict(title='営業CF（円）', side='left'),
            yaxis2=dict(title='累計CF（円）', side='right', overlaying='y'),
            hovermode='x unified',
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Arial, sans-serif", size=12)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # 年次キャッシュフロー表
        st.markdown('<div class="section-header"><h3>📋 年次キャッシュフロー詳細</h3></div>', unsafe_allow_html=True)
        st.dataframe(cf_df, use_container_width=True, height=400)
        
        # 投資判断
        st.markdown('<div class="section-header"><h3>🎯 投資判断サマリー</h3></div>', unsafe_allow_html=True)
        
        if results['IRR（%）'] != "N/A":
            if results['IRR（%）'] > 15:
                st.success("✅ **優良案件**: IRRが15%を超えており、非常に魅力的な投資案件です")
            elif results['IRR（%）'] > 10:
                st.info("👍 **良好案件**: IRRが10%を超えており、良好な投資案件です")
            elif results['IRR（%）'] > 5:
                st.warning("⚠️ **要検討**: IRRは平均的です。条件交渉の余地があります")
            else:
                st.error("❌ **再検討推奨**: IRRが低く、投資条件の見直しが必要です")

# Tab3: 市場分析
with tab3:
    st.markdown('<div class="section-header"><h3>🏠 類似物件の市場分析</h3></div>', unsafe_allow_html=True)
    
    if st.button("🔍 市場分析を実行", type="primary", use_container_width=True):
        with st.spinner("類似物件を検索中..."):
            # ユーザー物件の平米単価を計算
            user_unit_price = purchase_price * 10000 / land_area / 10000 if land_area > 0 else 0
            
            # 実際のAPIを使用するかチェック
            if real_estate_api_key and real_estate_api_key != "your-real-estate-api-key-here":
                try:
                    # APIエンドポイント
                    API_URL = "https://www.reinfolib.mlit.go.jp/ex-api/external/XIT001"
                    headers = {"Ocp-Apim-Subscription-Key": real_estate_api_key}
                    
                    # 都道府県コードの完全版
                    prefecture_codes = {
                        "北海道": "01", "青森県": "02", "岩手県": "03", "宮城県": "04", "秋田県": "05",
                        "山形県": "06", "福島県": "07", "茨城県": "08", "栃木県": "09", "群馬県": "10",
                        "埼玉県": "11", "千葉県": "12", "東京都": "13", "神奈川県": "14", "新潟県": "15",
                        "富山県": "16", "石川県": "17", "福井県": "18", "山梨県": "19", "長野県": "20",
                        "岐阜県": "21", "静岡県": "22", "愛知県": "23", "三重県": "24", "滋賀県": "25",
                        "京都府": "26", "大阪府": "27", "兵庫県": "28", "奈良県": "29", "和歌山県": "30",
                        "鳥取県": "31", "島根県": "32", "岡山県": "33", "広島県": "34", "山口県": "35",
                        "徳島県": "36", "香川県": "37", "愛媛県": "38", "高知県": "39", "福岡県": "40",
                        "佐賀県": "41", "長崎県": "42", "熊本県": "43", "大分県": "44", "宮崎県": "45",
                        "鹿児島県": "46", "沖縄県": "47"
                    }
                    
                    # 所在地から都道府県を抽出
                    prefecture = None
                    prefecture_name = None
                    for pref, code in prefecture_codes.items():
                        if pref in location:
                            prefecture = code
                            prefecture_name = pref
                            st.info(f"📍 {pref}の取引データを検索します")
                            break
                    
                    if prefecture:
                        # 最新の取引データを取得
                        current_year = datetime.now().year
                        current_quarter = (datetime.now().month - 1) // 3 + 1
                        
                        # 最新の四半期から順に試す
                        transactions = []
                        for year in range(current_year, current_year - 2, -1):
                            for quarter in range(current_quarter, 0, -1):
                                if year == current_year and quarter > current_quarter:
                                    continue
                                
                                params = {
                                    "year": str(year),
                                    "quarter": str(quarter),
                                    "area": prefecture
                                }
                                
                                st.caption(f"🔍 {year}年第{quarter}四半期のデータを取得中...")
                                
                                try:
                                    response = requests.get(API_URL, params=params, headers=headers, timeout=30)
                                    
                                    if response.status_code == 200:
                                        data = response.json()
                                        trans_data = data.get("data", [])
                                        if trans_data:
                                            transactions.extend(trans_data)
                                            st.caption(f"✅ {len(trans_data)}件のデータを取得")
                                            if len(transactions) >= 20:
                                                break
                                    else:
                                        st.caption(f"⚠️ HTTPエラー: {response.status_code}")
                                except Exception as e:
                                    st.caption(f"⚠️ 取得エラー: {str(e)}")
                                
                                time.sleep(0.5)  # API制限対策
                            
                            if len(transactions) >= 20:
                                break
                        
                        if transactions:
                            # 類似物件をフィルタリング
                            similar_properties = []
                            
                            # ユーザー物件の築年数を計算
                            user_building_age = datetime.now().year - year_built
                            
                            st.caption(f"🔍 類似条件: 面積 {land_area}㎡ (±30%), 築年数 {user_building_age}年 (±10年)")
                            
                            for trans in transactions:
                                if trans.get("Type") == "宅地(土地と建物)":
                                    try:
                                        # 面積の取得と比較
                                        area_str = str(trans.get("Area", "0")).replace(",", "")
                                        area = float(area_str)
                                        area_diff = abs(area - land_area) / land_area if land_area > 0 else 1
                                        
                                        # 面積が±30%以内かチェック
                                        if area_diff > 0.3:
                                            continue
                                        
                                        # 築年数の処理
                                        building_year_str = trans.get("BuildingYear", "")
                                        building_year = None
                                        building_age = None
                                        
                                        if building_year_str and building_year_str != "":
                                            # 和暦から西暦に変換
                                            if "令和" in building_year_str:
                                                year_num = int(re.search(r'\d+', building_year_str).group())
                                                building_year = 2018 + year_num
                                            elif "平成" in building_year_str:
                                                year_num = int(re.search(r'\d+', building_year_str).group())
                                                building_year = 1988 + year_num
                                            elif "昭和" in building_year_str:
                                                year_num = int(re.search(r'\d+', building_year_str).group())
                                                building_year = 1925 + year_num
                                            else:
                                                building_year = int(re.search(r'\d+', building_year_str).group())
                                            
                                            building_age = datetime.now().year - building_year
                                            
                                            # 築年数が±10年以内かチェック
                                            if abs(building_age - user_building_age) > 10:
                                                continue
                                        
                                        # 価格の処理
                                        price_str = str(trans.get("TradePrice", "0"))
                                        price = float(price_str.replace(",", ""))
                                        unit_price = price / area / 10000 if area > 0 else 0
                                        
                                        # 類似物件として追加
                                        similar_properties.append({
                                            '取引時期': f"{trans.get('Year', '')}年Q{trans.get('Quarter', '')}",
                                            '所在地': f"{trans.get('Prefecture', '')}{trans.get('Municipality', '')}{trans.get('DistrictName', '')}",
                                            '面積(㎡)': round(area, 1),
                                            '面積差': f"{area_diff*100:.1f}%",
                                            '築年': building_year if building_year else 'N/A',
                                            '築年数': f"{building_age}年" if building_age else 'N/A',
                                            '構造': trans.get('Structure', ''),
                                            '取引価格(万円)': round(price / 10000),
                                            '平米単価(万円/㎡)': round(unit_price, 2),
                                            '最寄駅': trans.get('NearestStation', ''),
                                            '駅距離': trans.get('TimeToNearestStation', '')
                                        })
                                        
                                    except Exception as e:
                                        continue
                            
                            if similar_properties:
                                # 面積の近い順にソート
                                similar_properties.sort(key=lambda x: float(x['面積差'].replace('%', '')))
                                similar_df = pd.DataFrame(similar_properties[:20])  # 上位20件
                                st.success(f"✅ 実際のAPIから{len(similar_properties)}件の類似物件を発見しました")
                                
                                # 類似度の統計を表示
                                st.caption(f"📊 類似物件の内訳:")
                                st.caption(f"  - 総取引数: {len(transactions)}件")
                                st.caption(f"  - 土地建物: {sum(1 for t in transactions if t.get('Type') == '宅地(土地と建物)')}件")
                                st.caption(f"  - 類似物件: {len(similar_properties)}件")
                            else:
                                raise Exception("類似物件が見つかりませんでした")
                        else:
                            raise Exception("取引データが見つかりませんでした")
                    else:
                        raise Exception("都道府県を特定できませんでした")
                        
                except Exception as e:
                    st.warning(f"APIエラー: {str(e)}")
                    st.info("サンプルデータを表示します")
                    # サンプルデータにフォールバック
                    similar_properties = []
                    for i in range(15):
                        unit_price = user_unit_price * (1 + random.uniform(-0.3, 0.3))
                        area = land_area * (1 + random.uniform(-0.3, 0.3))
                        
                        similar_properties.append({
                            '取引時期': f"2024年Q{random.randint(1, 4)}",
                            '所在地': f"{location[:6] if location else '東京都'}***",
                            '面積(㎡)': round(area, 1),
                            '築年': year_built + random.randint(-10, 10),
                            '構造': random.choice(['木造', '鉄骨造', 'RC']),
                            '取引価格(万円)': round(area * unit_price),
                            '平米単価(万円/㎡)': round(unit_price, 2),
                            '最寄駅': '品川',
                            '駅距離': f"{random.randint(5, 15)}分"
                        })
                    similar_df = pd.DataFrame(similar_properties)
            else:
                # APIキーがない場合はサンプルデータ
                st.info("🔔 実際のデータを取得するには、不動産取引価格情報APIキーを設定してください")
                similar_properties = []
                for i in range(15):
                    unit_price = user_unit_price * (1 + random.uniform(-0.3, 0.3))
                    area = land_area * (1 + random.uniform(-0.3, 0.3))
                    
                    similar_properties.append({
                        '取引時期': f"2024年Q{random.randint(1, 4)}",
                        '所在地': f"{location[:6] if location else '東京都'}***",
                        '面積(㎡)': round(area, 1),
                        '築年': year_built + random.randint(-10, 10),
                        '構造': random.choice(['木造', '鉄骨造', 'RC']),
                        '取引価格(万円)': round(area * unit_price),
                        '平米単価(万円/㎡)': round(unit_price, 2),
                        '最寄駅': '品川',
                        '駅距離': f"{random.randint(5, 15)}分"
                    })
                similar_df = pd.DataFrame(similar_properties)
            
            # 統計を計算
            median_price = similar_df['平米単価(万円/㎡)'].median()
            mean_price = similar_df['平米単価(万円/㎡)'].mean()
            std_price = similar_df['平米単価(万円/㎡)'].std()
            
            # 価格評価
            deviation = ((user_unit_price - median_price) / median_price * 100) if median_price > 0 else 0
            
            if deviation < -20:
                evaluation = "非常に割安"
                color = "green"
            elif deviation < -10:
                evaluation = "割安"
                color = "blue"
            elif deviation < 5:
                evaluation = "適正価格"
                color = "gray"
            elif deviation < 15:
                evaluation = "やや割高"
                color = "orange"
            else:
                evaluation = "割高"
                color = "red"
            
            # 結果を保存
            st.session_state.market_analysis = {
                'similar_df': similar_df,
                'median_price': median_price,
                'mean_price': mean_price,
                'std_price': std_price,
                'user_price': user_unit_price,
                'deviation': deviation,
                'evaluation': evaluation,
                'color': color
            }
    
    if st.session_state.market_analysis:
        analysis = st.session_state.market_analysis
        
        # 価格評価メトリクス
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="市場中央値",
                value=f"{analysis['median_price']:.2f}万円/㎡"
            )
        
        with col2:
            st.metric(
                label="あなたの物件",
                value=f"{analysis['user_price']:.2f}万円/㎡",
                delta=f"{analysis['deviation']:.1f}%"
            )
        
        with col3:
            if analysis['color'] == 'green':
                st.success(f"📊 価格評価: **{analysis['evaluation']}**")
            elif analysis['color'] == 'blue':
                st.info(f"📊 価格評価: **{analysis['evaluation']}**")
            elif analysis['color'] == 'orange':
                st.warning(f"📊 価格評価: **{analysis['evaluation']}**")
            elif analysis['color'] == 'red':
                st.error(f"📊 価格評価: **{analysis['evaluation']}**")
            else:
                st.info(f"📊 価格評価: **{analysis['evaluation']}**")
        
        # 価格分布グラフ
        st.markdown('<div class="section-header"><h3>📊 価格分布分析</h3></div>', unsafe_allow_html=True)
        
        fig = go.Figure()
        
        # ヒストグラム
        fig.add_trace(go.Histogram(
            x=analysis['similar_df']['平米単価(万円/㎡)'],
            name='類似物件',
            nbinsx=20,
            marker_color='rgba(102, 126, 234, 0.6)'
        ))
        
        # ユーザー物件の位置
        fig.add_vline(
            x=analysis['user_price'],
            line_dash="dash",
            line_color="red",
            annotation_text=f"あなたの物件<br>{analysis['user_price']:.1f}万円/㎡"
        )
        
        # 中央値
        fig.add_vline(
            x=analysis['median_price'],
            line_dash="dash",
            line_color="green",
            annotation_text=f"中央値<br>{analysis['median_price']:.1f}万円/㎡"
        )
        
        fig.update_layout(
            title="平米単価の分布",
            xaxis_title="平米単価（万円/㎡）",
            yaxis_title="件数",
            showlegend=True,
            height=400,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # 類似物件一覧
        st.markdown('<div class="section-header"><h3>📋 類似物件一覧</h3></div>', unsafe_allow_html=True)
        st.dataframe(analysis['similar_df'], use_container_width=True, height=400)

# Tab4: AI診断
with tab4:
    st.markdown('<div class="section-header"><h3>🤖 AI投資診断</h3></div>', unsafe_allow_html=True)
    
    if st.button("🤖 AI診断を実行", type="primary", use_container_width=True):
        with st.spinner("AI分析中..."):
            if st.session_state.simulation_results:
                # サンプル診断を表示
                st.session_state.ai_diagnosis = """
                ## 🎯 投資判断: ★★★☆☆（3/5）

                ### 💪 強み
                1. **立地条件**: 都心へのアクセスが良好で、賃貸需要が安定
                2. **利回り水準**: 表面利回りは都心部としては標準的
                3. **将来性**: エリアの再開発により、長期的な資産価値向上が期待可能

                ### ⚠️ リスク
                1. **築年数**: 築年数が経過しており、大規模修繕のリスクあり
                2. **空室リスク**: 競合物件が多いエリアのため、差別化が必要
                3. **金利上昇**: 将来的な金利上昇により収益性が低下する可能性

                ### 🔧 改善提案
                1. **リノベーション**: 適切な投資で家賃を5-10%向上可能
                2. **管理効率化**: 管理費の見直しで月額コストを削減可能
                3. **付加価値サービス**: IoT設備導入で差別化を図る

                ### 📝 総合アドバイス
                この物件は立地条件に優れていますが、築年数を考慮すると慎重な判断が必要です。
                購入を進める場合は、建物調査を実施し、長期的な修繕計画を明確にすることを推奨します。
                適切なリノベーションと管理により、安定した収益が期待できる物件と判断します。
                """
            else:
                st.warning("先にシミュレーションを実行してください")
    
    # AI診断結果の表示
    if 'ai_diagnosis' in st.session_state and st.session_state.ai_diagnosis:
        st.markdown(st.session_state.ai_diagnosis)

# フッター
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 2rem 0;'>
        <p style='font-size: 1.2rem; font-weight: 600; margin-bottom: 0.5rem;'>🏢 大家DX</p>
        <p style='font-size: 0.9rem;'>AI搭載 不動産投資シミュレーター</p>
        <p style='font-size: 0.8rem; margin-top: 1rem;'>© 2024 Oya DX. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)