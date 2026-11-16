# Jenkins CI/CD + Terraform Mini Project

* **CI/CD:** a Jenkins declarative pipeline (Checkout -> Build -> Test -> Package -> Deploy -> Smoke Test)
  for a small Flask app. Jenkins polls GitHub every ~2 minutes and redeploys the app as a Docker container.
* **IaC:** Terraform (module-based) that provisions an Ubuntu EC2 web server and a security group on AWS.

## Structure
```
.
├── app.py, test_app.py, requirements*.txt   # application + pytest tests
├── Dockerfile
├── Jenkinsfile                              # CI/CD pipeline
└── terraform/
    ├── versions.tf  variables.tf  main.tf  outputs.tf  terraform.tfvars.example
    └── modules/web_server/                  # reusable module (EC2 + security group + user_data)
```

## Jenkins server setup (Ubuntu 24.04 EC2, t3.small, 20 GB)
```bash
sudo apt update
sudo apt install -y fontconfig openjdk-21-jre git docker.io python3-venv python3-pip curl
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2026.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update && sudo apt install -y jenkins
sudo systemctl enable --now docker jenkins
sudo usermod -aG docker jenkins && sudo systemctl restart jenkins
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```
Open `http://<EC2-IP>:8080`, install suggested plugins, create the admin user.
Create a **Pipeline** job -> *Pipeline script from SCM* -> Git -> this repo, branch `*/main`, script path `Jenkinsfile`.

## Terraform (AWS CloudShell or any machine with AWS credentials)
```bash
cd terraform
terraform init
terraform fmt -recursive
terraform validate
terraform plan -out=tfplan
terraform apply tfplan
terraform output
terraform destroy      # clean up to avoid charges
```
