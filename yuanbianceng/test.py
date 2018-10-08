from inspect import signature

def spam(x, y, z=42):
    pass


sig = signature(spam)
print(sig)


print(sig.parameters)

bound_type = sig.bind_partial(int, z = int)

print(bound_type.arguments)


bound_value = sig.bind(1,2,3)

print(bound_value.arguments)

