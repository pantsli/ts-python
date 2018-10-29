def make_bold(fn):
	def new_fn():
		return '<b>'+fn()+'</b>'
	return new_fn

def make_italic(fn):
	def new_fn():
		return '<i>'+fn()+'</i>'
	return new_fn


@make_bold
def f1():
	return '我要学好python'

@make_italic
def f2():
	return '我要学好python'

@make_bold
@make_italic
def f3():
	return '我要学好python'

print(f1())
print(f2())
print(f3())
