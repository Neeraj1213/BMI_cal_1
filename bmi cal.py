name= input('What is your name?')
import time
weight= float(input('What is your weight? (in kgs)'))
height= float(input ('What is your height? (in metres)'))
BMI= weight / (height ** 2)
print('Ok, thank you for the information. Now I will calulate your BMI.')
time.sleep(3)
print('Done!')
time.sleep(1)
print('Do you wanna know?')
answer= input('yes/no: ')
if answer=='yes':
    print( "your BMI is",BMI,"!" )
else:
    print('Ok')
print('This means..')
time.sleep(2)
print('you are....')
if BMI<25:
    print('You are underweight.')
elif 25<= BMI>= 30:
    print('You are healthy. Good Job!')
else:
    print('Your are overweight.')