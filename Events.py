import apizabbix

api = apizabbix.connect()

event = api.event.get({
    "output": 'extend',
    "time_from": "1661373430",
    "time_till": "1661459830",
    "sortfield": [
        "clock", 
        "eventid"
    ],
    "sortorder": "desc"
})

print (event)