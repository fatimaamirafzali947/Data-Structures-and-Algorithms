#تابعی بنویسید که حاصلضرب a در b را بصورت بازگشتی محاسبه کند.
def zarb (a, b):
    if b==1:
        return a
    return zarb (a, b-1)+a
