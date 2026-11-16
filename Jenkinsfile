pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    // Continuous Integration: poll GitHub every ~2 minutes and build on new commits
    triggers {
        pollSCM('H/2 * * * *')
    }

    environment {
        APP_NAME = 'ci-demo-app'
        IMAGE    = "ci-demo-app:${env.BUILD_NUMBER}"
        APP_PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log -1 --pretty=format:"Commit: %h - %s (%an)"'
            }
        }

        stage('Build') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --quiet -r requirements.txt -r requirements-dev.txt
                    echo "Dependencies installed"
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -v --junitxml=report.xml
                '''
            }
            post {
                always {
                    junit 'report.xml'
                }
            }
        }

        stage('Package') {
            steps {
                sh 'docker build -t ${IMAGE} -t ${APP_NAME}:latest .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f ${APP_NAME} || true
                    docker run -d --name ${APP_NAME} --restart unless-stopped \
                        -p ${APP_PORT}:5000 -e APP_VERSION=${BUILD_NUMBER} ${IMAGE}
                '''
            }
        }

        stage('Smoke Test') {
            steps {
                sh '''
                    for i in 1 2 3 4 5 6 7 8; do
                        if curl -fsS http://localhost:${APP_PORT}/health; then
                            echo ""
                            echo "Smoke test passed"
                            exit 0
                        fi
                        sleep 3
                    done
                    echo "Smoke test FAILED"
                    exit 1
                '''
            }
        }
    }

    post {
        success {
            echo "Build #${env.BUILD_NUMBER} deployed successfully: http://<EC2-PUBLIC-IP>:5000"
        }
        failure {
            echo "Build #${env.BUILD_NUMBER} FAILED - check the stage logs above"
        }
        always {
            sh 'docker image prune -f || true'
        }
    }
}
