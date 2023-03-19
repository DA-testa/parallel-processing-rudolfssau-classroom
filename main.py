# python3

def parallel_processing(n, m, data):
    m
    threads = [0] * n
    result = []
    for d in data:
        worker_index = threads.index(min(threads))
        result.append([worker_index, threads[worker_index]])
        threads[worker_index] += d
    return result
def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for i, t in result:
        print(i, t)

if __name__ == "__main__":
    main()
