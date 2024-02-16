
from functools import reduce

number = 153

# This lambda function below
add_digits = reduce(lambda x, y: (int(x) + int(y)), list(map(lambda x: x, str(number))))

print(add_digits)