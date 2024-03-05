bind = "0.0.0.0:8001"
module = "intranet_innovatore.wsgi:application"

workers = 4  # Ajuste com base nos recursos do seu servidor
worker_connections = 1000
threads = 4

# certfile = "/etc/letsencrypt/live/intranet.innovatore.eng.br/fullchain.pem"
# keyfile = "/etc/letsencrypt/live/intranet.innovatore.eng.br/privkey.pem"
