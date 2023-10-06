import random
import csv
import datetime
from random import randint
from datetime import date
import os

print()
#getting current date and time
def todaydate():
    global day,time,today,today1,today11
    day=date.today()
    today=day.year
    today1=day.month
    today11=day.day
    time=datetime.datetime.now()
todaydate()


#project heading
def start():
    if int(time.strftime("%H"))>11 :
        x='P.M.'
    else:
        x='A.M.'
    print()
    print(day.strftime("%d/%m/%Y"),f'{"--PROJECT HOTEL RESERVATION--":^58s}',time.strftime("%H:%M"),x)
    print('-'*80)
    print(f'{"WELCOME TO INTERNATIONAL INN":^80s}')
    print('-'*80)
start()


def space():
    print()
    print('═'*80)
    print()


#validation for booking records

#name validation
def nameinput():
    global name
    name=input("Customer name          : ").strip()
    x=name.split()
    if len(name)>0:
        for i in range(len(x)):
            if x[i].isalpha():pass
            else:
                print("ENTER PROPER NAME...\n")
                nameinput()
        
            
    else:
        print("enter a name..retry\n")
        nameinput()
        

#address validation
def addressinput():
    global address
    address=input("Customer Address       : ").strip()
    if len(address)>0:
        return address
    else:
        print("enter an address..\n")
        addressinput()


#number validation(̶̿╔╚╝╗═)
def mobilenumber():
    global mobile 
    mobile = input('Customer mobile number : ').strip()
    if len(mobile)>0:
        if mobile.isdigit():
            if len(mobile)!=8:
                print("number not equal to 8 digits ...retry\n")
                mobilenumber()
            else:
                return mobile
        else:
            print("ENTER A MOBILE NUMBER...\n")
            mobilenumber()
    else:
        print("please enter a mobile number...\n")
        mobilenumber()


#email validation
def emailaddress():
    global email
    email=input("Customer Email         : ").strip()
    if len(email)>0:
        if '@' in email:
            if '.com' in email:
                return email
            else:
                print("Enter a proper email...\n")
                emailaddress()
        else:
            print("Enter a proper email...\n")
            emailaddress()
    else:
        print("Enter an email..\n")
        emailaddress()


#roomtype validation
def chkroomtype():
    global roomtype
    roomtype=input("Enter choice of room : ").strip()
    if len(roomtype)==1:
        if roomtype.isdigit():
            if roomtype not in '123456':
                print("ENTER DIGIT IN RANGE 1-6\n")
                chkroomtype()
            else:
                return roomtype
        else:
            print("ENTER A DIGIT....\n")
            chkroomtype()
    else:
        print("ENTER A SINGLE DIGIT ONLY...\n")
        chkroomtype()


#choosing room type
def chooseroomtype():
    print()
    print('-'*80,'\n')
    print("\t\t     ǁ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ǁ")
    print("\t\t     ǁ ==> List of room types available    ǁ")   
    print("\t\t     ǁ                                     ǁ")
    print("\t\t     ǁ  1-->  Single DX  (1200Rs/night)    ǁ")
    print("\t\t     ǁ  2-->  Double DX  (1700Rs/night)    ǁ")
    print("\t\t     ǁ  3-->  Single AC  (1300Rs/night)    ǁ")
    print("\t\t     ǁ  4-->  Double AC  (1000Rs/night)    ǁ")
    print("\t\t     ǁ  5-->  Single NAC (600Rs/night)     ǁ")
    print("\t\t     ǁ  6-->  Double NAC (850Rs/night)     ǁ")
    print("\t\t      ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿\n")
    print()
    chkroomtype()
    global roomtype,charges
    if int(roomtype)==1:
        roomtype,charges="Single DX",1200
    elif int(roomtype)==2:
        roomtype,charges ="Double DX",1700
    elif int(roomtype)==3:
        roomtype,charges = "Single AC",1000
    elif int(roomtype)==4:
        roomtype,charges = "Double AC",1300
    elif int(roomtype)==5:
        roomtype,charges = "Single NAC",600
    elif int(roomtype)==6:
        roomtype,charges = "Double NAC",850


#random room
def randroomnumber():
    global roomnumber
    emplist=[]
    for x in range(1,101):
        emplist+=[x]
    try:
        fobj=open("hotelr.csv",'rt')
        crobj=csv.reader(fobj)
        for rec in crobj:
            emplist.remove(int(rec[9]))
        fobj.close()
    except:pass
    roomnumber=random.choice(emplist)
    return roomnumber   


