'''
理解装饰器的执行行为
# 1. foo先作为参数赋值给fun后,foo 接收指向time_fun返回的new_fun
@time_fun <=> foo = time_fun(foo) <=> foo = new_fun

# 2. 表示调用foo函数,等价与new_fun()
# 内部函数new_fun被引用,所以外部函数的fun变量并没有释放,fun指向的是原来的foo函数对象
foo() <=> new_fun()
'''
from time import ctime, sleep

def time_fun(fun):
	def new_fun():
		print('%s called at %s'%(fun.__name__,ctime()))
		fun()
	return new_fun
# @time_fun 等价与 foo = time_fun(foo), foo先作为参数赋值给fun后,foo 接收指向time_fun返回的new_fun
# 即: foo = new_fun
@time_fun
def foo():
	print('I am foo')
# foo():表示调用foo函数,等价与new_fun()
# 内部函数new_fun被引用,所以外部函数的fun变量并没有释放,fun指向的是原来的foo函数对象
foo()
sleep(2)
foo()