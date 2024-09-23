import tkinter as tk
from tkinter import ttk
from tqdm import tqdm
import time
import threading

def chay_thanh_tien_do():
    for i in tqdm(range(50)):
        time.sleep(0.05) 
        bien_tien_do.set(i + 1)
        thanh_tien_do.update_idletasks()
    tuoi = nhap_tuoi.get()
    nhan_ket_qua.config(text=f"Tuổi của bạn là: {tuoi}")

def bat_dau():
    tuoi = nhap_tuoi.get()
    if tuoi.isdigit():
        tuoi = int(tuoi)
        threading.Thread(target=chay_thanh_tien_do).start()
    else:
        nhan_ket_qua.config(text="Vui lòng nhập một số hợp lệ.")

cua_so = tk.Tk()
cua_so.title("Công cụ tính số tuổi cực chuẩn")

nhan_tuoi = tk.Label(cua_so, text="Nhập số tuổi của bạn:")
nhan_tuoi.pack(pady=10)

nhap_tuoi = tk.Entry(cua_so)
nhap_tuoi.pack(pady=5)

nut_bat_dau = tk.Button(cua_so, text="Bắt đầu", command=bat_dau)
nut_bat_dau.pack(pady=10)

bien_tien_do = tk.IntVar()
thanh_tien_do = ttk.Progressbar(cua_so, maximum=50, variable=bien_tien_do)
thanh_tien_do.pack(pady=10)

nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack(pady=10)

cua_so.mainloop()
