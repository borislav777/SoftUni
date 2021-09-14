from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(args)

    while nums:
        for key, value in kwargs.items():
            if nums:
                if key == 'a':
                    kwargs[key] += nums.popleft()
                elif key == 's':
                    kwargs[key] -= nums.popleft()
                elif key == 'd':
                    try:
                        kwargs[key] /= nums.popleft()
                    except ZeroDivisionError:
                        pass
                elif key == 'm':
                    kwargs[key] *= nums.popleft()
    return kwargs




print(math_operations(6, a=0, s=0, d=0, m=0))
