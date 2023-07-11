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
                pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
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
