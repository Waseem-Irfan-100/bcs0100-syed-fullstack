pipeline {
    agent any

    environment {
        USERNAME = "2023bcs0100syedwaseemirfan"
        TAG = "100_2023bcs0100"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Build Backend Image') {
            steps {
                sh 'docker build -t $USERNAME/${TAG}_backend ./backend'
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh 'docker build -t $USERNAME/${TAG}_frontend ./frontend'
            }
        }

        stage('Docker Login') {
            steps {
                sh 'docker login -u $USERNAME -p YOUR_PASSWORD'
            }
        }

        stage('Push Images') {
            steps {
                sh 'docker push $USERNAME/${TAG}_backend'
                sh 'docker push $USERNAME/${TAG}_frontend'
            }
        }
    }
}