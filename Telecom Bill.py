import datetime
ata=int(input("Enter the number of calls ATA: "))
ato=int(input("Enter the number of calls ATO Local: "))
ator=int(input("Enter the number of calls ATO Roaming: "))
isd=int(input("Enter the number of calls ISD: "))

bill1 = 0
if ata>1 and ata<=50:
    bill1=0
elif ata>50 and ata<=200:
    bill1+=(ata-50)*0.50
elif ata>200 and ata<=500:
    bill1+=(ata-200)*1.5 + 0.50 * 150
elif ata>500:
    bill1+=(ata-500)*2 + 1.5* 300 + 0.50 * 150
else:
    print("Wrong Calls input")
#print("the total amount to be paid ATA:", bill1)

#bill2 = 0
if ato>1 and ato<=200:
    bill1+= ato*0.7
elif ato>200 and ato<=500:
    bill1+= 200*0.7 + 1.5*(ato-200)
elif ato>500:
    bill1+=200*0.7 + 1.5*300 + 2.5*(ato-500)
else:
    print("Wrong calls input")
#print("the total amount to be paid ATO:", bill2)

#bill3=0
if ator>1 and ator<=200:
    bill1+=ator*1.5
elif ator>200 and ator<=500:
    bill1+=200*1.5 + 3.5*(ator-200)
elif ator>500:
    bill1+=200*1.5 + 3.5*300 + 5*(ator-500)
else:
    print("Wrong Minutes")
#print("the total amount to be paid ATOR:", bill3)

#bill4=0
bill1+=isd*7.5
#print("The amount to be paid ISD:", bill4)

#tbill = bill1+bill2+bill3+bill4
print("The total amount of bill's:", bill1)

if bill1>100 and bill1<=500:
    bill1+=bill1*2/100
elif bill1>500 and bill1<=1200:
    bill1+=bill1*5/100
elif bill1>1200 and bill1<=2000:
    bill1+=bill1*7/100
elif bill1>2000:
    bill1+=bill1*10/100

print("The total amount to be paid with tax: ", bill1)
print("The total amount to be paid with GST:", bill1+bill1*18/100)
print("The bill generation date is : ", datetime.datetime.today())
print("Last date to pay bill:", datetime.date.today()+datetime.timedelta(10))
print("Amount to be paid after due date:", bill1+bill1*18/100+bill1*10/100)
