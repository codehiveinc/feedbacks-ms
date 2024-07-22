pipeline {
    agent any

    stages {
        stage('Clean old containers') {
            steps {
                script {
                    sh 'docker stop feedbacks-ms-container || true'
                    sh 'docker rm feedbacks-ms-container || true'
                }
            }
        }

        stage('Prepare .env file') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'envFeedbacks', variable: 'ENV_FILE_CONTENT')]) {
                        
                        writeFile(file: '.env', text: "${ENV_FILE_CONTENT}")
                    }
                }
            }
        }

        stage('Build and Run Docker') {
            steps {
                script {
                    sh 'docker build -t feedbacks-ms .'
                    sh 'docker run -d -p 8000:8000 --name feedbacks-ms-container --env-file .env feedbacks-ms'
                }
            }
        }
    }
}
