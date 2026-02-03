# import time
# from functools import wraps
# def timer(fn):  #fn = processing_time_dec(math)
#     @wraps(fn)
#     def inner(*args,**kwargs):
#         start_time = time.perf_counter()
#         res = fn(*args,**kwargs)
#         end_time = time.perf_counter()
#         print(f"Function compeleted in {(end_time - start_time):.6f} seconds")
#         return res
#     return inner
# # # # @timer
# # # # def hi():
# # # #     print("Barev Ashxarh")

# # # # hi()


# # # def proccesing_time_dec(fn): #fn = math
# # #     count = 0
# # #     @wraps(fn)
# # #     def inner(*args,**kwargs):
# # #         nonlocal count
# # #         count += 1
# # #         res = fn(*args,**kwargs)
# # #         print(f"Function called {count} times")
# # #         return res
# # #     return inner

# # # # @proccesing_time_dec # hii = proccesing_time_dec(hii)
# # # # def hii():
# # # #     print("1 + 1 = 11")

# # # # hii()
# # # # hii()
# # # # hii()
# # # # hii()
# # # # hii()
# # # # hii()


# # # @proccesing_time_dec
# # # @timer 
# # # def math():    #math = timer(processing_time_dec(math))
# # #     print("2 + 2 = 22")

# # # math()

# # def repeat(n):
# #     def dec(fn):
# #         def inner(*args,**kwargs):
# #             for i in range(n):
# #                 res=fn(*args,**kwargs)
# #             return res
# #         return inner
# #     return dec
            
# # @repeat(0)
# # def say_hello():
# #     print("Hello")
# # say_hello()


# def f(n):
#     if n==1:
#         return 1
#     return n*f(n-1)
# # print(f(5))  

# @timer
# def factorial_helper(n):
#     return f(n)
# print(factorial_helper(5))

# def foo(a: int) -> None:
#     '''This function do anything'''
#     ...

# help(foo)

def dec(fn):
    def innher(*args,**kwargs):
        res=fn(*args,**kwargs)
        if  isinstance(res,str):
            return res.upper()
        return res
    return innher

@dec
def foo():
    return "Hello world"

print(foo())

def foo1():
    return 15

print(foo1())
    