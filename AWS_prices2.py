import requests
import warnings
import pandas as pd
warnings.filterwarnings('ignore')



regions=['ap-northeast-1','ap-south-1','ap-southeast-1','ap-southeast-2','eu-central-1','eu-west-1','eu-west-2','us-east-1','us-east-2','us-west-1','us-west-2']
OS=['linux','rhel','windows']

links=[]
for region in regions:
    for system in OS:
        links.append("https://a0.p.awsstatic.com/pricing/1.0/ec2/region/" + region + "/reserved-instance/" + system + "/index.json?")

superdict=[]

for link in links:
    print("Downloading data from: " + link)
    res=requests.get(link,verify=False).json()
    superdict.append(res)


df={"Region":[],"System":[],"Type":[],"Price":[],"On demand":[],"Offering class":[]}



for res in superdict:
    for item in res['prices']:
        if item['attributes']['aws:offerTermLeaseLength']=="3yr" \
        and (item['attributes']['aws:offerTermOfferingClass'] =="convertible"
             or item['attributes']['aws:offerTermOfferingClass'] =="standard")\
        and item['attributes']['aws:offerTermPurchaseOption']=="No Upfront":
            if item['attributes']['aws:ec2:operatingSystem']=="Linux":
            #and item['attributes']['aws:ec2:instanceType'].endswith(('.large','.nano')):
                df["Region"].append(item['attributes']['aws:region'])
                df["System"].append("Linux/UNIX")
                df["Type"].append(item['attributes']['aws:ec2:instanceType'])
                df["Price"].append(float(item['calculatedPrice']['effectiveHourlyRate']['USD']))
                df["On demand"].append(item['calculatedPrice']['onDemandRate']['USD'])
                df["Offering class"].append(item['attributes']['aws:offerTermOfferingClass'])

            
            elif item['attributes']['aws:ec2:operatingSystem']=="RHEL":
                df["Region"].append(item['attributes']['aws:region'])
                df["System"].append("Red Hat Enterprise Linux")
                df["Type"].append(item['attributes']['aws:ec2:instanceType'])
                df["Price"].append(float(item['calculatedPrice']['effectiveHourlyRate']['USD']))
                df["On demand"].append(item['calculatedPrice']['onDemandRate']['USD'])
                df["Offering class"].append(item['attributes']['aws:offerTermOfferingClass'])
            elif item['attributes']['aws:ec2:operatingSystem']=="Windows":
                df["Region"].append(item['attributes']['aws:region'])
                df["System"].append("Windows")
                df["Type"].append(item['attributes']['aws:ec2:instanceType'])
                df["Price"].append(float(item['calculatedPrice']['effectiveHourlyRate']['USD']))
                df["On demand"].append(item['calculatedPrice']['onDemandRate']['USD'])
                df["Offering class"].append(item['attributes']['aws:offerTermOfferingClass'])
            
                

data=pd.DataFrame.from_dict(df).sort_values("System")
data.to_csv(r'C:\Users\SG0301917\OneDrive - Sabre\Desktop\Prices_df.csv',index=False)


