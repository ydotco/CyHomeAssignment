import pytest
from Utils import Utils
from Config import ConfigHelper
from Ec2Helper.Ec2Manager import Ec2Handler


def test_pythonify():
    assert(Utils.pythonify_key('"HeyJude":') == '"hey_jude":')


def test_ec2_manager():
    KEY_KEY = "key"
    TOKEN_KEY = "token"
    REGION_KEY = "default_region"
    SECTION_KEY = "ec2"

    key = ConfigHelper.get_conf(SECTION_KEY, KEY_KEY)
    token = ConfigHelper.get_conf(SECTION_KEY, TOKEN_KEY)
    default_region = ConfigHelper.get_conf(SECTION_KEY, REGION_KEY)

    ec2 = Ec2Handler(key, token, default_region)

    all_instances = ec2.get_all_instances()

    assert(all_instances is not None)


def test_ec2_manager_wrong_cred():
    ec2 = Ec2Handler("test", "token", "default_region")
    all_instances = ec2.get_all_instances()
    assert(len(all_instances) == 0)
