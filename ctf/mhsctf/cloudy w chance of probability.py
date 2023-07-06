from sys import stdin, stdout
import math
def main():
    inputt = stdin
    out = stdout
    counter = 0
    numbers = ''
    for i in inputt:
        if numbers == '':
            numbers = int(i)
        else:
            j = i.split(' ')
            out.write(str(calc_p(j))+"\n")
            counter += 1
            if counter == numbers:
                break
def calc_p(a):
    p=1
    for i in range(len(a)):
        a[i] = float(a[i])*0.01
    for i in a:
        p*=(1-i)
    return(int(math.floor((1-p)*100)))
main()
