class Person():
	# 只要对象重写了__call__方法,那么这个对象就是callable的
	def __call__(self):
		print('call me!')

# p1 = Person()
# p1()


class Test(object):
	def __init__(self,fun):
		print('执行Test的__init__方法~~~')
		self.__fun = fun
	def __call__(self):
		print('执行Test的 __call__方法~~~')
		print('装饰器的功能~~~')
		self.__fun()

def test():
	print('test函数执行~~~')
test = Test(test)

@Test
def test2():
	print('test2函数也执行~~~')

test()
test2()
