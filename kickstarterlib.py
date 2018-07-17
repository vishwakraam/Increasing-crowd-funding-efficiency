'''
Date - December 18, 2016

P4DS Final Project - Increasing Crowdfunding Efficiency - 2
Group 8: Ayoola Ogunsola, Sameer Vinayak, Malvika Tripathi, Edwin Mercado
'''

import csv
import datetime
from collections import deque
from campaign import *

def cleanFile(file, skip_header, file_writer):
    '''Clean file, add extra columns and write out to another file'''

    header_skipped = False   # Store whether header row has been skipped
    try:
        # Open csv file and read data; encode in utf-8 to avoid UnicodeDecodeError
        with open(file, newline='', encoding='utf-8') as csvfile:
            csv_data = csv.reader(csvfile, delimiter=',')
            # If SkipHeader is True, skip Header row
            if skip_header:
                fields = csv_data.__next__();
                header_skipped = True
            # From each row
            for row in csv_data:
                # Remove columns 2, 6, 8-9, 11-13, 15-16, 20, 22-25, 27-32
                # Start from end so indices are correct
                del (row[26:32], row[21:25], row[19], row[14:16], row[12], row[10:12])
                del (row[7:9], row[5], row[1])

                # Reformat and add extra columns if not the header
                if header_skipped:
                    # Change the date columns from Unix time to Datetime.Date
                    for i in [6, 7]:
                        row[i] = datetime.date.fromtimestamp(int(row[i]))

                    # Add additional columns
                    addNewColumns(row)   
                else:
                    # If header, add the extra column headers
                    row.append("name_length")
                    row.append("blurb_length")
                    row.append("campaign_length")
                    row.append("percent_funded")
                    row.append("excess_funds")
                    row.append("deficient_funds")
                    # This is header row; skip and store action
                    header_skipped = True;    

                # Write out new file
                file_writer.writerow(row)
   #except:
        #print("error!")
    finally:
        #outFile.close()
        pass

def addNewColumns(row):
    ''' Add values to new columns in data file '''
    
    if row[4] == "successful":
        s = Successful(row[0], row[1], row[2], row[3], row[4], row[5],
                       row[6], row[7], row[8], row[9], row[10], row[11])
        
        # Add column values to a queue
        queue1 = deque()
        queue1.append(s.calcNameLength())     # Store name_length
        queue1.append(s.calcBlurbLength())    # Store blurb_length
        queue1.append(s.calcCampaignLength()) # Store campaign_length
        queue1.append(s.percentFunded())      # Store percent_funded
        queue1.append(s.calcExcessFunds())    # Store excess_funds
        queue1.append(float(0))  # Store deficient_funds (0 for successful campaigns)

        # Add each column value to the row
        for k in range(len(queue1)):
            row.append(queue1.popleft())    # Write out each column value
            
    elif row[4] == "live":
        l = Live(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                 row[7], row[8], row[9], row[10], row[11])
        
        # Add column values to a queue
        queue2 = deque()
        queue2.append(l.calcNameLength())     # Store name_length
        queue2.append(l.calcBlurbLength())    # Store blurb_length
        queue2.append(l.calcCampaignLength()) # Store campaign_length
        queue2.append(l.percentFunded())      # Store percent_funded
        queue2.append(float(0))  # Store excess_funds (0 for live campaigns)
        queue2.append(float(0))  # Store deficient_funds (0 for live campaigns)
        
        # Add each column value to the row
        for k in range(len(queue2)):
            row.append(queue2.popleft())
            
    else:
        u = Unsuccessful(row[0], row[1], row[2], row[3], row[4], row[5],
                         row[6], row[7], row[8], row[9], row[10], row[11])
        
        # Add column values to a queue
        queue3 = deque()
        queue3.append(u.calcNameLength())     # Store name_length
        queue3.append(u.calcBlurbLength())    # Store blurb_length
        queue3.append(u.calcCampaignLength()) # Store campaign_length
        queue3.append(u.percentFunded())      # Store percent_funded
        queue3.append(float(0))  # Store excess_funds (0 for unsuccessful campaigns)
        queue3.append(u.calcDeficientFunds()) # Store deficient_funds

        # Add each column value to the row
        for k in range(len(queue3)):
            row.append(queue3.popleft())    
    
                                                
def main():
    ''' Main code for testing '''
    out_file = open("myKick3.csv", 'w', newline='', encoding='utf-8')
    file_writer = csv.writer(out_file, delimiter=',')
    cleanFile("Kickstarter.csv", False, file_writer)
    out_file.close()

    # Print out constants
    count_list = [Campaign.campaignCount, Successful.successCount, Live.liveCount,
                  Unsuccessful.unsuccessCount]
    print(count_list) 


# Execute main only when this file is executed drectly
# Do not run main when file is imported into another file
if __name__ == '__main__':
    main()
    
