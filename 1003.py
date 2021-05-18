a = int(input())

case0 = [0 for _ in range(41)]
case1 = [0 for _ in range(41)]

case0[0] = 1
case1[1] = 1

for i in range(2, 41):
    case0[i] = case0[i-1]+case0[i-2]
    case1[i] = case1[i-1]+case1[i-2]
    

for i in range(a):
    n = int(input())
    print(f'{case0[n]} {case1[n]}')

    
    
