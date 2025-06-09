"""
指定されたフォルダ内のPDFファイルを結合するためのスクリプト

主な機能:
- フォルダ内のPDFファイルを名前順に表示
- デフォルトの順序（名前順）で結合するか、カスタム順序を指定可能
- 出力ファイル名を指定可能

使用方法:
1. フォルダパスを指定（デフォルト: "../過去問/前期中間/"）
2. 結合順序を確認またはカスタマイズ
3. 出力ファイル名を指定

注意事項:
- 入力ファイルは必ずPDF形式である必要があります
- 出力ファイル名は自動的に.pdf拡張子が付加されます
- 実行前に以下のコマンドでPyPDF2をインストールしてください:
    pip install PyPDF2
"""


import os
from PyPDF2 import PdfMerger

def list_pdf_files(folder_path):
    return sorted([f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')])

def confirm_order(pdf_files):
    print("\n=== PDFファイル一覧（名前順） ===")
    for i, pdf in enumerate(pdf_files):
        print(f"{i + 1}: {pdf}")
    print("\nこの順番で結合してよろしいですか？ (yes/no)")
    return input(">> ").strip().lower() == "yes"

def get_custom_order(pdf_files):
    print("\n結合したい順番の番号をスペース区切りで入力してください。")
    print("例: 3 1 2")
    print(">> ", end="")
    indices = list(map(int, input().strip().split()))
    return [pdf_files[i - 1] for i in indices]

def get_output_filename():
    print("\n出力ファイル名を入力してください（例: result.pdf）")
    print(">> ", end="")
    filename = input().strip()
    if not filename.lower().endswith(".pdf"):
        filename += ".pdf"
    return filename

def merge_pdfs(pdf_files, folder_path, output_filename):
    merger = PdfMerger()
    for pdf in pdf_files:
        pdf_path = os.path.join(folder_path, pdf)
        merger.append(pdf_path)
    output_path = os.path.join(folder_path, output_filename)
    merger.write(output_path)
    merger.close()
    print(f"\n✅ 結合完了: {output_path}")

def main():
    folder_path = "../過去問/前期中間/"  # 適宜フォルダ変更
    pdf_files = list_pdf_files(folder_path)

    if not pdf_files:
        print("PDFファイルが見つかりません。")
        return

    if not confirm_order(pdf_files):
        pdf_files = get_custom_order(pdf_files)

    output_filename = get_output_filename()
    merge_pdfs(pdf_files, folder_path, output_filename)

if __name__ == "__main__":
    main()
