if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(n):
        match e:
            e = input().split(' ').strip('insert')

            case 'insert' in e:
                while True:
                    try:
                        e = e.strip('insert ')
                        command = list(map(int, e))
                        arr.insert(command[0], command[1])
                        break
                    except ValueError:
                        print("Please try again.")
            case 'append' in e:
                while True:
                    try:
                        e = e.strip('append ')
                        command = list(map(int, e))
                        arr.append(command[0])
                        break
                    except ValueError:
                        print("Please try again.")
            case 'remove' in e:
                while True:
                    try:
                        e = e.strip('remove ')
                        command = list(map(int, e))
                        arr.remove(command[0])
                        break
                    except ValueError:
                        print("Please try again.")
            case 'sort' in e:
                arr.sort()
                        
            case ' print' in e:
                print(arr)
            case 'pop' in e:
                arr.pop()
                        
            case 'reverse' in e:
                reversed_arr = []
                for i in range(len(arr)):
                    reversed_arr.append(arr[::-1])
       
        command = list(map(int, e))
        
