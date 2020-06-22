import yaml
import os

# WARNING: Never forget to change base file name
fname = "cdc_deployment.yaml"

stream = open(fname, 'r')
data = yaml.load(stream)

states = ['ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'CONNECTICUT', 'DELAWARE', 'FLORIDA',
          'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE',
          'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA',
          'NEVADA', 'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO',
          'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
          'Utah', 'Vermont', 'Virginia', 'Washington', 'Washington DC', 'West Virginia', 'Wisconsin', 'Wyoming',
          'American Samoa', 'Guam', 'Puerto Rico', 'USVI']

state_groups = ["texas vermont virginia washington_dc west_virginia wisconsin",
                "california american_samoa arkansas delaware guam hawaii",
                "connecticut minnesota pennsylvania",
                "washington new_york arizona montana new_mexico north_dakota",
                "new_jersey utah rhode_island alaska oregon maryland puerto_rico wyoming",
                "colorado florida georgia idaho indiana iowa kansas michigan",
                "ohio",
                "illinois",
                "kentucky louisiana maine massachusetts mississippi missouri nebraska nevada new_hampshire northern_mariana_islands oklahoma usvi",
                "south_dakota south_carolina tennessee north_carolina alabama",
                "pennsylvania"]

group_names = ["group1", "group2", "group3", "group4", "group5", "group6", "group7", "group8", "group9", "group10",
               "group11"]

# to create volume yaml
# for state in states:
#     volume_name = 'cdc-crawler-' + state.replace(' ', '-') + '-volume'
#     volume_name = volume_name.lower()
#     data['metadata']['name'] = volume_name
#     with open("volume_yaml/" + volume_name + ".yaml", 'w') as yaml_file:
#         yaml_file.write(yaml.dump(data, default_flow_style=False, sort_keys=False))


# to create network policy
# for state in states:
#     policy_name = "allow-cdc-" + state.replace(' ', '-')
#     policy_name = policy_name.lower()
#     app_name = "cdc-crawler-" + state.replace(' ', '-')
#     app_name = app_name.lower()
#     data['metadata']['name'] = policy_name
#     data['spec']['podSelector']['matchLabels']['app'] = app_name
#     with open("network_policy_yaml/" + policy_name + ".yaml", "w") as yaml_file:
#         yaml_file.write(yaml.dump(data, default_flow_style=False, sort_keys=False))


# to create multi state network policy
# for group in group_names:
#     policy_name = "allow-cdc-" + group
#     app_name = "cdc-crawler-" + group
#     data['metadata']['name'] = policy_name
#     data['spec']['podSelector']['matchLabels']['app'] = app_name
#     with open("nw_policy_multi/" + policy_name + ".yaml", "w") as yaml_file:
#         yaml_file.write(yaml.dump(data, default_flow_style=False, sort_keys=False))

# to create deployment yaml
for state in states:
    state_name = state.replace(' ', '_').lower()
    state = state.replace(' ', '-').lower()
    app_name = "cdc-crawler-" + state
    # data_name = "cdc-data-" + state
    # volume_name = 'cdc-crawler-' + state + '-volume'
    data['metadata']['labels']['app'] = app_name
    data['metadata']['name'] = app_name
    data['spec']['selector']['matchLabels']['app'] = app_name
    data['spec']['template']['metadata']['labels']['app'] = app_name
    data['spec']['template']['spec']['containers'][0]['name'] = app_name
    data['spec']['template']['spec']['containers'][0]['env'][0]['value'] = state_name
    data['spec']['template']['spec']['containers'][0]['env'][1]['value'] = os.getenv('elastic_server_host')
    data['spec']['template']['spec']['containers'][0]['env'][2]['value'] = os.getenv('elastic_username')
    data['spec']['template']['spec']['containers'][0]['env'][3]['value'] = os.getenv('elastic_password')
    data['spec']['template']['spec']['containers'][0]['env'][4]['value'] = os.getenv('elastic_port')
    # data['spec']['template']['spec']['containers'][0]['volumeMounts'][0]['name'] = data_name
    # data['spec']['template']['spec']['volumes'][0]['name'] = data_name
    # data['spec']['template']['spec']['volumes'][0]['persistentVolumeClaim']['claimName'] = volume_name
    with open("deployment_yaml/cdc_deployment_" + state + ".yaml", "w") as yaml_file:
        yaml_file.write(yaml.dump(data, default_flow_style=False, sort_keys=False))

# to create multiple state deployment yaml
# for i in range(len(group_names)):
#     app_name = "cdc-crawler-" + group_names[i]
#     data['metadata']['labels']['app'] = app_name
#     data['metadata']['name'] = app_name
#     data['spec']['selector']['matchLabels']['app'] = app_name
#     data['spec']['template']['metadata']['labels']['app'] = app_name
#     data['spec']['template']['spec']['containers'][0]['name'] = app_name
#     data['spec']['template']['spec']['containers'][0]['env'][0]['value'] = state_groups[i]
#     with open("deployment_yaml_multiple/cdc_deployment_" + group_names[i] + ".yaml", "w") as yaml_file:
#         yaml_file.write(yaml.dump(data, default_flow_style=False, sort_keys=False))
