# Video Demo Script (5-6 minutes)

**Intro (20s)** "I'm <NAME>, PRN <PRN>. This project has two parts: a Jenkins CI/CD pipeline and Terraform infrastructure as code."

**Part 1 - Repository (40s)** Show GitHub repo: app.py, test_app.py, Dockerfile, Jenkinsfile, terraform/.
Explain: pipeline as code - the Jenkinsfile is versioned with the application.

**Part 2 - Jenkins job (40s)** Show Pipeline job configuration: Pipeline script from SCM, repo URL, branch, Jenkinsfile path.
Explain: Jenkins pulls the Jenkinsfile from Git, pollSCM checks for commits every 2 minutes.

**Part 3 - Pipeline run (90s)** Click Build Now, show Stage View while it runs. Explain each stage:
Checkout (source integration), Build (venv + dependencies), Test (pytest + JUnit report), Package (docker build), Deploy (docker run), Smoke Test (curl /health).
Show Test Result (4 passed) and the app in the browser at :5000.

**Part 4 - Automatic CI (60s)** On GitHub edit the GREETING in app.py ("version 2") and commit.
Wait for Jenkins to start build #2 ("Started by an SCM change"), then refresh the browser: new text + new build number.

**Part 5 - Terraform (90s)** In CloudShell: show main.tf, module, variables.tf. Run init, validate, plan (explain 2 resources to add), apply.
Show outputs + browser website_url + the EC2 console. Run terraform destroy (explain state and cleanup).

**Concepts recap (20s)** CI vs CD, pipeline as code, stages, triggers, JUnit reports, IaC, providers, state, plan/apply/destroy, variables, outputs, modules.
