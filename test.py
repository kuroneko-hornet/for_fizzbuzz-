import copy as cp

def main():
    a = []
    num_array = []
    words = []
    flag = True
    for line in open('input.txt', 'r'):
        x = cp.copy(line.replace('\n',''))
        if x.isnumeric():
            key = int(x)
            break
        a.append(x)
    for i in range(len(a)):
        num,word=map(str,a[i].split(':'))
        num_array.append(int(num))
        words.append(word)
    for _ in range(len(a)):
        for i in range(len(a)-1):
            if(num_array[i]>num_array[i+1]):
                num_array[i],num_array[i+1] = num_array[i+1],num_array[i]
                tmp = cp.copy(words[i])
                words[i] = cp.copy(words[i+1])
                words[i+1] = cp.copy(tmp)
    print(num_array,words)
    for i in range(len(a)):
        if (key % num_array[i]) == 0:
            print(words[i],end='')
            flag = False
    if flag:
        print(key,end='')
    print()

if __name__ == '__main__':
    main()
