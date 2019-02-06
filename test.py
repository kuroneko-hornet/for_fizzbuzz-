def main():
    a = []
    num_array = []
    words = []
    flag = True
    while True:
        x = input()
        if x.isnumeric():
            key = int(x)
            break
        a.append(x)
    a.sort()
    for i in range(len(a)):
        num,word=map(str,a[i].split(':'))
        num_array.append(int(num))
        words.append(word)
    #print(num_array,words)
    for i in range(len(a)):
        if (key % num_array[i]) == 0:
            print(words[i],end='')
            flag = False
    if flag:
        print(key,end='')
    print()

if __name__ == '__main__':
    main()
