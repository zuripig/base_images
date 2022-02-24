
pipeline {
    agent any
    
    environment {
        FILE_NAME = "scan_${BUILD_NUMBER}"
        }

    stages {
        stage('Build') {
            steps {
                sh 'echo building ${FILE_NAME}'
            }
        }
        stage('Scan') {
            steps {
                sh 'echo scanning'
            }
        }
        stage('zip') {
            steps {
                sh 'echo zipping'
                sh 'zip -r python.zip ./*.py
            }
        }
        stage('Artifact') {
            steps {
                sh 'echo finishing'
            }
        }
    }
}
