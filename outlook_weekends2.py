import win32com.client
import os
import datetime as dt
import pandas as pd

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

print (dt.datetime.now())

reqDays=int(input("How many days you need to download: "))

# setup range for outlook to search emails (so we don't go through the entire inbox)
lastWeekDateTime = dt.datetime.now() - dt.timedelta(days = reqDays)
lastWeekDateTime = lastWeekDateTime.strftime('%m/%d/%Y %H:%M %p')

# Select main Inbox
inbox = outlook.GetDefaultFolder(6)

# Optional:  Select main Inbox, look in subfolder "Test"
#inbox = outlook.GetDefaultFolder(6).Folders["Test"]

messages = inbox.Items

# Only search emails in the time range above:
messages = messages.Restrict("[ReceivedTime] >= '" + lastWeekDateTime +"'")

print ('Reading Inbox, including Inbox Subfolders...')

# Download a select attachment ---------------------------------------
# Create a folder to capture attachments.
folderInv = r'C:\Users\SG0301917\OneDrive - Sabre\Desktop\RI calculator\Inventory'
folderRes = r'C:\Users\SG0301917\OneDrive - Sabre\Desktop\RI calculator\Reservations'
#if not os.path.exists(Myfolder): os.makedirs(Myfolder)


def dateConvert(att):
    fullDate=att.FileName.split(',')[1].lstrip() + att.FileName.split(',')[2].split('_')[0]
    days=dt.datetime.strptime(fullDate,'%B %d %Y').strftime('%Y-%m-%d')
    return days

def renameColumns(df):
    column_indices=list(range(7,8))
    new_name=["#NAME?"]*len(column_indices)
    old_names=df.columns[column_indices]
    df.rename(columns=dict(zip(old_names,new_name)),inplace=True)
    


try:
    for message in list(messages):
        try:
            s = message.sender
            s = str(s)
            
            for att in message.Attachments:
                if 'Inventory for Dashboard Refresh' in att.FileName:                    
                # Give each attachment a path and filename
                    print('Sender:' , message.sender)
                    outfile_name1 = folderInv + '\\'  + att.FileName
                    att.SaveASFile(outfile_name1)
                    df = pd.read_csv(outfile_name1)
                    renameColumns(df)
                    df.insert(0, 'Date', dateConvert(att))
                    df.to_csv(outfile_name1, index=False)
                    print('Saved file:', outfile_name1)
                    
                elif 'Reservations for Dashboard Refresh' in att.FileName:
                    print('Sender:' , message.sender)
                    outfile_name1 = folderRes + '\\' + att.FileName
                    att.SaveASFile(outfile_name1)
                    df = pd.read_csv(outfile_name1)
                    df.insert(0, 'Date', dateConvert(att))
                    df.to_csv(outfile_name1, index=False)
                    print('Saved file:', outfile_name1)                   
                

        except Exception as e:
            x=1

except Exception as e:
    x=1


response = input("Press any key to exit")
