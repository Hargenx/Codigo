#!/bin/bash
set -euxo pipefail
# Amazon Linux usa dnf
sudo dnf -y update
sudo dnf -y install nginx
sudo systemctl enable --now nginx
cat <<'HTML' | sudo tee /usr/share/nginx/html/index.html
<!doctype html>
<html><head><meta charset="utf-8"><title>Oficina EC2</title></head>
<body style="font-family:system-ui;max-width:720px;margin:40px auto">
<h1>Olá, EC2! 🚀</h1>
<p>Instância criada via <strong>User Data</strong> e Nginx configurado automaticamente.</p>
</body></html>
HTML