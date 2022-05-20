import tkinter as tk

# アプリの雛形作成
root = tk.Tk()
root.title('農産物価格更新')
root.geometry('450x650')

# テキストボックスの作成
text_box = tk.Entry(root)
text_box.place(x=50, y=50, width=185, height=40)

text_box2 = tk.Entry(root)
text_box2.place(x=260, y=50, width=140, height=40)

# アプリの実行
root.mainloop()