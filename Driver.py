from UnitTest import test_utils
import pytest
from Config import ConfigHelper
from Ec2Helper.Ec2Manager import Ec2Handler
from DBHelper import DBUtils
from dacite import Config, from_dict
from Models import InstanceModel

# Welcome :)
# In the config file you can filter which data you want to get from ec2. just add it to the set


KEY_KEY = "key"
TOKEN_KEY = "token"
REGION_KEY = "default_region"
SECTION_KEY = "ec2"

key = ConfigHelper.get_conf(SECTION_KEY, KEY_KEY)
token = ConfigHelper.get_conf(SECTION_KEY, TOKEN_KEY)
default_region = ConfigHelper.get_conf(SECTION_KEY, REGION_KEY)

# get ec2 data
ec2 = Ec2Handler(key, token, default_region)

all_instances = ec2.get_all_instances()

# save to db, in our case a json file (can be any key value db)
DBUtils.save_to_db('data.json', 'a+', all_instances)

# load saved json to object
instances = DBUtils.load_from_db('data.json')
if(instances is not None):
    instaces_dataclasses = []
    for k, v in instances.items():
        instaces_dataclasses.append(from_dict(InstanceModel.Instance, v))

# now we have a list objects with all our wanted information,
# so we can play around, make different graphs or do as we wish.
