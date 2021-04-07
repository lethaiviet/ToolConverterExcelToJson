import time
import json
import sys
import pandas as pd
from pyexcel_xlsx import get_data

DETERMINER = "\n"
# the keys have values that array type
G_SPEC_KEY = ["roles", "members"]

# ==================================================================================================
#     MAIN                                                                                        #
# ==================================================================================================
def main(argv):
    if is_json_file(argv):
        convert_json_to_excel(argv)
        return

    if is_excel_file(argv):
        convet_excel_to_json(argv)
        return

    # ==================================================================================================
    #     FUNCTION                                                                                    #
    # ==================================================================================================


def export_json(file_path, data, is_minify=False):
    with open(file_path, 'w') as out_file:
        if is_minify:
            # dump file json format minify
            json.dump(data, out_file, separators=(',', ':'))
        else:
            json.dump(data, out_file, sort_keys=True,
                      indent=4, ensure_ascii=False)


def read_excel(file_path):
    return get_data(file_path)


def create_dict_from_keys_n_values(keys, values):
    num_key = len(keys)
    num_value = len(values)

    result_dict = {}
    for idx in range(0, num_key):
        key = keys[idx]
        value = "" if idx > (num_value - 1) else values[idx]
        if(key in G_SPEC_KEY):
            values_array = value.split(DETERMINER)
            result_dict[key] = values_array
        else:
            result_dict[key] = value
    return result_dict


def read_json(path_file):
    with open(path_file) as json_file:
        data = json.load(json_file)
    return data


def convert_json_to_excel(file_path):
    output = file_path.split('.')[0] + '.xlsx'
    print("\nConvert json to excel: " + file_path + " -> " + output)
    data_json = read_json(file_path)
    new_data = []

    # Restruct the data is array
    for old_obj in data_json:
        new_obj = {}
        for key, value in old_obj.items():
            if isinstance(value, list):
                new_obj[key] = DETERMINER.join(value)
            else:
                new_obj[key] = value
        new_data.append(new_obj)

    df = pd.DataFrame(new_data)
    df.to_excel(output, index=False)
    print("DONE")


def convet_excel_to_json(file_path):
    raw_data = read_excel(file_path)

    for sheet_name in raw_data:
        users_data = []
        header_row = raw_data[sheet_name][0]
        num_user = len(raw_data[sheet_name])

        for idx in range(1, num_user):
            row_in_idx = raw_data[sheet_name][idx]
            data_dict = create_dict_from_keys_n_values(header_row, row_in_idx)
            users_data.append(data_dict)

        output = sheet_name + '.json'
        print("\nConvert json to excel: " + file_path + " -> " + output)
        export_json(sheet_name + '.json', users_data)
        print("DONE")


def is_json_file(name):
    return ".json" in name


def is_excel_file(name):
    return ".xlsx" in name


if __name__ == "__main__":
    main(sys.argv[1])
