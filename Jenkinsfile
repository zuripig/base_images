
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
        stage('HTML Output') {
            steps {
                sh 'echo output'
            }
        }
        stage('Artifact') {
            steps {
                sh 'echo finishing'
            }
        }
    }
}
