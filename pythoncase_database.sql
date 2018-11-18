select * from dual;
drop table vehiclecost;
drop table reservation;
select * from vehicles;
select * from reservation;
drop table reservation;
select * from car;
select * from vehiclecost;
update vehicles set avail='yes';

alter table reservation add cost varchar2(20);
delete from reservation;
desc vehiclecost;
create table vehicle1 as select * from vehicles where 1=2;

alter table reservation add sequence seq(name); 
create sequence seq start with 1 increment by 1;
create table reservation (name varchar(20),address 
varchar(20),credit_card varchar(20),vin varchar(20) references vehicles(vin));
create table car (make_model varchar(20),mpg 
varchar(20),numberofpassengers varchar(20),numberofdoors varchar(20),vin 
varchar(20) 
references vehicles(vin));
drop table vehicles;
create table van(make_model varchar(20),mpg 
varchar(20),numberfpassengers varchar(20),vin varchar(20) references vehicles(vin));

create table truck(mpg varchar(20),length varchar(20),num_rooms 
varchar(20),vin varchar(20) references vehicles(vin));

create table vehiclecost(vehicle_type varchar(20),daily_rate 
varchar(20), weekly_rate varchar(20) , weekend_rate varchar(20), 
free_miles varchar(20), per_mile_chrg varchar(20), insur_rate varchar(20));

create table vehicles(mpg varchar(20),vin varchar(20) primary key,type varchar(20));
drop table truck;
select value from v$parameter where name='service_names';


