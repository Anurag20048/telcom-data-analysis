from pathlib import Path
import pandas as pd, random
from faker import Faker
random.seed(42); Faker.seed(42); fake=Faker("en_IN")
OUT=Path("data/raw"); OUT.mkdir(parents=True,exist_ok=True)
cities={"Mumbai":"Maharashtra","Pune":"Maharashtra","Delhi":"Delhi","Hyderabad":"Telangana","Bangalore":"Karnataka","Chennai":"Tamil Nadu","Ahmedabad":"Gujarat","Nagpur":"Maharashtra","Surat":"Gujarat","Vadodara":"Gujarat"}
ids=[]
customers=[]
for i in range(1,1001):
    city=random.choice(list(cities)); customers.append({"customer_id":100000+i,"customer_name":fake.name(),"city":city,"state":cities[city],"plan":random.choice(["Prepaid","Postpaid"]),"join_date":fake.date_between("-3y","today"),"status":random.choices(["Active","Inactive"],weights=[92,8])[0]})
customers_df=pd.DataFrame(customers); customers_df.to_csv(OUT/"customers.csv",index=False); ids=customers_df.customer_id.tolist()
pd.DataFrame([{"recharge_id":f"R{i:07d}","customer_id":random.choice(ids),"recharge_date":fake.date_between("-1y","today"),"amount":random.choice([199,299,499,699,999]),"payment_mode":random.choice(["UPI","Credit Card","Debit Card","Net Banking"])} for i in range(1,10001)]).to_csv(OUT/"recharge.csv",index=False)
pd.DataFrame([{"usage_id":f"U{i:07d}","customer_id":random.choice(ids),"usage_date":fake.date_between("-1y","today"),"data_used_gb":round(random.uniform(.1,25),2),"call_minutes":random.randint(0,800),"sms_count":random.randint(0,250)} for i in range(1,30001)]).to_csv(OUT/"usage.csv",index=False)
issues=["Network Issue","Call Drop","Slow Internet","Billing Issue","Recharge Failed","SIM Activation","SMS Not Working"]
pd.DataFrame([{"complaint_id":f"C{i:06d}","customer_id":random.choice(ids),"complaint_date":fake.date_between("-1y","today"),"issue_type":random.choice(issues),"status":random.choices(["Resolved","Pending","Open"],weights=[75,15,10])[0],"resolution_days":random.randint(0,15)} for i in range(1,5001)]).to_csv(OUT/"complaints.csv",index=False)
print("Generated 1,000 customers, 10,000 recharges, 30,000 usage records and 5,000 complaints.")
