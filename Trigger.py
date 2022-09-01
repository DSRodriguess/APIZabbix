import apizabbix

api = apizabbix.connect()

trigger = api.trigger.get({
    "output": [
        "triggerid",
        "description",
        "priority"
    ],
    "filter": {
    "value": 1
    },
    "sortfield": "priority",
    "sortorder": "DESC"
})

for trigger in trigger:
    print(
        trigger
    )
    
api.user.logout()