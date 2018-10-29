from time import ctime, sleep

def time_fun_arg(who='hellp'):
	def time_fun(fun):
		print('who am i ?',who)
		def new_fun():
			print(who,'打印:')
			print('%s called at %s'%(fun.__name__,ctime()))
			fun()
		return new_fun
	return time_fun

# @time_fun_arg('孙悟空') 可以理解为 foo = time_fun_arg('孙悟空')(foo)
@time_fun_arg('孙悟空')
def foo():
	print('I am foo')

@time_fun_arg('唐僧')
def bar():
	print('I am bar')

# foo()==timefun_arg("孙悟空")(foo)()
foo()
foo()
# bar()==timefun_arg("唐僧")(foo)()
bar()
bar()
bar()
