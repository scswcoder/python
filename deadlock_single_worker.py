import concurrent.futures as cf

def wait_on_future():
    print("inside")
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function.
    print(f.result())
    print("hello")

executor = cf.ThreadPoolExecutor(max_workers=1)
print("submitting")
executor.submit(wait_on_future)

