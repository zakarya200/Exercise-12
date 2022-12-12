h = int(input("please entre the number:"))
def n(h):
    
    h //= 10
    if h:
        n(h)
    else:
        return
n(h)
print(h % 10, end=' ')
