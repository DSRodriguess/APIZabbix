
import apizabbix

api = apizabbix.connect()

hostgroups = api.hostgroup.get(
    output=['id'],
    filter={
        'name': 'Zabbix servers'
    },
)

events = api.event.get(
    output=[
        'clock',
        'name',
        'value',
        'severity',
    ],
    groupids=hostgroups[0]['groupid'],
)

severidades = [
    'Não classificada',
    'Informação',
    'Atenção',
    'Média',
    'Alta',
    'Desastre'
]

from datetime import datetime

for event in events:
    hora_evento = datetime.fromtimestamp(
        int(event['clock'])).strftime('%Y-%m-%d %H:%M:%S')
    severidade = severidades[(int(event['severity']))]
    print(
        'Evento: ' + event['name'] + ', ocorrido em: ' + hora_evento + ' com severidade ' + severidade)

api.user.logout()