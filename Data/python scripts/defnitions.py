import csv
import random
import shutil
import json

from tempfile import NamedTemporaryFile

#local imports
from variables import field_names, values, filename

def generate(fieldname):
    #create a temp file to store modifications done to the csv file
    temp_file = NamedTemporaryFile(dir=".\Temp", mode="w+t", delete=False, newline='')


    values_list = values[fieldname]
    with open('dependencies.json') as f:
        #load the dependencies dictonary into dependency_data
        dependency_data = json.load(f)
        #store the self weight into final_weights
        if dependency_data[fieldname] != "random" :
            final_weights = []
            working_dict = dependency_data[fieldname]
            #print(working_dict)
            no_dependencies = len(working_dict)
            self_weights = dependency_data[fieldname]["self"]
            final_weights = self_weights

        #open the files csv file and temp file to write the modifications to
        with open(filename, "rt") as csvReaderFile,temp_file:
            reader = csv.DictReader(csvReaderFile)
            writer = csv.DictWriter(temp_file, fieldnames=field_names, delimiter=',')
            #Write header row
            writer.writeheader()
            #copy contents with neccesary logic
            #fetching dependencies and weight from file
            for row in reader:
                if dependency_data[fieldname] == "random" :
                    row[fieldname]=random.choice(values_list)
                else:
                    if no_dependencies != 1 :
                        for i in range(1,no_dependencies):
                            keys_list = list(working_dict.keys())
                            dependency_name = keys_list[i]
                            weights = working_dict[dependency_name][values[dependency_name].index(row[dependency_name])]
                            #print(values[dependency_name].index(row[dependency_name]))
                            for index in range(0, len(weights)):
                                final_weights[index]+=weights[index]	
                    row[fieldname]=random.choices(values_list,weights=final_weights)[0]
                writer.writerow(row)
            temp_file.close()
            print("temp file name:",temp_file.name)
            shutil.move(temp_file.name, filename)