def chkindate():
    global checkindate,d1,m1,y1
    isValidDate = True
    print()
    try:
        checkindate = input('Enter customer check in  date (dd/mm/yy format)  : ').strip()
        d1,m1,y1 = checkindate.split('/')
        if int(y1)>2030 or int(y1)<today:
            print("entered year is out of range...retry\n")
            chkindate()
    except:
        print("Enter a proper date...\n")
        chkindate()
    if int(y1)==today:
         if int(m1)<today1:
             print("entered month is out of range...retry\n")
             chkindate()
         elif int(m1)==today1:
             if int(d1)<today11:
                 print("date entered is not valid\n")
                 chkindate()
    try:
        datetime.datetime(eval(y1),eval(m1),eval(d1))
    except ValueError:
        isValidDate = False
    if(isValidDate):
        return checkindate
    else :
        print("Inputted date is not valid...retry\n")
        chkindate()


def chkoutdate():
    global checkoutdate,d2,m2,y2
    isValidDate=True
    try:
        checkoutdate = input('Enter customer check out date (dd/mm/yy format)  : ').strip()
        d2,m2,y2 = checkoutdate.split('/')
        if 2030<int(y2) or int(y2)<today :
            print("entered year is out of range...retry\n")
            chkoutdate()
    except:
        print("Enter a proper date..\n")
        chkoutdate()
    if int(y2)==today:
         if int(m2)<today1:
            print("entered month is out of range for current year...retry\n")
            chkoutdate()
         elif int(m2)==today1:
             if int(d2)<today11:
                 print("date entered not valid\n")
                 chkoutdate()
    try:
        datetime.datetime(eval(y2),eval(m2),eval(d2))
    except ValueError:
        isValidDate = False
    if(isValidDate):pass
    else :
        print("Inputted date is not valid...retry\n")
        chkoutdate()
    daysstayed()


def daysstayed():
    global daysstay
    dx1,mx1,yx1 = eval(d1),eval(m1),eval(y1)
    dx2,mx2,yx2 = eval(d2),eval(m2),eval(y2)
    date1 = date(yx1,mx1,dx1)
    date2 = date(yx2,mx2,dx2)
    delta = date2 - date1
    daysstay = delta.days
    if yx2>yx1:
        return daysstay
    elif yx2==yx1 and mx2>mx1:
        return daysstay
    elif yx2==yx1 and mx2==mx1 and dx2>dx1:
        return daysstay
    elif yx2==yx1 and mx2==mx1 and dx2==dx1:
        print("Check in date cannot be same as checkout date....")
        print("ENTER CHECKOUT DATE AGAIN...\n")
        chkoutdate()
    else:
        print("check in date has to be before checkout date....")
        print("ENTER CHECKOUT DATE AGAIN...\n")
        chkoutdate()



def updatecharges():
    global charges
    charges=charges*int(daysstay)


def bookingprint():
    print()
    print()
    print(f'{"Welcome to International Inn,Simla":^80s}')
    print('-'*90)
    print(f'{"Name":20s}:{name:<15s}\t\t\t{"ADDRESS":12s}\t:{address:19s}')
    print(f'{"email":20s}:{email:<20s}\t\t{"Mobile":12s}\t:{mobile:<11s}')
    print(f'{"Type of room":20s}:{roomtype:<15s}\t\t\t{"Room number":12s}\t:{roomnumber:<4n}')
    print(f'{"check in date":20s}:{checkindate:<10s}\t\t\t\t{"check out date":<15s}\t:{checkoutdate:<10s}')
    print(f'{"no of days of stay":20s}:{daysstay:4n}')
    print('-'*90)


def addtofile():
    fobj=open('hotelr.CSV','a',newline='')
    cwobj=csv.writer(fobj)
    emp=[name.upper(),address,mobile,email,checkindate,checkoutdate,daysstay,roomtype,charges,roomnumber]
    cwobj.writerow(emp)
    fobj.close()

               
