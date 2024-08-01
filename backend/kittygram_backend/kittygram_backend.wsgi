[Unit]
Description=gunicorn daemon

After=network.target

[Service]
User=yc-user

WorkingDirectory=/home/yc-user/kittygram/backend/

ExecStart=/home/yc-user/kittygram/backend/venv/bin/gunicorn --bind 0.0.0.0:9000 kittygram_backend.wsgi

[Install]
WantedBy=multi-user.target
