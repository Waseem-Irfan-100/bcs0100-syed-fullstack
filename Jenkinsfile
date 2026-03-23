pipeline {
    agent any

    environment {
        USERNAME = "2023bcs0100syedwaseemirfan"
        TAG = "100_2023bcs0100"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Waseem-Irfan-100/bcs0100-syed-fullstack.git'
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
                sh 'docker login -u $USERNAME -p Sirmv@123'
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
