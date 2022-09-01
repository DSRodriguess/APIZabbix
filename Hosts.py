import apizabbix

api = apizabbix.connect()

hosts = api.host.get({
    "output": [
            "hostid",
            "host"
        ],
    "selectTriggers":'extend'

})

for hosts in hosts:
    print(
        hosts
    )
    
api.user.logout()