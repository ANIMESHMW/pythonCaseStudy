import cx_Oracle

import sys
try:
    con = cx_Oracle.connect('SYSTEM/root1234A@localhost:1521/orcl')
except:
    print("Connection cannot be established")

class Vehicle:
    

    def __init__(self):

        pass

    def create(self,  mpg,  VIN):

        self.mpg = mpg

        self.VIN = VIN

    def getVin(self):
        print(self.VIN)


    def isReserved(self):
#select * from registration where VIN=self.VIN

        if c>0:
            return True

    def getDescription(self):
        print(self,  self.mpg,  self.VIN)


    def setReserved(self,reserved):
        c=1

class Truck(Vehicle):

    

    def __init__(self):
        pass

    def create(self,  mpg,length, VIN,num_rooms):

        self.mpg = mpg
        self.num_rooms=num_rooms
        self.length=length
        self.VIN = VIN

    def getDescription(self):
        print(self,  self.mpg, self.VIN)


class Van:
    

    def __init__(self):
        pass

    def create(self, make_model, mpg, numberofpassenger,  VIN):
        self.make_model = make_model
        self.mpg = mpg
        self.numberofpassenger = numberofpassenger

        self.VIN = VIN

    def getDescription(self):
        print(self, self.make_model, self.mpg, self.numberofpassenger,self.VIN)

class VehicleCost:
    

    def __init__(self):
        pass

    def create(self,daily_rate, weekly_rate , weekend_rate, free_miles , per_mile_chrg, insur_rate,vehicle_type):

        self.daily_rate=daily_rate
        self.weekly_rate=weekly_rate
        self.weekend_rate=weekend_rate
        self.free_miles=free_miles
        self.per_mile_chrg=per_mile_chrg
        self.insur_rate=insur_rate
        self.vehicle_type=vehicle_type

    def getDescription(self):
        print(self,  self.mpg, self.VIN)


    def getDailyRate(self):
        print(self.daily_rate)
        return self.daily_rate

    def getWeeklyRate(self):
        print(self.weekly_rate)

    def getWeekendRate(self):
        print(self.weekend_rate)

    def getFreeDailyMiles(self):
        print(self.free_miles)

    def getPerMileCharge(self):
        print(self.per_mile_chrg)

    def getInsuranceRate(self):
        print(self.insur_rate)
        return self.insur_rate

    def getCosts(self):
        print("Daily rate",self.daily_rate)
        print("Weekly rate",self.weekly_rate)
        print("Weekend rate",self.weekend_rate)
        print("Free miles",self.free_miles)
        print("Per_mile_chrg",self.per_mile_chrg)
        print("Insur_rate",self.insur_rate)

class VehicleCosts(VehicleCost):
    def __init__(self):
        pass
    def create(self,vehicle_type):
        pass
    def getVehicleCosts(self,vehicle_type):
        
        cur = con.cursor()
        cur.execute('select * from vehiclecost where vehicle_type=:s', s=vehicle_type)
        return cur.fetchone()
        
    def calcRentalCost(self,vehicle_type, rental_period, want_insurance , miles_driving):
        #cost=vehicle_typeo.getDailyRate();
        vehco=VehicleCosts()
        cost=vehco.getVehicleCosts(vehicle_type)
        #issur_rate=self.insur_rate()
        if want_insurance==1:
            total=int(cost[1])*rental_period+int(cost[6])
        else:
            total=int(cost[1])*rental_period

        rent_miles=miles_driving-int(cost[4])
        if rent_miles>0:
            total=total+rent_miles*int(cost[5])
            return total
        else:
            return total
        

    def addVehicleCost(self,veh_type,veh_cost):
        pass



class vehicles():
    def __init__(self):
        pass
    def create(self):
        pass
    def getVehicle(self,vin):
       
        cur = con.cursor()
        cur.execute('select type from vehicles where vin=:s', s=vin)

        a = cur.fetchone()
        return a[0]
    

    def addVehicle(self,vehicle):
       
        cur = con.cursor()
        cur.execute('insert into vehicles values( )', (vin))

    def numAvailVechicles(self,typeo):
    
        cur = con.cursor()
        
        cur.execute("select count(*) from vehicles where type=:s minus select count(*) from reservation where type=:s ",s=typeo)
        a=cur.fetchone()
        return a[0]
    def getAvailVehicles(self,typeo):
    
        cur = con.cursor()
        
        cur.execute("select vin from vehicles where type=:s minus (select vin from reservation where type=:s)",s=typeo)
        print("The following Vehicle identification nos are available for you")
        for vin in cur.fetchall ():
            print(vin)
   
class Reservation():
    def __init__(self):
        pass
    def create(self,name,address,credit_card,vin):
        self.name=name
        self.address=address
        self.credit_card=credit_card
        self.vin=vin
    def getName(self):
        return self.name
    def getAddr(self):
        return self.address
    def credit_card(self):
        return self.credit_card
    def getVin(self):
        return self.vin




