#تابعی بنویسید که حاصل تقسیم صحیح a بر b را به صورت بازگشتی محاسبه کند.
def div (a, b):
    if a<b:
        return 0
    return div (a-b, b)+1