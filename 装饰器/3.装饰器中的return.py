'''
# new_fun函数中接收原函数fun的执行结果result
# new_fun函数返回原函数fun的执行结果result
'''
from time import ctime, sleep

def time_fun(fun):
	def new_fun(a,b):
		print('%s called at %s'%(fun.__name__,ctime()))
		# 定义变量result接收原函数fun的执行结果
		result = fun(a,b)
		# new_fun函数返回原函数fun的执行结果result
		return result
	return new_fun

@time_fun
def sum(a, b):
	return a + b

result = sum(123,456)
print('sum的返回结果:',result)