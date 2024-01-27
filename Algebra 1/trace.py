def trace(func):
    """Declaration of annotation.
    @trace can be placed before a function (global, local, or method) definition
    to cause diagnostic information to be printed when the function is called,
    and when the function returns.
    """
    depth = dict()

    def wrapper(*args, **kwargs):
        name = func.__name__
        if name not in depth:
            depth[name] = 0
        depth[name] += 1
        print(f"{depth[name]}: {'[' * depth[name]} {name}{args}")
        val = func(*args, **kwargs)
        print(f"{depth[name]}: {']' * depth[name]} {name} --> [{type(val).__name__}] {val}")
        depth[name] -= 1
        return val

    return wrapper
