# 第二章 Python入门（视频11-38）

## 什么是计算机语言
    计算机就是一台用来计算机的机器，人让计算机干什么计算机就得干什么！
    需要通过计算机的语言来控制计算机（编程语言）！
    计算机语言其实和人类的语言没有本质的区别，不同点就是交流的主体不同！
    计算机语言发展经历了三个阶段：
        机器语言
            - 机器语言通过二进制编码来编写程序
            - 执行效率好，编写起来太麻烦

        符号语言（汇编）
            - 使用符号来代替机器码
            - 编写程序时，不需要使用二进制，而是直接编写符号
            - 编写完成后，需要将符号转换为机器码，然后再由计算机执行
                符号转换为机器码的过程称为汇编
            - 将机器码转换为符号的过程，称为反汇编  
            - 汇编语言一般只适用于某些硬件，兼容性比较差  

        高级语言
            - 高级语言的语法基本和现在英语语法类似，并且和硬件的关系没有那么紧密了
            - 也就是说我们通过高级语言开发程序可以在不同的硬件系统中执行
            - 并且高级语言学习起来也更加的容易，现在我们知道的语言基本都是高级语言
            - C、C++、C#、Java、JavaScript、Python 。。。

## 编译型语言和解释型语言
    计算机只能识别二进制编码（机器码），所以任何的语言在交由计算机执行时必须要先转换为机器码，
        也就是像 print('hello') 必需要转换为类似 1010101 这样的机器码   

    根据转换时机的不同，语言分成了两大类：
        编译型语言
            - C语言
            - 编译型语言，会在代码执行前将代码编译为机器码，然后将机器码交由计算机执行
            - a(源码) --编译--> b(编译后的机器码)
            - 特点：
                执行速度特别快
                跨平台性比较差

        解释型语言 
            - Python JS Java
            - 解释型语言，不会在执行前对代码进行编译，而是在执行的同时一边执行一边编译
            - a（源码）--解释器--> 解释执行  
            - 特点：
                执行速度比较慢
                跨平台性比较好   

## Python的介绍   
    Python是解释型语言

    Python（英国发音：/ˈpaɪθən/ 美国发音：/ˈpaɪθɑːn/），是一种广泛使用的高级编程语言，属于通用型编程语言，由吉多·范罗苏姆创造，第一版发布于1991年。可以视之为一种改良（加入一些其他编程语言的优点，如面向对象）的LISP。作为一种解释型语言，Python的设计哲学强调代码的可读性和简洁的语法（尤其是使用空格缩进划分代码块，而非使用大括号或者关键词）。相比于C++或Java，Python让开发者能够用更少的代码表达想法。不管是小型还是大型程序，该语言都试图让程序的结构清晰明了。 

    Life is short you need Python （人生苦短，我用Python）    

    Python的用途：
        WEB应用
            Facebook 豆瓣 。。。
        爬虫程序
        科学计算
        自动化运维
        大数据（数据清洗）
        云计算
        桌面软件/游戏
        人工智能
        。。。     

## Python开发环境搭建
    开发环境搭建就是安装Python的解释器
    Python的解释器分类：
        CPython（官方）
            用c语言编写的Python解释器
        PyPy
            用Python语言编写的Python解释器
        IronPython
            用.net编写的Python解释器
        Jython
            用Java编写的Python解释器

    步骤：
        1.下载安装包 python-3.6.5.exe
            - 3.x
            - 2.x    
        2.安装（傻瓜式安装） 
        3.打开命令行窗口，输入python 出现如下内容
            Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
            Type "help", "copyright", "credits" or "license" for more information.
            >>>    

## Python的交互界面
    当我们通过命令行来输入Python，所进入到的界面就是Python的交互界面
    结构：
        版本和版权声明：
        Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
        Type "help", "copyright", "credits" or "license" for more information.

        命令提示符：
        >>>

        在命令提示符后可以直接输入Python的指令！输入完的指令将会被Python的解释器立即执行！

        安装Python的同时，会自动安装一个Python的开发工具IDLE，通过IDLE也可以进入到交互模式
        但是不同的是，在IDLE中可以通过TAB键来查看语句的提示。
        IDLE实际上就是一个交互界面，但是他可以有一些简单的提示，并且可以将代码保存

    交互模式只能你输入一行代码，它就是执行一行，所以他并不适用于我们日常的开发！ 
        仅可以用来做一些日常的简单的测试！   

    我们一般会将Python代码编写到一个py文件中，然后通过python指令来执行文件中的代码

    练习：
        自己尝试创建一个py文件，并向文件中写入python打印语句（print...） 
            然后执行该文件。
        如果你的系统的扩展名无法修改，请尝试自行baidu！

## Python和Sublime的整合
    1.在Sublime中执行Python代码，ctrl + b 自动在Sublime内置的控制台中执行  
        这种执行方式，在某些版本的Sublime中对中文支持不好，并且不能使用input()函数

    2.使用SublimeREPL来运行python代码    
        安装完成，设置快捷键，希望按f5则自动执行当前的Python代码
        { "keys": ["f5"], "caption": "SublimeREPL:Python","command": "run_existing_window_command", "args":{"id": "repl_python_run","file": "config/Python/Main.sublime-menu"}},

