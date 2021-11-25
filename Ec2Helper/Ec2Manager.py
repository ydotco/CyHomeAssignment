import boto3
from Config import ConfigHelper


class Ec2Handler():
    def __init__(self, key: str, token: str, default_region: str) -> None:
        self.key = key
        self.token = token
        self.default_region = default_region

    def get_all_instances(self):
        all_instances = {}
        try:
            ec2 = boto3.client('ec2', aws_access_key_id=self.key,
                               aws_secret_access_key=self.token,
                               region_name=self.default_region)

            # get all available regions
            regions = ec2.describe_regions()

            for region in regions['Regions']:
                instance = self.add_region(region['RegionName'])
                if instance is not None:
                    if instance["ResponseMetadata"]["HTTPStatusCode"] == 200:
                        for res in instance["Reservations"]:
                            for ins in res["Instances"]:
                                fin_ins = {}
                                for k, v in ins.items():
                                    if k in ConfigHelper.conf_dict['ec2_wanted_keys']:
                                        fin_ins[k] = v
                                all_instances[ins["InstanceId"]] = fin_ins
        except:
            pass
        return all_instances

    def add_region(self, region: str):
        ec2 = boto3.client('ec2', aws_access_key_id=self.key,
                           aws_secret_access_key=self.token,
                           region_name=region)

        try:
            data = ec2.describe_instances()
            return data
        except ec2.exceptions.ClientError as e:
            pass