def booking():
    print(f'{"BOOKING PROCESS":^80s}\n')
    print("═"*80,'\n')
    print()
    nameinput()
    addressinput()
    mobilenumber()
    emailaddress()
    chooseroomtype()
    randroomnumber()
    print("Customer room number -->",roomnumber)
    chkindate()
    chkoutdate()
    daysstayed()
    updatecharges()
    bookingprint()
    addtofile()


def roominput():
    global room1
    room1=input("Customer room number   : ").strip()
    if room1.isdigit():
        if int(room1)>100:
            print("Entered room number does not exist..retry\n")
            roominput()
        else:return room1
    else:
        print("Enter a digit..\n")
        roominput()


def chktoretry():
    global xcheck
    xcheck=input("[Y] to delete [X] to cancel : ")
    return xcheck
    

def cancellation():
    print()
    nameinput()
    roominput()
    global name
    fobj=open("hotelr.csv")
    fobj1=open("TEMP.csv",'w',newline='')
    crobj=csv.reader(fobj)
    cwobj=csv.writer(fobj1)
    emplist,found,a=[],0,0
    #try:
    for rec in crobj:
            if a==0:
                if name.upper()==rec[0].upper() and room1==rec[9]:
                    print()
                    print("-->customer records found")
                    print(f'{"--Customer details--":^90s}')
                    print()
                    print(f'\t{"Name":20s}:{rec[0]:<15s}\t\t{"ADDRESS":12s}\t:{rec[1]:19s}')
                    print(f'\t{"email":20s}:{rec[3]:<20s}\t{"Mobile":12s}\t:{rec[2]:<11s}')
                    print(f'\t{"Type of room":20s}:{rec[7]:<15s}\t\t{"Room number":12s}\t:{rec[9]:<4s}')
                    print(f'\t{"check in date":20s}:{rec[4]:<10s}\t\t\t{"check out date":<15s}\t:{rec[5]:<10s}')
                    print(f'\t{"no of days of stay":20s}:{rec[6]:^4s}\n')
                    chktoretry()
                    print()
                    if xcheck in 'yY[Y][y]':
                        found=a=1
                        print()
                    elif xcheck in 'Xx[X][x]':
                        found,a=2,1
                        print()
                    else:
                        print("Invalid input entered retry..")
                        print('-'*80)
                        cancellation()
                else:cwobj.writerow(rec)
            else:cwobj.writerow(rec)
    fobj.close()
    fobj1.close()
    if found==1:
      os.remove("hotelr.csv")
      os.rename("TEMP.csv","hotelr.csv")
      print("-->Customer records deleted")
      print("-->Hotel records updated\n")
    elif found==2:pass
    elif found==0:
        print()
        print("-->Record not found\n")
        x=input('[X] to exit [R] to re-enter name : ')                   
        print('\n')            
        if x in 'Rr[r][R]':
            print("-"*80)
            cancellation()
        elif x in 'Xx[X][x]':pass
        else:
            print("Invalid input entered ...\n")
            pass
    

def chkinputadding():
    global n
    try:
        n=int(input("Enter number of records to be inputted : "))
        if n>5:
            print("Enter value less than 5...\n")
            chkinputadding()
    except:
        print("Enter a digit less than 5...\n")
        chkinputadding()
    return n


def addingrecords():
    chkinputadding()
    for x in range(n):
        print()
        print("-->Enter record",x+1)
        print()
        nameinput()
        addressinput()
        mobilenumber()
        emailaddress()
        chooseroomtype()
        randroomnumber()
        print("Customer room number -->",roomnumber)
        chkindate()
        chkoutdate()
        daysstayed()
        updatecharges()
        addtofile()
        print("RECORD ADDED...")
        print()


def deleteallrecords():#2d(ii)
    fobj = open("hotelr.csv",'w',newline='')
    fobj.close()
    print("all records deleted")


#validation for edit particular rec
def chkeditparticular():
    global ch
    ch=input('Choose option  : ')
    if len(ch)==1:
        if ch in '123':pass
        else:
            print('ENTER DIGIT IN RANGE(1-3)...\n')
            chkeditparticular()
    else:
        print("Enter a single digit...\n")
        chkeditparticular()


