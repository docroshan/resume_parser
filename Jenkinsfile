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
                pip install -r requirements.txt
                python -m spacy download en_core_web_sm
                python -m nltk.downloader words
                python --version
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing..."
                sh '''
                python demo.py
                '''
            }
        }
    }
}
