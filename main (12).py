kilometers=float(input('How many kilometers?:'))
conv_fac=0.621371
miles=kilometers*conv_fac
print('%0.3f kilometers is equal to %0.3f miles' %(kilometers,miles))


celsius=float(input('Enter temperature in Celsius: '))
fahrenheit=(celsius * 1.8)+32
print('%0.1f Celsius is equal to %0.1f degree Fahrenheit'%(celsius, fahrenheit))

feet=float(input('Enter measurement in feet: '))
meters=feet*0.3048
print('%0.1f feet is equal to %0.1f meters'%(feet, meters))

milliliters=float(input('Enter amount in milliliters: '))
gallons=milliliters*0.00026417
print('%0.1f milliliters is equal to %0.1f gallons'%(milliliters,gallons))

acres=float(input('Enter amount in acres: '))
feet=acres*43560
print('%0.1f acres is equal to %0.1f feet'%(acres,feet))