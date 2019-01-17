def add_123(input_number):
    total_check=0
    if input_number==0:
        return 1

    if input_number<0:
        return 0

    if input_number>0:
        total_check+=add_123(input_number-1)
        total_check+=add_123(input_number-2)
        total_check+=add_123(input_number-3)

    return total_check


case_number = int(input())
for i in range(case_number):
    input_number = int(input())
    print(add_123(input_number))
