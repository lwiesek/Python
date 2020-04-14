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
    
def split_by_cat(dataframe, column_name):
    '''
    this function splits dataframe into chunks
    based on categorical data column
    '''
    cat_list = dataframe[column_name].unique().tolist()
    df_list = []
    for cat in cat_list:
        df = dataframe[dataframe[column_name]==cat]
        df_list.append(({column_name: cat}, df))
    return df_list

def merge_splitted(df_list):
    '''
    this function merges dataframe chunks
    from split_by_cat list of tuples
    to single df
    '''
    frames = []
    for df_tuple in df_list:
        cat_dict, df = df_tuple
        frames.append(df)
    return pd.concat(frames)


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
                    # add new column, copy values from Product
                    df['System']=df['Product']
                    # split by Product as category to get Linux- and RHEL-only dfs
                    df_list = split_by_cat(df, 'Product')
                    for df_tuple in df_list:
                        cat_dict, dfs = df_tuple
                        if cat_dict['Product'] == 'Linux/UNIX':
                            linux_df = dfs
                        elif cat_dict['Product'] == 'Red Hat Enterprise Linux':
                            rhel_df = dfs
                    # get all unique AMIs from Linux instances
                    unique_linux_amis = linux_df['AMI'].unique().tolist()
                    # iterate through RHEL instances and change Product_by_AMI to Linux/UNIX when appropriate (time measured)
                    for index, row in rhel_df.iterrows():
                        if row['AMI'] in unique_linux_amis:
                            rhel_df.at[index, 'System'] = 'Linux/UNIX'
                    df_out = merge_splitted(df_list)
                    
                    df_out.to_csv(outfile_name1, index=False)
                    print('Saved file:', outfile_name1)
                    
                elif 'Reservations for Dashboard Refresh' in att.FileName:
                    print('Sender:' , message.sender)
                    outfile_name1 = folderRes + '\\' + att.FileName
                    att.SaveASFile(outfile_name1)
                    df1 = pd.read_csv(outfile_name1)
                    df1.insert(0, 'Date', dateConvert(att))
                    df1.to_csv(outfile_name1, index=False)
                    print('Saved file:', outfile_name1)                   
                

        except Exception as e:
            x=1

except Exception as e:
    x=1


response = input("Press any key to exit")
