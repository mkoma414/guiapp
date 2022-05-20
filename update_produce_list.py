import tkinter as tk
import openpyxl

# 更新ボタンがクリックされた時の動作
def update_button_clicked():
  # 更新用データの用意
  name = text_box.get().replace('\x10', '')
  price = int(text_box2.get().replace('\x10', ''))

  update_dict = { name: price }

  # エクセルファイルの更新
  wb = openpyxl.load_workbook('全体売上.xlsx')
  sheet = wb.worksheets[0]

  for row_num in range(2, sheet.max_row):
    produce_name = sheet.cell(row=row_num, column=1).value
    if produce_name in update_dict:
      sheet.cell(row=row_num, column=2).value = update_dict[produce_name]
      fill = openpyxl.styles.PatternFill(patternType='solid',fgColor='FF6E91') 
      sheet.cell(row=row_num, column=2).fill = fill

  wb.save('価格更新.xlsx')

# アプリの雛形作成
root = tk.Tk()
root.title('農産物価格更新')
root.geometry('450x650')

# テキストボックスの作成
text_box = tk.Entry(root)
text_box.place(x=50, y=50, width=185, height=40)

text_box2 = tk.Entry(root)
text_box2.place(x=260, y=50, width=140, height=40)

# 更新ボタンの作成
update_button = tk.Button(root, text='更新', font=("Meiryo",18), command=update_button_clicked)
update_button.place(x=135, y=565, width=180, height=45)

# アプリの実行
root.mainloop()


