import json
import csv
import time
import numpy

    

# ONETIME SCRIPT TO UPDATE LATEST LIST OF TOP 1M WEBSITES
# Read the top-1million.csv file and store it into a sorted list and JSON for easily accessing of data.

def create_sorted_arr_and_dict():

    try:
        start = time.time()
        domain_data_array = []
        domain_data_dict = {}

        with open('top-1million.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                domain_data_array.append(row[1]) # saving domain to list
                domain_data_dict[row[1]] = row[0] # saving domain : rank to dict

        # Sort the list by domain name
        sorted_domain_data = sorted(domain_data_array)

        # Open the file in write mode to clear the contents
        with open('sorted-top1million.txt', 'w') as outfile:
            pass

        # Save the sorted data to a new file
        with open('sorted-top1million.txt', 'w') as outfile:
            for row in sorted_domain_data:
                outfile.write(row + '\n')

        # Open the file in write mode to clear the contents
        with open('domain-rank.json', 'w') as outfile:
            pass

        # Write the dictionary to the file
        with open('domain-rank.json', 'w') as outfile:
            json.dump(domain_data_dict, outfile)

        end = time.time()

        print('Script Executed Successfully.')
        print('Execution Time : ', end - start)

    except Exception as e:
        print(f"Error: {e}")


# create_sorted_arr_and_dict() # UNCOMMENT AND RUN THE SCRIPT WHILE UPDATING THE LATEST LIST