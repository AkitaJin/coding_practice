# 装饰器

#装饰器
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

import functools
import datetime

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def exec_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('executed at %s.' % datetime.datetime.now())
        return func(*args, **kw)
    return wrapper

def exec_time_text(msg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('executed at %s with msg: %s' % (datetime.datetime.now(), msg))
            return func(*args, **kw)
        return wrapper
    return decorator

@log
# @exec_time
@exec_time_text('qwe')
def now():
    print('2021年8月16日00:12:24')

f=now
f()