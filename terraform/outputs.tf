output "instance_id" {
  description = "ID of the EC2 instance"
  value       = module.web_server.instance_id
}

output "public_ip" {
  description = "Public IP address of the web server"
  value       = module.web_server.public_ip
}

output "website_url" {
  description = "URL of the provisioned web server"
  value       = module.web_server.website_url
}

output "security_group_id" {
  description = "ID of the security group"
  value       = module.web_server.security_group_id
}
