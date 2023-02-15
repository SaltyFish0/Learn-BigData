class TestContext:

    def __enter__(self):
        # __enter__ 在进入 with 语句块之前被调用，这个方法的返回值赋给了 with 后的 t 变量
        print('__enter__')
        return 1

    # __exit__ 在执行完 with 语句块之后被调用
    # 如果在 with 语句块内发生了异常，那么 __exit__ 方法可以拿到关于异常的详细信息：
    # exc_type：异常类型exc_value：异常对象exc_tb：异常堆栈信息
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('exc_type: %s' % exc_type)
        print('exc_value: %s' % exc_value)
        print('exc_tb: %s' % exc_tb)


with TestContext() as t:
    a = 1 / 0
    print('t: %s' % t)
# 从输出结果我们可以看到，当 with 语法块内发生异常后，__exit__ 输出了这个异常的详细信息，其中包括异常类型、异常对象、异常堆栈。
# 如果我们需要对异常做特殊处理，就可以在这个方法中实现自定义逻辑。
