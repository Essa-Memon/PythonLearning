print("***WelCome to Python Development***\n")
name = input('Enter your Name: ')
qualification = input('Enter your Qualification: ')
experience = input('Enter your experience: ')
company = input('Enter your Company: ')
salary = input('Enter your Salary: ')
pfPercent = input('Enter your PF Percent Deduction: ')
pfAmount = int(salary)/100*int(pfPercent)
netSalary = int(salary)-int(pfAmount)


print('\n ***Personal Information*** \n Name :', name.title(), '\n Qualification :', qualification, '\n Experience :', experience, '\n Company :', company, '\n Salary :', salary, '\n PF Amount :', pfAmount, '\n Salary After 6% PF deduction :', netSalary)

print('\n ***Education Marks Calculator*** \n')
ssc = input('Enter your SSC Marks: ')
hsc = input('Enter your HSC Marks: ')
entryTest = input('Enter your Entry Test Marks: ')
sscPercent = int(ssc)/650*100
hescPercent = int(hsc)/1100*100
sscWeightage = int(sscPercent)/100*20
hscWeightage = int(hescPercent)/100*30
entryTestpercent = int(entryTest)/100*50
TotalPercent = int(sscWeightage)+int(hscWeightage)+int(entryTestpercent)
print('Result', TotalPercent, '%')
#z= int(x)-int(y)*int(c)
#print(z)


