import re

#简单示例
print("---简单示例---")
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
mo = phoneNumRegex.search("My number is 415-555-4242")
print('Phone number found: ' + mo.group())

#括号分组
print("括号分组")
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
mo = phoneNumRegex.search("My number is 415-555-4242")
print(mo.group(1)) #组1
print(mo.group(2)) #组2
print(mo.group(0)) #全部
print(mo.group())  #全部
print(mo.groups()) #所有值的元组

#匹配括号
print("---匹配括号---")
phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d)')
mo = phoneNumRegex.search("My number is (415)-555-4242")
print(mo.group(1)) #组1
print(mo.group(2)) #组2

#用|(管道)匹配多个分组
print("---用|(管道)匹配多个分组---")
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

#前缀匹配
print("---前缀匹配---")
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())
print(mo.group(1))

#用问号?实现可选匹配,即零次或1次
print("---用问号?实现可选匹配,即零次或1次---")
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo3 = phoneRegex.search('My number is 415-555-4242')
print(mo3.group())

mo4 = phoneRegex.search('My number is 555-4242')
print(mo4.group())


#用星号*匹配零次或多次
print("---用星号匹配零次或多次---")
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The adventures of Batwowowowoman')
print(mo3.group())

#用加号+匹配一次或多次
print("---用加号+匹配一次或多次---")
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwowowoman')
print(mo2.group())

mo3 = batRegex.search('The adventures of Batman')
print(mo3==None)

#用花括号{}匹配特定次数
print('用花括号{}匹配特定次数')
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2 == None)

#贪心和非贪心匹配
print("贪心和非贪心匹配")
greedyhaRegex = re.compile(r'(Ha){3,5}')#贪心匹配，匹配最长字符串
mo3 = greedyhaRegex.search('HaHaHaHaHa')
print(mo3.group())
nonegreedyhaRegex = re.compile(r'(Ha){3,5}?')
mo4 = nonegreedyhaRegex.search('HaHaHaHaHa')
print(mo4.group())

#findall()方法,返回所有匹配的字符串
print('---findall()方法,返回所有匹配的字符串---')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#无分组
mo = phoneNumRegex.search('cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
mo2 = phoneNumRegex.findall('cell: 415-555-9999 Work: 212-555-0000')
print(mo2)
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #有分组
mo3 = phoneNumRegex.findall('cell: 415-555-9999 Work: 212-555-0000')
print(mo3)

#字符分类
print("---字符分类---")
xmasRegex = re.compile(r'\d+\s\w+') #匹配一个或多个数字，一个空白符，一个或多个（字母/数字/下划线）字符
mo4 = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, '
                        '6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridges')
print(mo4)

#建立自己的字符分类
print("---建立自己的字符分类---")
vowelRegex = re.compile(r'[aeiouAEIOU]') #匹配所有元音字符
mo5 = vowelRegex.findall('Robocop eats baby food. BABY FOOD')
print(mo5)
consonantRegex = re.compile(r'[^aeiouAEIOU]') #匹配所有非元音字符
mo6 = consonantRegex.findall('Robocop eats baby food. BABY FOOD')
print(mo6)

#插入字符^和结束字符$
print('---插入字符^和结束字符$---')
beginsWithHello = re.compile(r'^Hello') #以Hello开始
mo7 = beginsWithHello.search('Hello world!') #Suc
print(mo7)
m8 = beginsWithHello.search('He said hello.') #Fail
print(m8 == None)

endsWithNumber = re.compile(r'\d$') #以数字结束
mo9 = endsWithNumber.search('Your number is 42') # OK
print(mo9)
mo10 = endsWithNumber.search('Your number is 42.') #Fail
print(mo10 == None)

wholeStringIsNum = re.compile(r'^\d+$') #匹配从开始到结束都是数字的字符串
mo11 = wholeStringIsNum.search('1234567890') #ok
print(mo11)
mo12 = wholeStringIsNum.search('123456xyz7890') #fail
print(mo12)
mo13 = wholeStringIsNum.search('12 34567890') #fail
print(mo13)

#通配字符.
print("---通配字符.---") #匹配换行以外的所有字符
atRegex = re.compile(r'.at')
mo14 = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo14)

#用.*匹配所有字符
print('---用.*匹配所有字符---')
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo15 = nameRegex.search('First Name: AL Last Name: Sweigart')
print(mo15.group(1))
print(mo15.group(2))

nonegreedyRegex = re.compile(r'<.*?>') #非贪心模式
mo16 = nonegreedyRegex.search('<To serve man> for dinner>')
print(mo16.group())
greedyRegex = re.compile(r'<.*>') #贪心模式
mo17 = greedyRegex.search('<To serve man> for dinner>')
print(mo17.group())

#用re.DOTALL匹配换行
print('---用re.DOTALL匹配换行---')
noNewlineRegex = re.compile('.*') #不匹配换行
mo18 = noNewlineRegex.search('Serve the public trust. \nProtect '
                             'the innocent. \nUphold the law.')
print(mo18.group())
newlineRegex = re.compile('.*', re.DOTALL)
mo19 = newlineRegex.search('Serve the public trust. \nProtect '
                             'the innocent. \nUphold the law.')
print(mo19.group())

#re.I不区分大小写匹配
print("---re.I不区分大小写匹配---")
robocop = re.compile(r'robocop',re.I)
mo = robocop.search('Robocop is part man, part machine, all cop.')
print(mo.group())

mo = robocop.search('ROBOCOP protects the innocent.')
print(mo.group())

mo = robocop.search('Al, why does your programming book talk about robocop so much?')
print(mo.group())

#用sub()方法替换字符串
print('---用sub()方法替换字符串---')
nameRegex = re.compile(r'Agent \w+')
mo20 = nameRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo20)
agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo21 = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was '
                                      'a double agent.')
print(mo21)






