module "web_server" {
  source = "./modules/web_server"

  name              = "${var.project_name}-${var.environment}"
  instance_type     = var.instance_type
  allowed_http_cidr = var.allowed_http_cidr
}
