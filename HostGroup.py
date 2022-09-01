import apizabbix

api = apizabbix.connect()

hostgroups = api.hostgroup.get(
    output='extend',
    excludeSearch=True
)

for hostgroup in hostgroups:
    print(
        hostgroup['name']
    )
    
api.user.logout()