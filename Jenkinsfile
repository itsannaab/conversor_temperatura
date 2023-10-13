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
                git branch: 'main', url: 'https://github.com/itsannaab/conversor_temperatura'
                bat 'py converter.py'
            }
        }
        stage('Test') {
            steps {
                bat 'py -m pip install -r requirements.txt'  
                bat 'py -m pytest'
            }
        }
    }
}
