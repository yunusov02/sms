import time
from pushbullet import Pushbullet
import pandas as pd

# Your Pushbullet API key
api_key = 'API_KEY'

pb = Pushbullet(api_key=api_key)
print(pb.devices)
device = pb.devices[1]

# Read the Excel file
df = pd.read_excel('index.xlsx')

# Iterate over each row in the Excel file
# for index, row in df.iterrows():
#     # Get the phone number and message from the current row
#     phone_number = "+" + str(row['Phone Number'])
#     message = str(row['Message'])
    
#     # Send the SMS using Pushbullet
#     push = pb.push_sms(device=device, number=phone_number, message=message)
#     print(push)
#     time.sleep(1)
