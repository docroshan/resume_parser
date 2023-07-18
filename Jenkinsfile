pipeline {
    agent { 
        node {
            label 'docker-agent-py'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building..."
                sh '''
                echo "Installing packages"
                pip install nltk
                pip install pyresparser
                python -m nltk.downloader stopwords
                python --version
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing..."
                sh '''
                python test.py
                '''
            }
        }
    }
}
