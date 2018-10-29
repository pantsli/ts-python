# 在fun函数开始执行前打印开始执行,执行完毕是打印执行结束
def begin_end(fun):
	# fun是被装饰的函数
	# new_fun是通过装饰器生成的新函数,它对fun函数进行功能增强
	# *args: 通用的用于收集位置参数的方法,**kwargs: 用于收集关键字参数
	def new_fun(*args,**kwargs):
		print('开始执行')
		result = fun(*args,**kwargs)
		print('执行结束')
		# 将fun的执行结果返回
		return result
	# 将增强后的函数返回
	return new_fun

@begin_end
def fun():
	print('我是fun函数')

# fun()

@begin_end
def sum(a, b):
	return a + b

result = sum(1,2)
print('sum函数的返回结果,result:',result)

@begin_end
def show(*,name,age):
	print('你的名字是:',name)
	print('你的年龄是:',age)
kw = {'name':'孙悟空','age':18}
show(**kw)