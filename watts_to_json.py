import re
import json

def parse_text_to_json(watts_text_file):
    objects = []
    infile = open(watts_text_file).readlines()
    obj = {}
    for line in infile:
        item = [x.strip() for x in re.split(r':|\t', line.strip('\t\n\r').rstrip(" ").lstrip(" "))]
        if item[0] == "Checked_Out":
            obj["Checked_Out"] = item[2:]
        elif len(item) == 4:
            obj[item[0]] = item[1]
            obj[item[2]] = item[3]
        else:
            if item[0] != "":
                obj[item[0]] = item[1]
            elif len(obj) > 0:
                objects.append(obj)
                obj = {}
    return json.dumps(objects, sort_keys=True, indent=4, separators=(',', ':'))



if __name__ == "__main__":
    for filename in ["someP1.lib0", "someP1.lib1"]:
        outfile = open(filename + ".json", "w")
        outfile.write(parse_text_to_json(filename))





