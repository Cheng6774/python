"""if condition:
    true_expressions
else:
    false_expressions
"""
x = 1
y = 2
z = 3
if x > y:
    print('x is greater than y')
else:
    print('x is less or equal to y')

x = 4
y = 2
z = 3
if x > y:
    print('x is greater than y')
else:
    print('x is less or equal y')

#高级主题
"var = var1 if condition else var2"
worked = True
result = 'done' if worked else 'not yet'
print(result)
