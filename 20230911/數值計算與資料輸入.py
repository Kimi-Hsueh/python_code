#python運算的結果請參考ipynb檔

'''
python數學運算子
運算子	描述	範例
+	加法	5+8
-	減法	90-10
*	乘法	4*7
/	浮點數除法	7 / 2
//	整數除法	7 // 2
%	餘數	7 % 3
**	次方	3 ** 4
'''
#範例：
print((5+8),'加法')
print((90-10),'減法')
print((7/2),'浮點數除法')
print((7//2),'計算商數')
print((7%3),'計算餘數')
print((3**4),'次方計算')

#python的整數
5
print(type(5))

#數字前不可以加0
05

#正整數
print(123)
print(+456)

#負整數
print(-123)
print(-456)

#整數運算
print(5+9)
print(100-7)
print(4-10)

#多個數值運算
print(5+9+3)
print(4+3-2-1+6)

##乘法運算
print(6*7)
print(7*6)
print(6*7*2*3)

#浮點數除法
print(9/5)
print(7//3) #我不太懂在非整除顯示的答案最後一個數字會是顯示5，而非4

#整數除法(只顯示商數)
print(9/5)
    #除數不可為0，否則會………
print(5/0)
    #輸出紶果：ZeroDivisionError: division by zero

#使用變數運算
a=95
print(a)
print(a-3)

#運算結果也可以變成變數
a=95
print(a)
temp=a-3
a=temp
print(a)
#簡化後寫法
a=a-3
a #這邊我不懂，為什麼沒有宣告變數，它卻知道a是95咧？

#餘數計算
print(9%5)

#divmod ->同時得到商與餘數
#語法(被除數,除數)
divmod(7,3)
#答案(2, 1)

#數學運算子優先順序
#先括孤()->次方**->正負數+- ->乘除法* / % //->加減法+- ->等於=
print(2+3*4)
#先算3*4 --->12
#然後再加2 --->14
print((2+3)*4)
#先算2+3 --->5
#再算5*4 --->20
print(2*(1+2)**2-2**2*2)
#先算1+2 --->2*3**2-2**2*2
#再算3**2及2**2 --->2*9-4*2
#再算2*9及4*2 --->18-8
#答案是10

#10進位轉換為2/8/16進位
'''
表示	進位
0b 0B	2進位
0o 0O	8進位
0x 0X	16進位
'''
print(10),print(type(10))
#在2進制輸入10
print(0b10)
#在8進制輸入10
print(0o10)
#在16進制輸入10
print(0x10)

#類型轉換
'''
將內容轉換為不同的資料型態,共4種類型
1 轉換為整數 
2 轉換為浮點數
3 轉換為布林值
4 轉換為字串
'''
#1 轉換為整數
'''
利用 int ( ) 可分別將浮點數、布林值、字串轉換為整數
若符點數非整數，轉換成整數時原則上向 0 取整數
將布林值轉換為整數時，True 會得到 1 而 False 會得到 0
字串內的字元必須是整數才能進行轉換
'''
#浮點數轉換為整數
print(int(4.99)) 
#布林值轉為整數
print(int(True))
print(int(False))
#正負值轉換為整數
print(int('99'))
print(int('-23'))
print(int('+12'))
print(int(-23))
'''
#文字肉容不可以轉換為整數
print(int('99 bottles of beer on the wall'))
#出現錯誤 ValueError: invalid literal for int() with base 10: '99 bottles of beer on the wall'
print(type('99 bottles of beer on the wall'))
#結果為<class 'str'>
#因為變數為文字型態
print(int('98.6')) 
#出現錯誤 ValueError: invalid literal for int() with base 10: '98.6'
print(type('98.6'))
#結果為<class 'str'>
#因為變數為文字型態,小數點被判讀為英文符號的句點
'''
#運算結果轉換為整數
print(4+7.0)
print(int(4+7.0))
print(True+2)
print(int(True+2))
print(False+5.0)
print(int(false+5.0))
#int的範圍
go =10**1000
print(go)
print(go*go)

#2 轉換為浮點數
'''
利用 float ( ) 可分別將整數、布林值、字串轉換為浮點數
將布林值轉換為浮點數時，True 會得到 1.0 而 False 會得到 0.0
字串內的字元必須是數值才能進行轉換
'''
#布林轉換為浮點數(結果會自動在小數點後面補1個0)
print(float(True))
print(int(False))
#整數轉換為浮點數(結果會自動在小數點後面補1個0)
print(float(98))
print(float('99'))
#將帶有小數點的文字類型數字轉換為浮點數
print(float('98.6')) 
print(float('-1.5'))
print(float('1.0e4'))
#與轉換整數不同的是，此處的文字句點被視為浮點

#轉換為布林值
'''
利用 bool ( ) 可分別將整數、浮點數、字串轉換為布林值
原始資料型態為數值時，僅傳入 0 或 0.0 時會回傳 False，其餘皆為 True
原始資料型態為字串時，僅傳入空字串會回傳 False ，其餘皆為 True
'''
print(bool(4.79))
print(bool(13245))
print(bool(0))
print(bool(0.0))
print(bool('False'))
print(bool(-5))
print(bool(''))

#將資料型態轉換為字串
'''
用法 : str ( 欲轉換之內容 )
利用 str ( ) 可分別將整數、浮點數、布林值轉換為字串
'''
print(type(str(377)))
# <class 'str'>
print(type(str(-50)))
# <class 'str'>
print(type(str(5.0)))
# <class 'str'>
print(type(str(True)))
# <class 'str'>
print(type(str(False)))
# <class 'str'>

