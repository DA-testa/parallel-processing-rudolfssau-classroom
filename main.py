# python3
import concurrent

def parallel_processing(n, m, data):
    output = []
    threads = [0] * n
    with concurrent.futures.ThreadPoolExecutor(max_workers=n) as executor:
        futures = []
        for value in data:
            future = executor.submit(process_value, value, threads)
            futures.append(future)
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            output.append(result)
    return output

def process_value(value, threads):
    thread_index = threads.index(min(threads))
    threads[thread_index] += value
    return (thread_index, threads[thread_index])

def main():
    imp = list(map(int, input().split()))
    n = imp[0]
    m = imp[1]
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for value in result:
        print(value[0], value[1])

if __name__ == "__main__":
    main()
