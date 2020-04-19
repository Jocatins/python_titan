prizes = [20, 30,40, 1000]

double_prizes = []
for prize in prizes:
    double_prizes.append(prize // 2)
print(double_prizes)


# comprehension method
double_prizes = [prize*2 for prize in prizes]
print(double_prizes)

# squaring numbers
nums = [1,2,3,4,5,6,7,8,7]

squared_nums = []
for num in nums:
    if (num ** 2) %2 == 0:
        squared_nums.append(num ** 2)
print(squared_nums)

# comprehension method
nums = [1,2,3,4,5,6,7,8]
squared_nums  = [num **2 for num in nums if(num **2)% 2 ==0 ]
print(squared_nums)