#edit particular rec
def editparticular():                                           #problem : choosing new room type if u choose the same theres an error 
    global room1
    roominput()
    fobj=open('hotelr.CSV','rt')
    gobj=open('TEMP.CSV','wt',newline='')
    crobj=csv.reader(fobj)
    cwobj=csv.writer(gobj)
    found=0
    #try:
    for rec in crobj:
        if rec[9]==room1:
            print()
            print('-'*80)
            print("-->RECORD FOUND")
            found=1
            print("\t\t     ǁ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ǁ")
            print("\t\t     ǁ ==> Options to edit customer record ǁ")
            print("\t\t     ǁ                                     ǁ Customer Name     -->",rec[0].upper())
            print("\t\t     ǁ     1-->  TO CHANGE MOBILE NO.      ǁ Current mobile no.-->",rec[2])
            print("\t\t     ǁ     2-->  TO CHANGE ROOM TYPE       ǁ Current room type -->",rec[7])
            print("\t\t     ǁ     3-->  TO CHANGE ROOM NUMBER     ǁ Current room no.  -->",rec[9])
            print("\t\t      ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿")
            print()
            global ch
            chkeditparticular()
            print()
            if ch=='1':
                print("Enter new number...")
                mobilenumber()
                rec[2]=mobile
            if ch=='2':
                chooseroomtype()
                rec[7]=roomtype
                rec[8]=charges*int(rec[6])
                print("New room type selected-->",rec[7])
            if ch=='3':
                randroomnumber()
                rec[9]=roomnumber
                print("New room number-->",rec[9])
        cwobj.writerow(rec)
    #except:print("ERROR...")
    fobj.close()
    gobj.close()
    if found==1:
        print('Record Updated!!')
        os.remove('hotelr.CSV')
        os.rename('TEMP.CSV','hotelr.CSV')
    else:
        print()
        print('Entered room number is not taken\n')
        x=input('[R] to retry [X] to quit : ')
        print()
        if x in 'rR[R][r]':
            print('-'*80,'\n')
            editparticular()
        elif x in 'xX[x][X]':
            pass
        else:
            print("Retry...\n")
            print('-'*80,'\n')
            editparticular()


#chk to see if service chrge already exists
def chkservicecharges():
    global astop
    try:
        fobj1=open("services.csv")
        crobj1=csv.reader(fobj1)
        for rec1 in crobj1:
            if rec1[13]==room1:
                astop=2
                fobj1.close()
                return astop
    except:pass
    astop=5


#chk if valid input was made in room service

#validation for washing services
def washingvalid():
    global washing
    washing=input('Input No. of times Laundary was used :').strip()
    if washing.isdigit():
        return washing
    else:
        print("Enter a digit...retry\n")
        washingvalid()


#validation for coftea services
def cofteavalid():
    global coftea
    coftea=input('Input No of Coffee and Teas ordered  :').strip()
    if coftea.isdigit():
        return coftea
    else:
        print("Enter a digit...retry\n")
        cofteavalid()


#validation for medical services
def medivalid():
    global medi
    medi=input('Input No of times Medical Aids used  :').strip()
    if medi.isdigit():
        return medi
    else:
        print("Enter a digit...\n")
        medivalid()


#validation for spa services
def spavalid():
    global spa
    spa=input('Input No of times Spa used :').strip()
    if spa.isdigit():
        return spa
    else:
        print("Enter a digit...\n")
        spavalid()


#validation for spa services
def spavalid():
    global spa
    spa=input('No of times Spa used :').strip()
    if spa.isdigit():
        return spa
    else:
        print("Enter a digit...\n")
        spavalid()


#validation for food services
def foodvalid():
    global food
    food=input('No of times Food served in the room / restaurant :').strip()
    if food.isdigit():
        return food
    else:
        print("Enter a digit...\n")
        foodvalid()


#validation for phone services
def phonevalid():
    global phone
    phone=input('Input Total no of telephone calls made :').strip()
    if phone.isdigit():
        return phone
    else:
        print("Enter a digit...\n")
        foodvalid()


