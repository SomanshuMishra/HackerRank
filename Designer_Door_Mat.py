# Enter your code here. Read input from STDIN. Print output to STDOUT
n = list(input().split(' '))
row= int(n[0])
col = int(n[1])
row1=True
spl_chr = '.|.'
spl_chr_num = 1
dash = '-'
num = 1

for r in range(1,(int((row-1)/2)+1)):
    dash_num = int(col-(spl_chr_num*3))
    print((dash)*int((dash_num)/2),end='')
    for spl in range(spl_chr_num):
        print(spl_chr,end='')
    spl_chr_num+=2
    print((dash)*int((dash_num)/2))
    
print((dash)* int((col-7)/2),end='')
print('WELCOME',end='')
print((dash)* int((col-7)/2))

spl_chr_num-=2
for r in range(1,(int((row-1)/2)+1)):
    dash_num = int(col-(spl_chr_num*3))
    print((dash)*int((dash_num)/2),end='')
    for spl in range(spl_chr_num):
        print(spl_chr,end='')
    spl_chr_num-=2
    print((dash)*int((dash_num)/2))