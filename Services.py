import apizabbix

api = apizabbix.connect()

service = api.service.get(
    output='extend',
    selectTrigger='extend'
)

for service in service:
    print(
        service
    )
 
api.user.logout()