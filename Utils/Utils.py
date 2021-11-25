import re
import json


def multiple_replace(Key_dict: dict, text: str):
    # Create a regular expression  from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, Key_dict.keys())))

    # For each match, look-up corresponding value in dictionary
    return regex.sub(lambda mo: Key_dict[mo.string[mo.start():mo.end()]], text)


def pythonify_key(key: str):
    new_key = key
    if len(key) > 4:
        new_key = '"' + key[1].lower()
        for letter in key[2::]:
            if letter.isupper():
                letter = f"_{letter.lower()}"
            new_key += letter
    return new_key


def pythonify(instances: dict):

    pattern = "(\"\w+\":)"
    inst_str = json.dumps(instances, default=str)
    all_finds = re.findall(pattern, inst_str)
    keys_dict = {}
    for i in all_finds:
        keys_dict[i] = pythonify_key(i)
    new_instances_str = multiple_replace(keys_dict, inst_str)
    return json.loads(new_instances_str)
