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

cubicFeet=float(input('Enter amount in cubic feet: '))
liters=cubicFeet*28.316
print('%0.1f liters is equal to %0.1f feet'%(cubicFeet,liters)

lightYear=float(input('Enter amount in light years: '))
feet2=lightYear*9460000000000000
print('%0.1f light years is equal to %0.1f feet'%(lightYear,feet2)

pounds=float(input('Enter amount in pounds: '))
kilograms=pounds*2.20462262
print('%0.1f pounds is equal to %0.1f kilograms'%(kilograms, pounds)