## 几个概念
    1.表达式
        表达式就是一个类似于数学公式的东西
        比如：10 + 5   8 - 4
        表达式一般仅仅用了计算一些结果，不会对程序产生实质性的影响
        如果在交互模式中输入一个表达式，解释器会自动将表达式的结果输出

    2.语句
        在程序中语句一般需要完成某种功能，比如打印信息、获取信息、为变量赋值。。。
        比如：
            print()
            input()
            a = 10
        语句的执行一般会对程序产生一定的影响
        在交互模式中不一定会输出语句的执行结果  

    3.程序（program）
        程序就是由一条一条的语句和一条一条的表达式构成的。

    4.函数（function）
        函数就是一种语句，函数专门用来完成特定的功能
        函数长的形如：xxx()          
        函数的分类：
            内置函数
                - 由Python解释器提供的函数，可以在Python中直接使用
            自定义函数   
                - 由程序员自主的创建的函数
        当我们需要完成某个功能时，就可以去调用内置函数，或者自定义函数 
        函数的两个要素：
            参数
                - ()中的内容就是函数的参数
                - 函数中可以没有参数，也可以有多个参数，多个参数之间使用,隔开
            返回值        
                - 返回值是函数的返回结果，不是所有的函数都有返回值
## 基本语法
    1.在Python中严格区分大小写
    2.Python中的每一行就是一条语句，每条语句以换行结束
    3.Python中每一行语句不要过长（规范中建议每行不要超过80个字符）
        "rulers":[80],
    4.一条语句可以分多行编写，多行编写时语句后边以\结尾  
    5.Python是缩进严格的语言，所以在Python中不要随便写缩进  
    6.在Python中使用#来表示注释，#后的内容都属于注释，注释的内容将会被解释器所忽略
        我们可以通过注释来对程序进行解释说明，一定要养成良好的编写注释的习惯
        注释要求简单明了，一般习惯上#后边会跟着一个空格


## 字面量和变量
    字面量就是一个一个的值，比如：1，2，3，4，5，6，‘HELLO’
        字面量所表示的意思就是它的字面的值，在程序中可以直接使用字面量

    变量（variable）变量可以用来保存字面量，并且变量中保存的字面量是不定的
        变量本身没有任何意思，它会根据不同的字面量表示不同的意思

    一般我们在开发时，很少直接使用字面量，都是将字面量保存到变量中，通过变量来引用字面量

## 变量和标识符
## 数据类型   
    数据类型指的就是变量的值得类型，也就是可以为变量赋哪些值 
    数值
        整型
            布尔值
        浮点型
        复数
    字符串
    空值

## 类型检查
## 对象（object）
    - Python是一门面向对象的语言
    - 一切皆对象！
    - 程序运行当中，所有的数据都是存储到内存当中然后再运行的！
    - 对象就是内存中专门用来存储指定数据的一块区域
    - 对象实际上就是一个容器，专门用来存储数据
    - 像我们之前学习的数值、字符串、布尔值、None都是对象
    - 参考 图1

## 对象的结构
    - 每个对象中都要保存三种数据
        - id（标识）
            > id用来标识对象的唯一性，每一个对象都有唯一的id
            > 对象的id就相当于人的身份证号一样
            > 可以通过id()函数来查看对象的id
            > id是由解析器生成的，在CPython中，id就是对象的内存地址
            > 对象一旦创建，则它的id永远不能再改变

        - type（类型）
            > 类型用来标识当前对象所属的类型
            > 比如：int str float bool 。。。
            > 类型决定了对象有哪些功能
            > 通过type()函数来查看对象的类型
            > Python是一门强类型的语言，对象一旦创建类型便不能修改


        - value（值）
            > 值就是对象中存储的具体的数据
            > 对于有些对象值是可以改变的
            > 对象分成两大类，可变对象 不可变对象
                可变对象的值可以改变
                不可变对象的值不能改变，之前学习的对象都是不可变对象
        - 参考 图2

    练习：尝试自己画一下对象的内存结构。  

## 变量和对象
    - 对象并没有直接存储到变量中，在Python中变量更像是给对象起了一个别名
    - 变量中存储的不是对象的值，而是对象的id（内存地址），
        当我们使用变量时，实际上就是在通过对象id在查找对象
    - 变量中保存的对象，只有在为变量重新赋值时才会改变
    - 变量和变量之间是相互独立的，修改一个变量不会影响另一个变量

    - 参考 图3

## 类型转换
    - 所谓的类型转换，将一个类型的对象转换为其他对象
    - 类型转换不是改变对象本身的类型，而是根据当前对象的值创建一个新对象

## 运算符(操作符)
    - 运算符可以对一个值或多个值进行运算或各种操作
    - 比如 + 、-、= 都属于运算符
    - 运算符的分类：
        1.算术运算符
        2.赋值运算符
        3.比较运算符（关系运算符）
        4.逻辑运算符
        5.条件运算符（三元运算符）    

