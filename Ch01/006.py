# 006

# 變數指定(=)
# 將 tuple 指定為 x
x = (1, 2, 3)
print(x)

# 將 list 指定為 x
x = [1, 2, 3]
print(x)

# 變數移除(del)
del x
# 移除變數後再取用該變數會發生錯誤 -> NameError: name 'x' is not defined
# print(x)

# 運算賦值(+=.-=.*=./=.//=.**=.%=)
x = 1
print(x)
x += 1
print(x)
x -= 1
print(x)
x *= 3
print(x)
x /= 3
print(x)

# 平方運算
x = 2
print(x)
x **= 3
print(x)

# 地板除法
x = 27
print(x)
x //= 4
print(x)

# 餘數
x = 27
print(x)
x %= 4
print(x)

# 顯示當前變數(dir. globals. locals)
# dir: 顯示變數
# output: ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'x']
print(dir())

# globals: 顯示全域變數
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001E274DF6CD0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\2.Project\\SideProject\\Python-practice\\ch01\\006.py', '__cached__': None, 'x': 3}
print(globals())

# locals: 顯示區域變數
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001E274DF6CD0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\2.Project\\SideProject\\Python-practice\\ch01\\006.py', '__cached__': None, 'x': 3}
print(locals())

# 查詢變數型態(type)
x = 1
t = type(x)
print(t)

y = 1.0
print(type(y))

x = "123"
print(type(x))

x = [1, 2, 3]
print(type(x))

x = (1, 2, 3)
print(type(x))

x = {}
print(type(x))
