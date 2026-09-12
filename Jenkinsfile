pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Build') {
            steps {
                bat 'echo No build step required for Python Flask application'
            }
        }
    }
}
