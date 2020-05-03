str_ = input("""Enter text: """)
def func_str(str_):
    for item in str_:
        if item in [',', '.', '!', '?', ':', ';', '/']:
            str_ = str_.replace(item , '')
    return str_
            
print(func_str(str_))
