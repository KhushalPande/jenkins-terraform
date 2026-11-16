variable "name" {
  description = "Name prefix for all resources"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "allowed_http_cidr" {
  description = "CIDR block allowed to reach port 80"
  type        = string
  default     = "0.0.0.0/0"
}