#room service charges
def calcroomservices():
    print()
    global astop
    astop=1
    nameinput()
    roominput()
    chkservicecharges()
    fobj=open('services.csv','at',newline='')
    cwobj=csv.writer(fobj)
    gobj=open('hotelr.csv','rt')#13 14
    crobj=csv.reader(gobj)
    print()
    service,found=[],0
    for rec in crobj:
        if astop==2:
            print("Services charges for particular customer already exist")
            found=2
            break
        if rec[9]==room1:
            if rec[0].upper()==name.upper():
                print("-->RECORD FOUND\n")
                found=1
                washingvalid()
                cofteavalid()
                medivalid()
                spavalid()
                foodvalid()
                phonevalid()
                wc=int(washing)*50
                ctcharges=30*int(coftea)
                mc=int(medi)*100
                bc=200*int(spa)
                fc=200*int(food)
                pc=1*int(phone)
                tsc=wc+ctcharges+mc+bc+fc+pc
                service+=[washing,coftea,medi,spa,food,phone,tsc,wc,ctcharges,mc,bc,fc,pc,room1,name]
    if found==2:
        fobj.close()
        gobj.close()
        print()
        x=input('[B] to print bill [S] to print service charge bill [X] to quit :')
        print()
        if x in 'bB[B][b]':
            print('-'*80)
            print()
            customerbill()
        elif x in 'xX[x][X]':
            pass
        elif x in 'sS[S][s]':
            print()
            space()
            roomservicebill()
        else:
            print("Invalid input entered...\n")
            pass
    elif found==1:
        print("record updated\n")
        cwobj.writerow(service)
        fobj.close()
        gobj.close()
        x=input('[B] to print bill [S] to print service charge bill [X] to quit : ')
        print()
        if x in 'bB[B][b]':
            space()
            print(f'{"CUSTOMER BILL":^80s}\n')
            print('═'*80,'\n')
            customerbill()
        elif x in 'xX[x][X]':
            pass
        elif x in 'sS[S][s]':
            print()
            print('-'*80)
            roomservicebill()
        else:
            print("Invalid input entered...\n")
            pass
    elif str(found) not in '12':
        fobj.close()
        gobj.close()
        print('Entered room number and/or name does not match\n')
        x=input('[R] to retry [X] to quit : ')
        print()
        if x in 'rR[R][r]':
            print('-'*80)
            calcroomservices()
        elif x in 'xX[x][X]':
            pass
        else:
            print("Retry...\n")
            print('-'*80)    
            calcroomservices()

            
#display room number
def displayroomnumber():#3d
    print(f'{"DISPLAYING OCCUPIED ROOMS":^80s}\n')
    print('═'*80)
    print()
    fobj=open("hotelr.csv")
    crobj=csv.reader(fobj)
    c=1
    try:
        for rec in crobj:
            print()
            print(c,"==>""\tRoom number :",rec[9],"\t\t\t\t      Status : OCCUPIED\n")
            print(f'{"--Customer details--":^90s}')
            print()
            print(f'\t{"Name":20s}:{rec[0]:<15s}\t     {"ADDRESS":12s}     :{rec[1]:19s}')
            print(f'\t{"email":20s}:{rec[3]:<20s}    {"Mobile":12s}     :{rec[2]:<11s}')
            print(f'\t{"Type of room":20s}:{rec[7]:<15s}\t     {"Room number":12s}     :{rec[9]:<4s}')
            print(f'\t{"check in date":20s}:{rec[4]:<10s}\t\t     {"check out date":<15s}  :{rec[5]:<10s}')
            print(f'\t{"days of stay":20s}:{rec[6]:^4s}\n')
            c+=1
            print('-'*80,'\n')
        if c==1:print("No rooms are currently occupied")
    except:print("no records found...\n")
    fobj.close()
    space()


# menu for editing records    
def updationdeletion():#2d
    print(f'{"EDITING MENU":^80s}\n')
    print()
    print("\t\t     ╔═════════════════════════════════════╗")
    print("\t\t     ║                                     ║")
    print("\t\t     ║  ==> Options to edit hotel records  ║")
    print("\t\t     ║                                     ║")
    print("\t\t     ║     1-->  ADD A RECORD              ║")
    print("\t\t     ║     2-->  DELETE ALL RECORDS        ║")
    print("\t\t     ║     3-->  DELETE PARTICULAR RECORD  ║")
    print("\t\t     ║     4-->  EDIT CUSTOMER RECORDS     ║")
    print("\t\t     ║     5-->  GO BACK TO MENU           ║")
    print("\t\t     ╚═════════════════════════════════════╝\n")
    ch=input("==> Choose option  : ").strip()
    if ch=='1':
        space()
        print(f'{"ADDING RECORD":^80s}')
        space()
        addingrecords()
        space()
    elif ch=='2':
        space()
        print(f'{"DELETING ALL RECORDS":^80s}\n')
        deleteallrecords()
        space()
    elif ch=='3':
        space()
        print(f'{"DELETING PARTICLUAR RECORD":^80s}\n')
        cancellation()
        space()
    elif ch=='4':
        space()
        print(f'{"EDITING PARTICLUAR RECORD":^80s}\n')
        print('═'*80,'\n')
        editparticular()
        space()
    elif ch=='5':
        space()
        pass
    elif len(ch)!=1:
        print("Enter a digit...\n")
        space()
        updationdeletion()
    else:
        if len(ch)>1:
            print("Enter a single digit only...\n")
            space()
            updationdeletion()
        else:
            print("enter a digit in range[1-5]...\n")
            print("\t\t\t\t1--> Restart\n\t\t\t\t2--> Go back to menu")
            print()
            ch=input("Choose option :")
            if ch=='1':
                space()
                updationdeletion()
            elif ch=='2':
                space()
                pass
            elif ch!='1' and ch!='2':
                print("invalid input...retry\n")
                space()
                updationdeletion()


