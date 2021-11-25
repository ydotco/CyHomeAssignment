conf_dict = {'ec2': {'key': 'AKIA5OTURWZJO5J4PSPB',
                     'token': 'FoZaYFiq7rJWaSUne/6qck7ntvM6CRRD6j3Ls03T',
                     'default_region': 'us-east-2'},
             'ec2_wanted_keys': {'Architecture', 'ImageId', 'InstanceId', 'InstanceType', 'LaunchTime', 'MetadataOptions', 'Monitoring', 'NetworkInterfaces', 'Placement', 'PlatformDetails', 'PrivateDnsName', 'PublicDnsName', 'PrivateIpAddress', 'PublicIpAddress', 'SecurityGroups', 'State', 'Tags', 'ClientToken'}
             }


# Get config value if it doesnt exist return "" (empty string)
def get_conf(section: str, key: str):
    if section in conf_dict:
        if key in conf_dict[section]:
            return conf_dict[section][key]
    return ""
