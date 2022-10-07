def call_value(x):
	print(id(x))
	x += 1
	print(id(x))
	print("in_func_x:",x)
  return x

x = 5
xNew = 0
xNew = call_value(x)
print(id(x))
print("out_func_x:",xNew)