#valid chk input for service bill
def validservicebill():
    global xchk
    xchk=input('[E] to enter service charges [X] to quit : ')
    if len(xchk)==1:
        if xchk not in 'eE[E][e]xX[x][X]':
            print("Invalid input entered...retry\n")
            validservicebill()
        else:return xchk
    else:
        print("Invalid input entered...retry\n")
        validservicebill()


#detailed service charge report
def roomservicebill():
    print()
    found=0
    global astop,name,room1
    nameinput()
    roominput()
    chkservicecharges()
    fobj=open('hotelr.csv','rt')
    crobj=csv.reader(fobj)
    gobj=open('services.csv','rt')
    crobj1=csv.reader(gobj)
    for rec in crobj:
        if room1==rec[9] and name.upper()==rec[0].upper():
            found=0
            if astop==2:
                for services in crobj1:
                    if services[13]==room1:
                        print('-'*80)
                        print('\tNo of times Laundary was used:',services[0])
                        print('\tNo of Coffee and Teas ordered:',services[1])
                        print('\tNo of times Medical Aids used:',services[2])
                        print('\tNo of times Spa used:',services[3])
                        print('\tNo of times Food served in the room / restaurant:',services[4])
                        print('\tTotal no of telephone calls:',services[5])
                        print('\tTotal Washing Charges= Rs',services[7])
                        print('\tTotal Tea Coffee charges= Rs',services[8])
                        print('\tTotal Charges for Medical aids= Rs',services[9])
                        print('\tTotal Charges of Beautician(SPA)= Rs',services[10])
                        print('\tTotal Food Charges= Rs',services[11])
                        print('\tTotal Telephone Call Charges= Rs',services[12])
                        print()
                        print('\tTOTAL SERVICE CHARGE BILL: Rs',services[6])
                        print('\n')
                        print('-'*80)
                        print()
                        found=1
                        
            else:
                found=3
                break
    fobj.close()
    gobj.close()
    if found==1:
        x=input('[B] to print bill [X] to quit :')
        print()
        if x in 'bB[B][b]':
            space()
            customerbill()
        elif x in 'xX[x][X]':
            pass
        else:
            print("INVALID INPUT...")
            pass
    elif found==3:
        print()
        print("Service charges do not exist for customer")
        print("Input service charges first..\n")
        validservicebill()
        print()
        if xchk in 'eE[E][e]':
            space()
            calcroomservices()
        elif xchk in 'xX[x][X]':
            pass
        else:
            print("INVALID INPUT... Retry")
            validservicebill()
    else:
        print()
        print("Entered record does not exist in hotel...\n")
        y=input("[R] to re-enter name [X] to quit : ")
        if y in 'rR[r][R]':
            print()
            print('-'*80)
            roomservicebill()
        elif y in 'xX[x][X]':
            pass
        else:
            print("INVALID INPUT...")
            pass

        
#checking validation of amount in words
def wordamount():
    global words
    words=input('Input Total Amount in words').strip()
    x=words.split()
    if len(x)>0:
        for i in range(len(x)):
            if x[i].isalpha():pass
            else:
                print("ENTER PROPER AMOUNT...\n")
                wordamount()       
    else:
        print("enter amount..retry\n")
        wordamount()


