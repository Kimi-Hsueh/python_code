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

#多行文字
'''Boom!'''
"""Eek!"""
 #不太懂為什麼多行註解會變成剩下一個單引號
#單行文字(這一段完全看不懂操作)    
poem = "Apple Arcade 推出的最新遊戲《Next Stop Nowhere》，由位於洛杉磯的開發商 Night School Studio 出品。這款遊戲是太空公路之旅的夥伴冒險，其中不同角色間展開了一些精彩的劇情。在銀河系的外圍，每個人和所有事物之間都有充分的空間，Night School 希望這款遊戲可為近來可能感到孤立的玩家提供一些慰藉。"
print(poem)
poem2 = '''Apple Arcade 推出的最新遊戲《Next Stop Nowhere》，由位於洛杉磯的開發商 Night School Studio 出品。

這款遊戲是太空公路之旅的夥伴冒險，其中不同角色間展開了一些精彩的劇情。

在銀河系的外圍，每個人和所有事物之間都有充分的空間，Night School 希望這款遊戲可為近來可能感到孤立的玩家提供一些慰藉。 '''
print(poem2)

#將各個變數已逗號區隔之後，存檔後結果逗號會變成空格的方式顯現出來，但不知道什麼要這麼做
print(99,'bottles','would be enough.') 

#單/雙引號在display之後的結果都會回到一對單引號,如果是使用print指令下，就變為空字串
''
""
''''''
""""""
#Continue Lines with \
alphabet = ''
alphabet += 'abcdefg'
alphabet += 'hijklmnop'
alphabet += 'qrstuv'
alphabet += 'wxyz'
print(alphabet) #結果會自己將所有已宣告的變數組合起來

#連接字串
#當宣告的變數文字內容太長時，可在每個段落後加上"+\"去連結整個變數
black = 'abcdefg' + \
    'hijklmnop' + \
    'qrstuv' + \
    '123456'
print(black)

#這一段我看不懂在寫啥……
1+2+
1+2+\ #這行我不懂為什麼會出現結果

#字串使用加法運算
#字串無法自動加數值
bottles = 99
print(bottles)
print(type(bottles)) #出現的型態為int
base = "" #空字串
base = base + 'current inventory:'
print(base)
print(type(base))
print(base+str(bottles))

#脫溢字元(特殊字元)
'''
- 反斜線作為跳脫字元，可用於引用特殊字元。
如果在字串資料中遇到單引號時，則必須以 \ 來跳脫（escape）處理，避免被誤認為字串結束。
	- \\ 反斜線
	- \’ 單引號
	- \” 雙引號
	- \n 換行
	- \t 固定間隔(Tab分段)
'''
games = '遊戲：《鬼靈精大腳怪》\n說明：今天的遊戲更新為玩家開啟了一個全新的探索環境。從城鎮下方的新碼頭出發，乘渡輪前往新的小島，然後乘坐四輪驅動車四處巡遊，或者在衝浪遊戲中盡情衝浪。玩家還可以購買新船進行升級與比賽，或是出海捕捉鹹水魚。這是調皮大腳怪的暑假！\n\n遊戲：《迷你公路》\n說明：《迷你公路》推出了一項新更新，以透過 Fast Forward 模式協助加快道路網絡的建立，使玩家能選擇其遊戲速度。' 
print(games)

#\t ->Tab分段
print('\tabc')
print('a\tbc')
print('ab\tc')
print('abc\t')

#\" 顯示雙引符號 ->先斜線再雙引號
testimony = "\"I did nothing!\" he said. \"Not that either! Or the other thing.\""
print(testimony)
test = "I did nothing! he said.Not that either! Or the other thing."
print(test)
#在這邊可以比較一下輸出結果

fact = "The world's largest rubber duck was 54'2\" by 65'7\" by 105'"
print(fact)

speech = 'Today we honor our friend, the backslash: \\.' 
print(speech)

# 使用"+"運算子組合文字段落
print('Release the kraken! ' + 'At once!')

