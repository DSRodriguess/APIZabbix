import apizabbix

api = apizabbix.connect()

problem = api.problem.get(
    output='extend',
    selectAcknowledges = 'extend',
    recent= 'true',
    sortfield = ["eventid"],
    sortorder = 'DESC'
)

for problem in problem:
    print(
        problem
    )
 
api.user.logout()