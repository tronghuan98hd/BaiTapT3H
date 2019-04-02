samples = ["python", None, "cpython", True, 1, 1 + 1j, False, [100, 200, 300], 99.99, (31, "January")]
result = []
for data in samples:
    if not isinstance(data, (int, float, complex)):
        result.append(data)
print(result)

#['python', None, 'cpython', [100, 200, 300], (31, 'January')]

