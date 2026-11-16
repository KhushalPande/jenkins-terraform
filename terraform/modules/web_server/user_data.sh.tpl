#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
apt-get update -y
apt-get install -y nginx

cat > /var/www/html/index.html <<'HTML'
<!DOCTYPE html>
<html>
<head><title>${name}</title></head>
<body style="font-family:Arial;text-align:center;padding-top:80px;background:#eef7ee">
  <h1>Provisioned with Terraform</h1>
  <p>Environment: <b>${name}</b></p>
  <p>This EC2 instance and its security group were created as code.</p>
</body>
</html>
HTML

systemctl enable --now nginx
