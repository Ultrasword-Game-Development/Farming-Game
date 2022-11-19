import sys

# use sys.argv to get input data

args = sys.argv[1::]

BASE_PATH = "engine/templates"

templates = {
    "entity": "entity_template.py",
    "other": "other.py"
}


def replace_text(data: str, to_replace: str, replace: str) -> str:
    data.replace(to_replace, replace)
    return data

def save_and_replace(in_file: str, out_file: str, replace_str: str, new_str: str) -> None:
    with open(in_file, 'r') as file:
        new = replace_text(file.read(), replace_str, new_str)
        file.close()
    # save new
    with open(out_file, 'w') as file:
        file.write(new)
        file.close()


if args:
    # run with args
    # arg 1 = template type
    # arg 2 = location
    type_string = ""
    location_string = ""
    i = 0
    while i < len(args):
        a = args[i]
        if a == '-t':
            # collect the template type
            for j in range(i+1, len(args)):
                if args[j].startswith('-'): break
                type_string += args[j]
            # we now have type string
            i = j
        elif a == '-f':
            # collect the result location
            for j in range(i+1, len(args)):
                if args[j].startswith('-'): break
                location_string += args[j]
            # we now have result string
            i = j
    
    # save the file to the resulting location
    in_file = ""
    replace_str = ""
    new_str = ""
    save_and_replace(in_file, location_string, replace_str, new_str)
    sys.exit()

# withotu args

print("Finish this file")