#Customer bill printing
def customerbill():
    nameinput()
    roominput()
    chkservicecharges()
    aobj=open('HOTELDATA.CSV','at',newline='')
    cwobj2=csv.writer(aobj)
    mobj=open('TEMP.CSV','w',newline='')
    cwobj=csv.writer(mobj)
    lobj=open("TEMP1.CSV",'w',newline='')
    cwobj1=csv.writer(lobj)
    fobj=open('hotelr.csv','rt')
    crobj=csv.reader(fobj)
    gobj=open('services.csv','rt')
    crobj1=csv.reader(gobj)
    found=0
    for rec in crobj:
        if rec[9]==room1 and rec[0].upper()==name.upper():
            if astop==2:
                for record in crobj1:
                    if record[13]==room1:
                        found=1
                        z=int(rec[8])
                        sercharge=float(record[6])
                        a=0.15*(int(rec[8])+sercharge)
                        total=z+a+sercharge
                        cwobj2.writerow(rec)
                        print()
                        print('Total amount= Rs.',total)
                        wordamount()
                        print()
                        print('-'*80)
                        billno=randint(100000,900000)
                        print()
                        print(f'{"FINAL BILL":^76s}\n')
                        print('-'*80)
                        print(f'{"Name":16s}:{rec[0]:<15s}\t{"Room No":16s}:{int(rec[9]):<3n}\t{"Bill No":7s}:{billno:<8n}')
                        print(f'{"Check in date":16s}:{rec[4]:<15s}\t{"Check out date":15s}\t:{rec[5]:<15s}')
                        print('-'*80)
                        print(f'{"Room rent":16s}:Rs.{z:<6n}')
                        print(f'{"Service charges":16s}:Rs.{sercharge:<6n}')
                        print(f'{"Sales Tax(15%)":16s}:Rs.{a:<6n}')
                        print('-'*80)
                        print(f'{"Total":20s}:Rs.{total:<6n}')
                        print(f'{"Received(In Words)":20s}:Rs.{words:<100s}\n')
                        print('-'*80)
                        print()
                        print(f'{"THANK YOU FOR STAYING AT INTERNATIONAL INN":^80s}\n')
                    else:cwobj1.writerow(record)         
            else:
                found=3
                break
        else:
            cwobj.writerow(rec)
    aobj.close()
    fobj.close()
    mobj.close()
    gobj.close()
    lobj.close()
    if found==1:
        os.remove("hotelr.csv")
        os.rename("TEMP.CSV","hotelr.csv")
        os.remove("services.csv")
        os.rename("TEMP1.CSV","services.csv")
        print('═'*80)
    elif found==3:
        print()
        print("Service charges do not exist for customer")
        print("Input service charges first..\n")
        validservicebill()
        print()
        if xchk in 'eE[E][e]':
            space()
            print(f'{"ROOM SERVICE CALCULATION":^80s}\n')
            print('═'*80,'\n')
            calcroomservices()
        elif xchk in 'xX[x][X]':
            pass
        else:
            print("INVALID INPUT...")
            pass
    else:
        print()
        print("Entered record does not exist in hotel...\n")
        y=input("[R] to re-enter name [X] to quit : ")
        if y in 'rR[r][R]':
            print()
            print('-'*80,'\n')
            customerbill()
        elif y in 'xX[x][X]':
            pass
        else:
            print("INVALID INPUT...")
            pass

        
#hotel monthly income
def monthlyincome():
    try:
        fobj=open('HOTELDATA.CSV','rt')
        crobj=csv.reader(fobj)
        jant=febt=mart=aprt=mayt=junet=julyt=augt=septemt=octot=novt=dect=0
        for rec in crobj:
            print(rec)
            checkoutdate=rec[5]
            d2,m2,y2 = checkoutdate.split('/')
            m2=int(m2)
            if m2==1:
                jant+=float(rec[10])
            if m2==2:
                febt+=float(rec[10])
            if m2==3:
                mart+=float(rec[10])
            if m2==4:
                aprt+=float(rec[10])
            if m2==5:
                mayt+=float(rec[10])
            if m2==6:
                junet+=float(rec[10])
            if m2==7:
                julyt+=float(rec[10])
                print(julyt)
            if m2==8:
                augt+=float(rec[10])
            if m2==9:
                septemt+=float(rec[10])
            if m2==10:
                octot+=float(rec[10])
            if m2==11:
                novt+=float(rec[10])
            if m2==12:
                dect+=float(rec[10])
        print('Monthly total in January=',jant)
        print('Monthly total in February=',febt)
        print('Monthly total in March=',mart)
        print('Monthly total in April=',aprt)
        print('Monthly total in May=',mayt)
        print('Monthly total in June=',junet)
        print('Monthly total in July=',julyt)
        print('Monthly total in August=',augt)
        print('Monthly total in September=',septemt)
        print('Monthly total in October=',octot)
        print('Monthly total in November=',novt)
        print('Monthly total in December=',dect)
        fobj.close()
    except:print("no data on monthly income")