#使用"+"運算子組合變數
a = 'Duck.'
b=a
c = 'Grey Duck!' 
print(a, b, c) 
print(a+b+c)

# 資料輸入
'''
input 代表資料輸入
輸入資料後可利用變數 .class 方式查詢變數的資料型態。
預設輸入的資料型態為字串
若是整數資料您必須加入 int( ) 轉換。
如果輸入浮點數或者字串都會產生錯誤訊息。
若是浮點數小數資料您必須加入 float( ) 轉換。
如果輸入整數會當作浮點數處理，輸入字串會產生錯誤訊息。
'''


#建立1個input01.py
#input01.py檔案內容：
# input01.py
a = input("輸入整數1a: ") 
b = input("輸入整數1b: ") 
c = int(input("int輸入c:")) 
d = int(input("int輸入d:")) 
f=a+b
g=c+d 
print(f)
print(g)

#建立1個input02.py
#input02.py檔案內容
# input02.py

c = int(input("int輸入c:"))
d = int(input("int輸入d:")) 
g=c+d
print(g) #此為整數運算
h = float(input("float輸入h:"))
i = float(input("float輸入i:"))
j=h+d
print(j) #此為浮點數運算

# input02.py

c = int(input("int輸入c:"))
d = int(input("int輸入d:")) 
g=c+d
print(g)
h = float(input("float輸入h:"))
i = float(input("float輸入i:"))
j=h+d
print(j)

#建立1個input03.py
#input03.py檔案內容
# input03.py

a = input("輸入字串: ")
print(a,a.__class__ ) 
a = input("輸入整數: ") 
print(a,a.__class__ )#出現的結果為str，因為input預設的輸入資料型態為字串
a = float(input("float輸入浮點數: "))
print(a,a.__class__ )
a = int(input("int輸入整數:"))
print(a,a.__class__ )#因為在input前面已經有了int的資料類型轉換
a = int(input("int輸入字串:"))
print(a,a.__class__ )#在此處如果輸入數字的文字會是int型態，但如果輸入文字，則會出現錯誤訊息

