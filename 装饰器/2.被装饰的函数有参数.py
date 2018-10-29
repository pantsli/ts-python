'''
# 1. 被修饰的函数有两个参数
# 被修饰的函数有两个参数 需要在生成的新函数new_fun 添加两个形参
# new_fun在调用原函数fun的时候将两个参数传入作为实参

# 2. 被装饰的函数有不定长参数
# 可以使用通用的形参书写形式*args 接收所有的位置参数,**kwargs接收所有的关键字参数
'''
from time import ctime, sleep
# 被修饰的函数有两个参数
def time_fun(fun):
	def new_fun(a,b):
		print('%s called at %s'%(fun.__name__,ctime()))
		fun(a,b)
	return new_fun

@time_fun
def sum(a, b):
	print('%s 的参数 a:%s'%(sum.__name__,a))
	print('%s 的参数 b:%s'%(sum.__name__,b))
	return a + b

# sum(1,2)
# sleep(2)
# sum(3,1)

# 被装饰的函数有不定长参数
def time_fun2(fun):
	def new_fun(*args,**kwargs):
		print('%s called at %s'%(fun.__name__,ctime()))
		fun(*args,**kwargs)
	return new_fun

@time_fun2
def fun(a,b,c):
	print('fun参数 a:',a)
	print('fun参数 b:',b)
	print('fun参数 c:',c)

arg = (1,)
kw = {'b':1,'c':2}
fun(*arg,**kw)