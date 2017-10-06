if __name__ == '__main__':
    N = int(raw_input())
    lst = []
    result = []
    
    for i in range(N):
        lst.append(raw_input())
    
    for j in range(N):
        command = lst[j].split()
        command = command[0]
        
        if command == 'insert':
            result.insert(int(command[1]), int(command[2])
        elif command == 'remove':
            result.remove(int(command[1])
        elif command == 'append':
            result.append(int(command[1]))
        elif command == 'sort':
            result.sort()
        elif command == 'pop':
            result.pop()
        elif command == 'reverse':
            result.reverse()
        elif command == 'print':
            print result
