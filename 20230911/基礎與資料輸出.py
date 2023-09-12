#python運算的結果請參考ipynb檔

#各種不同的資料類型
str('字串')#文字字串
int(20)#整數數值
float(20.1)#浮點數值
bool(False)#布林函數
    #註：結果只會出現最後一個值，是因為若未加入print指令，預設為以display指令，且只會顯示最後一個值

#如何查詢目前資料的型態->print(type(20.1))
print(type('天邊一片雲'))
print(type(20))
print(type(20.1))
print(type(False))

#如何讓python進行運算
#整數運算->print(二元運算式)
print(5+8)
print(90-10)
print(4*7)
print(6/2)
print(7//2)
print(7%3)
print(999**20)

#浮點數與整數運算
print(5.0+8)
print(5.0+8+10)
print(5.0+8*2)
print(2*(1+2)**2-2**2*2)

#字串的加法運算->print('文字' + '文字')
print("abc" + "efg")
print('我是' + '學習者')

#字串+數值 -> 出錯
print("abc" + 13)
#出現錯誤的結果為TypeError: can only concatenate str (not "int") to str
#該錯誤訊息為：僅能字串+字串

#str() -> 轉為字串
print("abc" + str(13))
#出現的結果為'abc13'，因為13被定義成了“文字”

#int() -> 轉為整數
print(int("13") + int("25"))
    #如果出現非整數的狀況
print(int("13.1") + int("25.4"))
    #因為int指令內並非整數，所以出現數值錯誤訊息

#float() -> 轉為浮點數
print(float("13.5") + float("21.7"))
#整數數值與浮點數值運算
print(20+13.1)
    #為什麼整數數值可以與浮點數值進行運算？
    #因為整數數值被先轉為浮點數值，之後才可以進行相同資料類型的運算

#變數宣告
    #變數名稱 = 變數內容
    #與其他程式語言不同的是，在python，變數直接宣告即可
    #範例：
kimi = 1
tina = 6
print(kimi+tina)
    #變數宣告也可以寫在同一行
kimi,tina=1,6
print(kimi+tina)
#如果不使用變數可以選擇以 del 語法將變數刪除以節省記憶體。
#例如刪除 kimi 變數，那操作方式為:
del kimi #這邊不太懂怎麼運用

#變數命名的規則
#開頭第一個字不能是數字。
#可使用大小寫字母或「_」。
#不可與內建保留字 (右邊表格所列) 同名。
#Python 3 可以使用中文名稱。
#大小寫視為不同的變數。
#不可以出現特殊字元或空白。

#question: 請問以下哪一個變數命名是錯的?
#(1) 5well.->錯誤，變數命名首字不可為數字
#(2) pcschool ->正確，因為變數可使用大小寫
#(3) 巨匠 ->正確，因為python3支援中文

#question: 請問以下哪一個變數命名是錯的?(複選題)
#(1) 7eleven ->錯誤，變數首字不可為數字
#(2) pcschool&python ->錯誤，因為變數不可出現特殊字元
#(3) Pcschool python ->錯誤，因為變數不可出現空白
#(4) if ->錯誤，因為變數不可與內建保留字同名

#question: 若要建立 x 變數內容為 15，請問哪一行是對的? (選擇題)
#(1) x equals 15 ->錯誤，因為變數不可以有空白及保留字(我猜的)
#(2) x is 15 ->錯誤，因為變數不可以有空白(我猜的)
#(3) 15 = x  ->錯誤，先變數名稱再等於數字（我猜的）
#(4) x = 15 ->正確
