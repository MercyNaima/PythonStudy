import time


def timer(func):
    def time_call(*args, **kwargs):
        print("程序开始运行...")
        time_start = time.time()
        result = func(*args, **kwargs)
        time_stop = time.time()
        print("程序运行结束...")
        print(f"共耗时{time_stop - time_start:.2f}秒...")
        return result
    return time_call

