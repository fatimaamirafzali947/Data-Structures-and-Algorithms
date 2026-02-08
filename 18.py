#تابع بازگشتی به شکل زیر داریم. مقدار x(5,3) را محاسبه کنید.
def x (a,b):
    if a<b:
        return a+b
    return x (a-1, b)
