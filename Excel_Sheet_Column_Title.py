def excel(n):
    r=''
    while n>0:
        rem=(n-1)%26
        r=chr(65+rem)+r
        n=(n-1)//26
    return r
n=int(input())
excel_column=excel(n)
print(excel_column)