#練習題
'''
question:以下的資料輸出哪一個是錯的?(選擇題)
(1) "I can add integers, like " + str(5) + " to strings." ->正確，因為是str型態相加
(2) "Isaid"+("Hey"*2)+"Hey!" ->正確，因為是str型態運算
(3) "The correct answer to this multiple choice exercise is answer number" + 2 ->錯誤，因為是str+int，運算不可以是不同型態的 
(4) True + False 正確，因為是布林值運算
'''
'''
question:請問執行後的說明哪一個是對的?(選擇題)
a,b,c="pcschool",2016,3.41
print(b)
(1) 2016 正確
(2) 3.41
(3) pcschool
'''
'''
請問執行後的說明哪一個是對的?(選擇題)
test=("abc"+"!")*2
print(test)
(1) abc!2
(2) abc! abc! 正確
(3) abc+!*2
'''
'''
question: 請問計算後Z的內容哪一個是對的?(選擇題)
x=5
y=7 
z=x+y+1
(1) 571 
(2) 1
(3) 13 正確，因為變數為int型態
'''
'''
#num.py
a,b,c=4,2,5
d,f=3.25,5.5
print (a*b) # 8
print (a**b) # 16
print (a % 3) # 1 餘數除法
print (d + f) # 8.75
print (c//b) # 2.5 商數除法
print (a/b) # 2 浮點數除法
'''
'''
question: 請問執行後的說明哪一個是對的?(選擇題)
g,h=9,3
print(g/h)
(1) 3 
(2) 0 
(3) 3.0 正確，因為是浮點數除法
'''
'''Homework(mathop.py):
讓使用者輸入被除數(整數)及除數(整數，不可以是零)
程式會顯示兩數相除的商及餘數。
請輸入被除數(整數):45
請輸入除數(整數,不可以為0):4
商 11 餘數: 1
'''
x=int(input('請輸入被除數:'))
y=int(input('被除數:'))
print('商=',x//y)
print('餘數=',x%y)

'''
Homework(plus_s.py):
計算使用者輸入的2個任意數，程式會顯示2數相加的總和。
請輸入第一個數值:45.67
請輸入第二個數值:67.47
兩個數的和是xxx.xx
'''
import decimal
x=float(input('請輸入任意小數點數字:'))
y=float(input('請再次輸入任意小數點數字:'))
print(x)
print(y)
print('相加結果=',x+y) 

#複合指定運算子
'''
當「=」左右兩邊是相同資料時可以使用精簡方式:
省略「=」右邊相同資料。
將「=」右邊的計算符號移到「=」左邊。
'''
#操作範例1
    #原始範例
x=int(input('請輸入整數數字:'))
x=x+2
print(x)
    #精簡過後
x=int(input('請輸入整數數字:'))
x+=2
'''
精簡的內容如下
Step1 ->把x=x+2相同的x變成1個
Step2 ->x=+2的加號移至等號的左邊
Step3 ->結果為x+=2
'''
print(x)

#操作範例2
    #原始範例
y=int(input('請轉入大於3的數字:'))
y=y-3
print(y)
    #精簡過後
y=int(input('請轉入大於3的數字:'))
y-=3
'''
精簡的內容如下：
Step1 ->把y=y-3相同的y變成1個
Step2 ->把y=-3的減號移至等號的左邊
Step3 ->結果為y-=3
'''
print(y)

#操作範例3-自己出的題目
x=int(input('請輸入任意整數數字x='))
y=int(input('請輸入任意整數數字y='))
#原算式 x=x*2
x*=2
print(x)
#原算式 y=y+8
y+=8
print(y)

#把最終的計算結果相加
#原算式 x=x*2,y=y+8
x=int(input('請輸入任意整數數字x='))
y=int(input('請輸入任意整數數字y='))
x*=2
y+=8
print('計算過後的x=',x)
print('計算過後的y=',y)
print(x+y)

'''
Homework(complex.py):
請使用者輸入一個任意數，程式會顯示此數的平方值及立方值
'''
x=int(input('請給我一個整數'))
a=x**2
b=x**3
print('輸入數字的平方為',y)
print('輸入數字的立方為',b)

'''
Homework(complex_s.py):
請以(複合指定運算子)設計程式,讓用者輸入三個任意數，程式會顯示3數相加的總和(float)
'''
#原算式
a=float(input('給我第一個數字'))
b=float(input('給我第二個數字'))
c=float(input('給我第三個數字'))
d=a+b+c
print('你剛剛給我三個數字的相加是',d)
#複合指定運算子
total=0
keyin=float(input('給我第一個數字'))
total+=keyin
keyin=float(input('給我第二個數字'))
total+=keyin
keyin=float(input('給我第三個數字'))
total+=keyin
print(total)
'''
Homework(ladder.py):
讓使用者輸入梯形的上底、下底及高，程式會計算梯形的面積(上底加下底乘以高除以2)
'''
top=float(input('請給我梯形的上底'))
buttom=float(input('請給我梯形的下底'))
heigh=float(input('請給我梯形的高'))
print('梯形的上底',top,'公分')
print('梯形的下底公分',buttom,'公分')
print('梯形的高',heigh,'公分')
x=(top+buttom)*heigh/2
print('梯形的面積',round(x,ndigits=3),'平方公分')
#四捨五入到第幾位的函數 ->round(變數,ndigits=小數點後第幾位)\
'''
Homework(degree.py)
讓使用者輸入直角三角形的對邊
讓使用者輸入直角三角形的斜邊
計算角度
公式:
sin(x) = 對邊 / 斜邊
x是radian(弧度)
'''
import math #掛載python數學模組
x=float(input('請輸入對邊'))
y=float(input('請輸入斜邊'))
redian=math.asin(x/y) #此部份是計算圓周的孤度
degress=math.degrees(redian) #此部份是利用math模組內的degress功能計算出夾角
round(degress,ndigits=3) #此部份是四捨五入至小數點後2位
print('對邊',x,'cm','斜邊',y,'cm','角度',degress,'度')