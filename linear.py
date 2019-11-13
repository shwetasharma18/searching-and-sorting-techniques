def linear(num,num_list):
   i = 0
   while i < len(num_list):
        if num_list[i] == num:
           return "found at" , i
        elif num not in num_list:
            return "not found"
        else:
            i = i + 1

num_list = [12,4,6,5,2,9,16,7,23]

num = int(raw_input("enter your input :- "))

print linear(num,num_list)