#Bill drop down menu#̶̿╔╚╝╗║═
def billsmenu():
    print()
    print(f'{"BILL PRINTING MENU":^80s}\n')
    print("\t\t     ╔═════════════════════════════════════╗")
    print("\t\t     ║                                     ║")
    print("\t\t     ║    ==> Bill printing options        ║")
    print("\t\t     ║                                     ║")
    print("\t\t     ║     1-->  HOTEL MONTHLY INCOME      ║")
    print("\t\t     ║     2-->  PRINT ROOM SERVICE BILL   ║")
    print("\t\t     ║     3-->  PRINT CUSTOMER BILL       ║")
    print("\t\t     ║     4-->  GO BACK TO MENU           ║")
    print("\t\t     ╚═════════════════════════════════════╝\n")
    ch=input("==> Choose option  : ").strip()
    if ch=='1':
        space()
        print(f'{"HOTEL MONTHLY INCOME":^80s}\n')
        monthlyincome()
        space()
    elif ch=='2':
        space()
        print(f'{"ROOM SERVICE BILL":^80s}')
        print()
        print('═'*80)
        roomservicebill()
        space()
    elif ch=='3':
        space()
        print(f'{"CUSTOMER BILL":^80s}\n')
        print('═'*80)
        print('\n')
        customerbill()
        space()
    elif ch=='4':
        space()
        pass
    elif len(ch)!=1:
        print("Enter a digit...\n")
        space()
        billsmenu()
    else:
        if len(ch)>1:
            print("Enter a single digit only...\n")
            space()
            billsmenu()
        else:
            print("enter a digit in range[1-4]...\n")
            space()
            billsmenu()

            
#drop down menu
while True:
    print()
    print()
    print(f'{"HOTEL MENU":^80s}\n')
    print("\t\t     ╔═════════════════════════════════════╗")
    print("\t\t     ║                                     ║")
    print("\t\t     ║  ==> List of options available      ║")
    print("\t\t     ║                                     ║")
    print("\t\t     ║     1-->  BOOKING                   ║")
    print("\t\t     ║     2-->  CANCELLATION              ║")
    print("\t\t     ║     3-->  ROOM SERVICE              ║")
    print("\t\t     ║     4-->  BILLS/INCOME              ║")
    print("\t\t     ║     5-->  UPDATE RECORDS            ║")
    print("\t\t     ║     6-->  DISPLAY OCCUPIED ROOMS    ║")
    print("\t\t     ║     7-->  QUIT                      ║")
    print("\t\t     ╚═════════════════════════════════════╝\n")
    ch=input("==> Choose option  : ").strip()
    if ch=='1':
        space()
        booking()
    elif ch=='2':
        space()
        print(f'{"CANCELLATION PROCESS":^80s}\n')
        print('═'*80)
        cancellation()
        print('═'*80)
    elif ch=='3':
        space()
        print(f'{"ROOM SERVICE CALCULATION":^80s}\n')
        print('═'*80)
        calcroomservices()
        space()
    elif ch=='4':
        print()
        space()
        billsmenu()
    elif ch=='5':
        space()
        updationdeletion()
    elif ch=='6':
        space()
        displayroomnumber()
    elif ch=='7':
        print('\n')
        print("\t\t\t    ×××××HAVE A GOOD DAY×××××")
        break
    else:
        if len(ch)==1:
            if ch.isdigit():
                print("INVALID DIGIT ENTERED (choose number from 1-7)....\n")
                space()
            else:
                print("INVALID INPUT...retry\n")
                space()
        elif len(ch)==0:
            print("Enter a digit...")
        else:
            print("Enter a single digit only....\n")
            space()

