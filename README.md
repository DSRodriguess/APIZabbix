
# 📡 APIZabbix

Este projeto consiste em uma coleção de scripts Python desenvolvidos para interagir com a API do Zabbix.
O objetivo é facilitar a automação de tarefas administrativas e operacionais, como a obtenção de eventos, hosts, grupos de hosts, triggers, serviços e problemas.

## 🧰 Funcionalidades

Os scripts disponíveis permitem:

- **Consulta de Eventos**: Recupera eventos registrados no Zabbix.
- **Consulta de Eventos por Grupo de Hosts**: Filtra eventos com base em grupos de hosts específicos.
- **Consulta de Grupos de Hosts**: Lista todos os grupos de hosts configurados.
- **Consulta de Hosts**: Obtém informações detalhadas sobre os hosts monitorados.
- **Consulta de Problemas**: Identifica problemas ativos no ambiente monitorado.
- **Consulta de Serviços**: Acessa dados relacionados aos serviços monitorados.
- **Consulta de Triggers**: Recupera informações sobre triggers configuradas.

## 🗂️ Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
APIZabbix/
├── apizabbix.py           # Script principal para interações com a API
├── config.ini             # Arquivo de configuração com parâmetros de conexão
├── Events.py              # Script para consulta de eventos
├── EventsHostGroup.py     # Script para consulta de eventos por grupo de hosts
├── HostGroup.py           # Script para consulta de grupos de hosts
├── Hosts.py               # Script para consulta de hosts
├── Problem.py             # Script para consulta de problemas
├── Services.py            # Script para consulta de serviços
├── Trigger.py             # Script para consulta de triggers
└── README.md              # Documentação do projeto
```

## ⚙️ Pré-requisitos

- Python 3.x
- Bibliotecas Python: `requests`

Você pode instalar as dependências necessárias utilizando:

```bash
pip install requests
```

## 🚀 Como Utilizar

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/DSRodriguess/APIZabbix.git
   cd APIZabbix
   ```

2. **Configure o arquivo `config.ini`**:

   Edite o arquivo `config.ini` com as informações do seu servidor Zabbix:

   ```ini
   [zabbix]
   url = http://seu-servidor-zabbix/api_jsonrpc.php
   user = seu_usuario
   password = sua_senha
   ```

3. **Execute os scripts desejados**:

   Por exemplo, para consultar os hosts:

   ```bash
   python Hosts.py
   ```

## 📄 Licença

Este projeto é de uso acadêmico e não possui uma licença específica definida.

## 👨‍💻 Autor

- [DSRodriguess](https://github.com/DSRodriguess)
