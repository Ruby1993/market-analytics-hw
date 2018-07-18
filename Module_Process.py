import pandas as pd
import json

# Transforming the json file to csv file
def json_csv(file_path,key_output,*args):
    #file_path: (string) the path of json file
    #key_output: (string)the column name you defined to use for the key value in the json file (city name)
    #*args: (tuple) the tuple includs the attribute name you would love to bring for each element (attributes for each city)
    with open(file_path) as f:
        inp = json.load(f)
    output=pd.DataFrame()
    for key,item in inp.items():
        dic={key_output:key}
        if args:
            for arg in args:
                if arg in item.keys():
                    dic[arg]=item[arg]
                else:
                    raise Exception('The attribute in the *args is not in the json file')
        output=output.append(dic,ignore_index=True)
    return output
