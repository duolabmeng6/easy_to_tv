try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    # print("ic 调试需要安装 pip install icecream")
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa
