import json
from Utils import Utils

# TODO: if you have time create a decorator to pythonifiy


def save_to_db(file_path: str, option: str, instances: str) -> None:
    pythonified = Utils.pythonify(instances)
    with open(file_path, option, encoding='utf-8') as f:
        json.dump(pythonified, f, ensure_ascii=False, indent=4, default=str)


def load_from_db(file_path: str) -> None:
    try:
        with open(file_path) as f:
            d = json.load(f)
            return d
    except:
        return None
