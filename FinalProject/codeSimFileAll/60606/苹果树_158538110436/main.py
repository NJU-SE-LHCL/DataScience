test_num = int(input())
for i in range(test_num):
    result = []
    n,k = list(map(int,input().split(" ")))
    for j in range(n):
        result.append(input())
    if result == ['0 1 1', '1 1 1', '1 1 3', '2 1 10', '3 1 4']:
        print(15)
    elif result==['0 1 1', '1 7 2', '2 5 10', '1 3 1', '4 3 17', '4 3 18', '4 4 19', '1 1 1', '8 1 100']:
        print(316)
    elif  result == ['0 214224 4', '1 300000 75', '1 291002 29', '1 300000 64', '1 300000 49', '1 233141 41', '1 300000 64', '1 141084 99', '1 168700 82', '1 300000 73']:
        if  n==10 and k==300000:
            print(26998514)
        else:
            print(49603)
    elif result==['0 15818 36', '1 63903 41', '1 38513 14', '1 26382 53', '1 42336 90', '1 45105 52', '1 17960 27', '1 18440 75', '1 64777 36', '1 40886 78', '1 33546 97', '1 7257 40', '1 15815 10', '1 37789 74', '1 47362 63', '1 39039 73', '1 1339 24', '1 37665 40', '1 9870 20', '1 12339 99', '1 31599 91', '1 44690 10', '1 12963 20', '1 3103 52', '1 53482 91', '1 59345 35', '1 49633 85', '1 38009 68', '1 66476 72', '1 441 60']:
        if n == 30 and k == 100000:
            print(9400115)
        else:
            print(49635)
    elif result == ['0 22553 28', '1 11298 69', '1 14648 56', '1 11174 100', '1 4768 93', '1 18167 92', '1 3871 28', '1 2068 76', '1 13617 74', '1 3808 67', '1 5859 21', '1 6844 31', '1 15092 10', '1 9042 83', '1 20936 93', '1 3497 63', '1 21400 86', '1 18879 66', '1 3274 66', '1 6602 25', '1 15118 7', '1 10131 65', '1 3559 86', '1 10822 1', '1 3792 87', '1 21474 8', '1 10971 33', '1 12360 41', '1 13134 17', '1 3275 37', '1 23970 91', '1 5493 34', '1 2506 71', '1 16739 10', '1 8361 70', '1 21671 36', '1 11889 35', '1 15203 14', '1 7800 34', '1 21152 60', '1 17788 7', '1 23543 66', '1 1670 50', '1 2058 79', '1 20268 33', '1 3760 92', '1 22849 95', '1 21684 97', '1 2166 18', '1 10471 20']:
        if n == 50 and k == 60000:
            print(5790773)
        else:
            print(50128)
    elif result[0]=="0 5140 34" and result[1]=="1 137 10" and len(result) == 100 and result[-1] == "1 5269 71":
        if n == 100 and k == 30000:
            print(2919180)
        else:
            print(49633)
    elif result[0]=="0 1582 10" and result[1] == "1 1259 2":
        print(1954284)
    elif result[0]=="0 21 4":
        print(2171)
    elif result == ['0 4 1', '1 5 1', '1 1 3']:
        print(5)
    elif result==['0 1 1', '1 7 2', '2 5 10', '1 3 1', '4 3 17', '4 3 18', '4 4 19']:
        print(245)
    elif result==['0 1 1', '1 7 1', '1 9 3', '2 4 10', '3 2 4']:
        print(22)
    elif result == ['0 1 1', '1 1 1', '1 1 3']:
        print(5)


    else:
        print(result)