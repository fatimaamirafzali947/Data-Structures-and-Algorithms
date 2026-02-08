#متدی به کلاس پشته اضافه کنید که تمامی اعداد زوج درون پشته را در خروجی نمایش دهد
def even (self):
    for i in range (len(self.st)):
        if self.st [i]%2==0:
            print(self.st[i])