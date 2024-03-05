bind = "0.0.0.0:8001"
module = "intranet_innovatore.wsgi:application"

workers = 4  # Ajuste com base nos recursos do seu servidor
worker_connections = 1000
threads = 4

certfile = "/etc/letsencrypt/live/srv479192.hstgr.cloud/fullchain.pem"
keyfile = "/etc/letsencrypt/live/srv479192.hstgr.cloud/privkey.pem"
