from aocd import get_data, submit

def time_it(func, name=None):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        n = name if name else func.__name__
        print(f"-  Runtime: {end-start} seconds")
        return result
    return wrapper

# Runner
def part(part, day, year, func, submit_to_aoc):
    print(f'-- Part {part}')
    result = str(time_it(func)())
    print("-  Result:  " + result)
    if submit_to_aoc and result != "None":
        print("-  Submitting...")
        p = "a" if part == "One" else "b"
        submit(result, part=p, day=day, year=year)
    else:
        print("-  Not Submitting!")
    print()