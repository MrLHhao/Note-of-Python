
+#函数
  sys.exit() 让程序终止或退出。调用前需导入sys模块。
 +type（）：返回变量类型；
 +isinstance（a, b）：判断a与b类型是否相同，相同返回True，否则返回False。参数b需为数据类型或tuple；
 +not 操作符：将布尔类型结果反转 not True = False；
 +small = x if  x<y else y ：如果if条件成立，y赋值给small，否则x赋值给small
 +assert 断言：当这个关键字后面条件为假时，程序自动崩溃并抛出assertionError的异常。用于在程序中置入检查点，确保某一条件为真时才能继续执行。
 +资格运算符：检查一个值是否在序列中。如s=123， 1 in s → True。
 +for 循环： for 目标 in 表达式 ：循环体。
 +range(start, stop, step):其中start和step为可选参数，start默认从0 开始，step默认为1，从start按步长step生成到stop 的序列（闭开区间）。
 +continue：中止本次循环并进行下一次循环。（开始前会判断条件是否成立）。
 +break：跳出循环。
 +input(): 函数总是返回一个字符串
 +
 +#列表[list]
 +.append(): 向列表添加元素。每次只能添加一个。
 +.extend(): 用一个列表扩展另一个列表。参数需要为列表。
 +.insert(,): 向列表指定位置插入一个元素，第一个参数为插入位置，第二个参数为元素。
 +.remove(): 从列表中删除元素，参数为列表元素，不需要知道所在位置。
 +del(): del(列表名[位置]) 删除对应位置元素，也可以直接删除列表。
 +.pop(): 默认删除列表最后一个元素，加参数值，删除对应位置元素。
 +.copy(): 复制列表。
 +.clear(): 清空列表，清空后变为空列表，列表仍然存在。
 +.sort(): 对列表进行顺序排列。.sort(reverse=True)倒序排列。
 +.reverse(): 将列表进行翻转。
 +分片：列表名[a:b],截取a~b闭开区间元素，参数a默认0，参数b默认最后。分片方法拷贝后生成新的副本，不随原列表变化，通过’=’拷贝的列表随原列表变化。
 +列表解析，灵感取自函数式编程语言 Haskell。Ta 是一个非常有用和灵活的工具，可以用来动态的创建列表，语法如： [有关A的表达式 for A in B]
 +  例如
 +		>>> list1 = [x**2 for x in range(10)]
 +		>>> list1
 +		[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
 +		相当于
 +		list1 = []
 +		for x in range(10):
 +		list1.append(x**2)
 +
 +#元组(tuple)
 +元组创定义后不可修改。创建元组圆括号不是关键，关键在于逗号。创建空元组，元组名=（）；创建只有一个元素的元组，需要在元素后加’,’，如tuple =(1,)。
 +向元组中增加，通过切片方式间接实现：
 +	temp = (‘小甲鱼’,’黑夜’,’迷途’,’小布丁’)；
 +	temp=temp[:2]+(‘怡静’,)+temp[2:] 注意逗号
 +	temp = (‘小甲鱼’,’黑夜’,’ 怡静’,’迷途’,’小布丁’)
 +删除元组 del 
 +
 +#字符串'str'
 +修改字符串方法同元组切片方法。
 +.capitalize(): 第一个字母大写。返回新字符串，原字符串不变。
 +.casefold(): 全部小写。返回新字符串，原字符串不变。
 +.center(width): 将字符串居中，并使用空格填充至长度width的新字符串。
 +.count(sub[start[,end]]): 返回sub在字符串中出现的次数，start和end参数表示范围，可选。
 +.encode(endoding=’utf-8’,errors=’strict’): 以encoding指定的编码方式对字符串进行编码。
 +.endswith(sub[,strat[,end]]): 检查字符串是否乙sub子字符串结束，如果是返回True，否则返回False，start和end参数表示范围，可选。
 +.expandtabs([tabsize=8]): 把字符串中的tab符号(\t)转换为空格，如果不指定参数，默认的空格数是tabsize=8。
 +.find(sub[,start[,end]]): 检测sub是否包含在字符串中，如果有则返回索引值，否则返回-1，start和end参数表示范围，可选。
 +.index(sub[,start[,end]]): 与find方法一样，不过如果sub不在字符串中会产生一个异常。
 +.join(sub): 以字符串作为分隔符，插入到sub中所有的字符之间。
 +.ljust(width): 返回一个左对齐的字符串并使用空格填充至长度为width的新字符串。
 +.lstrip(): 去掉字符串左边的所有空格。
 +.partition(): 找到子字符串sub，把字符串分成一个3元组(pre_sub,sub,fol_sub)，如果字符串中不包含sub，则返回’原字符串’,’ ’,’ ’)。
 +.replace(old,new[,count]): 字符串中的old子字符串替换成new子字符串，如果count指定，则替换不超过count次。
 +.rfind(sub[,start[,end]]): 类似find()方法，从右边开始查找。
 +.rindex(sub[,start[,end]]): 类似index()方法，从右边开始。
 +.rjust(width):返回一个右对齐的字符串，并使用空格填充至长度为width的新字符串。
 +.split(sep= None,maxsplit=-1): 不带参数默认以空格为分隔符切片字符串，如果maxsplit参数有设置，则仅分隔maxsplit个子字符串，返回切片后的子字符串拼接的列表。
 +.strip([chars]): 删除字符串前边和后边的所有空格，chars参数可以指定删除的字符，可选。
 +.swapcase(): 反转字符串中的大小写。
 +.title(): 返回标题划（返回的单词都是以大写开头，其余字母均小写）的字符串。
 +.translate(table): 根据table的规则（可以有str.maketrans(‘a’,’b’)定制），转换字符串中的字符。
 +.upper(): 转换字符串中的所有小写字母为大写。
 +.isalnum():	所有字符都是数字或者字母，为真返回True，否则返回False。
 +.isalpha():	所有字符都是字母，为真返回True，否则返回False。
 +.isdigit():	所有字符都是数字，为真返回True，否则返回False。
 +.islower():	所有字符都是小写，为真返回True，否则返回False。
 +.isupper():	所有字符都是大写，为真返回True，否则返回False。
 +.istitle():	所有单词都是首字母大写，为真返回True，否则返回False。
 +.isspace():	所有字符都是空白字符，为真返回True，否则返回False。