class Reservations():
    def __init__(self):
        pass
    def isReserved(self,vin):
        
        cur=con.cursor()
        cur.execute('select count(*) from reservation where vin=:s',s=vin)
        a=cur.fetchone()
        n=int(a[0])
        if n>0:
            print("it is reserved")
        else:
            print("the vehcile is not reserved")
    def  getVinForReserv(self,credit_card):
        
        cur = con.cursor()
        cur.execute('select vin from reservation where credit_card=:s', s=credit_card)

        a = cur.fetchone()
        return a
    def addReservation(self,resv,vin,credit_card,address,cost):

        
        cur = con.cursor()
        res=Reservations()
        b=res.getVinForReserv(credit_card)
        if b is not None:
            
        #cur.execute("insert into vehicles select * from vehicle1 where vin=(select vin from reservation where credit_card=:c)",c=credit_card)
        #cur.execute('update vehicles set avail=:y where vin=(select vin from reservaton where credit_card=:s) ',s=credit_card,y="yes")
            
            print ("Reservation is there")
        else:
          
            cur.execute('select type from vehicles where vin=:v',v=vin)
            a=cur.fetchone()
            ty=a[0]
            cur.execute('insert into reservation values(:S,:t,:u,:v,:w,:x)',s=resv,t=address,u=credit_card,v=vin,w=ty,x=cost)
            cur.execute('select type from vehicles where vin=:v',v=vin)
            print("Reservation is done!!")
            
       
        
        con.commit()
    def findReservation(self,name,addr):
        
        cur = con.cursor()
        cur.execute('select count(*) from reservation where name=:s and address=:t', s=name,t=addr)
        a = cur.fetchone()
        n = int(a[0])
        if n > 0:
            print("reservation is there")

        else :
            print("reservation is not there")

    def cancelReservation(self,credit_card):
        
        cur = con.cursor()
        res=Reservations()
        b=res.getVinForReserv(credit_card)
        if len(b)>0:
            
        #cur.execute("insert into vehicles select * from vehicle1 where vin=(select vin from reservation where credit_card=:c)",c=credit_card)
        #cur.execute('update vehicles set avail=:y where vin=(select vin from reservaton where credit_card=:s) ',s=credit_card,y="yes")
            cur.execute('delete from reservation where credit_card=:s', s=credit_card)
            print ("Reservation has been cancelled")
        else:
            print("reservation does not exists")
        con.commit()






        #select * from reservation where vin=:vin
i=0
while(i<=8):
    print("Enter to vehicle Reservation System");
    print(" 1 Display Vehicle type \n 2 Check Rental rates \n 3 Check Available vehicles \n 4 Get a cost of specific rental \n 5 Make a reservation \n 6 Cancel a reservation \n 7 Quit")
    choice = input()
    if int(choice)==1:
        vin=input("Enter vin")
        veho=vehicles()
        typeo=veho.getVehicle(vin)
        print("The vehicle type is ",typeo)
    if  int(choice)==2:

        typeo=input("Enter vehicle type")
        vehco=VehicleCosts()
        cost=vehco.getVehicleCosts(typeo)
        print ("Daily rate",cost[1],"\n weekly_rate",cost[2],"\nweekend_rate",cost[3],"\nfree_miles",cost[4],"\nper_mile_chrg",cost[5],"\ninsur_rate",cost[6])
    if int(choice)==3:

        veho=vehicles()
        typeo=input("Enter vehicle type")
        veho.getAvailVehicles(typeo)
    if int(choice)==4:

        vehco=VehicleCosts()
     
        typeo=input("Enter vehicle type")
        #veho.getAvailVehicles(typeo)
        print ("press 0-5","Daily rate ",0," weekly_rate ",1,"weekend_rate ",2,"free_miles ",3,"per_mile_chrg ",4,"insur_rate ",5)
        inp=input("enter 0-5")
        cost=vehco.getVehicleCosts(typeo)
        inte=int(inp)
        print("The specific cost of vehicle is ",cost[inte+1])

    if int(choice)==5:
        res=Reservations()
        vehco=VehicleCosts()
        name=input("name")
        credit_card=input("Enter your credit_card")
        vin=input("Enter VIN")
        Address=input("Enter your address")
        insur=input("Insurance required 0 or 1")
        rent=input("Rental period")
        miles=input("miles driving")
        
        cur=con.cursor()
        a=cur.execute('select type from vehicles where vin=:v',v=vin)
        b=a.fetchone()
        cost=vehco.getVehicleCosts(b[0])
        tot=vehco.calcRentalCost(b[0], int(rent), int(insur) , int(miles))
        print ("The total cost is ",tot)
        res.addReservation(name,vin,credit_card,Address,tot)
    
    if int(choice)==6:
        res=Reservations()
        cred=input("Enter your Credit_card details")
        res.cancelReservation(cred)
    
    if int(choice)==7:
        con.commit()
        con.close()
        sys.exit()
    i=i+1
    
    
con.close()
