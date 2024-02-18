pipeline {
    agent any
    
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/seu-usuario/seu-repositorio'
            }
        }
        
        stage('Setup') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    sh 'python -m pytest tests/test_app.py'
                }
            }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                script {
                    docker.build("my-docker-image:latest")
                    docker.withRegistry('https://registry.example.com', 'docker-registry-credentials') {
                        docker.image("my-docker-image:latest").push()
                    }
                }
            }
        }
    }
}
