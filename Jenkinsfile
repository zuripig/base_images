
pipeline {
    agent any
    
    environment {
        FILE_NAME = "scan_${BUILD_NUMBER}"
                }
    stages {
        stage('zip') {
            steps {
                sh 'echo zipping'
                sh 'zip -r python.zip ./*.py'
                  }
        }
    }
}
