pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'dev', url: 'https://github.com/dhaval-narale/inventory-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t inventory-app .'
            }
        }

        stage('Remove Old Container') {
            steps {
                sh 'docker rm -f inventory-app || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:80 --name inventory-app inventory-app'
            }
        }
    }
}
