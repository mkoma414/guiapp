import tkinter as tk

# 更新ボタンがクリックされた時の動作
def update_button_clicked():
  produce_name = text_box.get().replace('\x10', '')
  price = text_box2.get().replace('\x10', '')

  print('農産物名：' + produce_name)
  print('価格：' + price)

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


