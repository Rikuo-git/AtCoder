#my solution
count = {"2":"hon","4":"hon","5":"hon","7":"hon","9":"hon","0":"pon","6":"pon","1":"pon","8":"pon","3":"bon",}
print(count[input()[-1]])


#shortest by prd_xxx
print('pphbhhphph'[int(input())%10]+'on')

#fastest by JohnU
n=input()
n=n[::-1]
if (n[0]=="3"):
    print("bon")
elif (n[0]=="0" or n[0]=="1" or n[0]=="6" or n[0]=="8"):
    print("pon")
else:
    print("hon")