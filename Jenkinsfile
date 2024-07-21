pipeline {
    agent any

    stages {
        stage('Clean up') {
            steps {
                script {
                    sh 'docker system prune -a --volumes -f || true'
                }
            }
        }

        stage('Clean old containers') {
            steps {
                script {
                    sh 'docker stop feedback-container || true'
                    sh 'docker rm feedback-container || true'
                }
            }
        }

        stage('Build and Run Docker') {
            steps {
                script {
                    sh 'docker build --no-cache -t feedback-app .'
                    sh 'docker run -d -p 3000:3000 --name feedback-container feedback-app'
                }
            }
        }

        stage('Check Disk Usage') {
            steps {
                script {
                    sh 'df -h'
                }
            }
        }
    }

    post {
        always {
            script {
                sh 'docker system prune -a --volumes -f || true'
            }
        }
    }
}
