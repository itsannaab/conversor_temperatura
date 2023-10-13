pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/itsannaab/conversor_temperatura.git']])
            }
        }
        stage('Build') {
            steps {
                bat 'python3 converter.py'
            }
        }
    }
}
