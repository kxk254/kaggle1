import pandas as pd
from io import BytesIO

# 各セクションのデータをExcelのシートごとに用意
sheets = {}

# 基本情報
basic_info = pd.DataFrame({
    '項目': ['工事名', '管理ビル名', '工事場所', '実施日', '作業時間', '作業責任者', '連絡先', '作業人数'],
    '内容': ['〇〇ビル空調設備更新工事（例）', '〇〇オフィスビル', '東京都〇〇区〇〇町〇-〇-〇', 
            '令和〇年〇月〇日（〇）', '〇〇：〇〇 ～ 〇〇：〇〇', '氏名（所属会社名）', 
            '〇〇-〇〇〇〇-〇〇〇〇', '〇名（内訳：電気2名、設備1名など）']
})
sheets['基本情報'] = basic_info

# 工事内容
work_content = pd.DataFrame({
    '工事内容': ['〇〇階 空調機交換作業', '〇〇階 配管改修工事', '共用部照明LED化作業']
})
sheets['工事内容'] = work_content

# 使用機器・資材
equipment = pd.DataFrame({
    '品名': ['室内機', '配管材', '電動工具'],
    '数量': ['2台', '20m', '一式'],
    '備考（寸法・重量など）': ['約40kg／台', '銅管', 'インパクトドライバー他']
})
sheets['使用機器・資材'] = equipment

# 安全対策
safety_measures = pd.DataFrame({
    '安全対策・注意事項': [
        '作業エリアの養生（養生マット、ブルーシート等）',
        '共用部の通行制限なし（必要な場合は警備員配置）',
        '火気使用なし（使用時は事前申請）',
        '騒音作業は〇時～〇時の間に限定',
        '作業後は清掃・原状回復を徹底'
    ]
})
sheets['安全対策'] = safety_measures

# 連絡状況
contact_status = pd.DataFrame({
    '部署／テナント名': ['管理事務所', '警備室', '〇〇テナント様'],
    '連絡日': ['〇月〇日'] * 3,
    '担当者': ['氏名'] * 3,
    '備考': ['作業許可取得済み', '当日立会予定', '騒音説明済み']
})
sheets['連絡状況'] = contact_status

# 承認欄
approval = pd.DataFrame({
    '役職': ['作業責任者', '管理会社担当者', 'ビル管理責任者'],
    '氏名': ['○○', '○○', '○○'],
    '署名／押印': ['', '', ''],
    '日付': ['', '', '']
})
sheets['承認欄'] = approval

# Excelファイルとして保存
with pd.ExcelWriter('工事作業書_テンプレート.xlsx', engine='xlsxwriter') as writer:
    for sheet_name, df in sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Excelファイル '工事作業書_テンプレート.xlsx' を作成しました。")