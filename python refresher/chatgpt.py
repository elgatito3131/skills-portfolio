
def count_names(names):
    name_count = {}

    for name in names:
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
    
    return name_count


if __name__ == "__main__":
    names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "elgato", "Alice"]
    result = count_names(names)
    print(result)

'''
def minmaxavg(numbers):
    mini = min(numbers)
    maxi = max(numbers)
    avg = sum(numbers) / len(numbers)

    return {'min': mini, 'max': maxi, 'average': avg}

if __name__ == "__main__":
    numbers = [1, 2, 3, 1, 5, 15, 7, 8, 9, 10]
    result = minmaxavg(numbers)
    print(result)
'''
    
'''
def minmaxavg(numbers):
    min_val = numbers[0]
    max_val = numbers[0]
    total = 0.0

    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
        total += num

    avg = total / len(numbers)

    return {'min': min_val, 'max': max_val, 'average': avg}

if __name__ == "__main__":
    numbers = [1, 2, 3, 1, 5, 15, 7, 8, 9, 10]
    result = minmaxavg(numbers)
    print(result)
'''