pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = '2023bcs0100syedwaseemirfan'
        ROLL = '2023bcs0100'
        TAG = "${env.BUILD_NUMBER}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                sh """
                docker build -t ${DOCKER_HUB_USER}/${ROLL}_frontend:${TAG} ./frontend
                docker build -t ${DOCKER_HUB_USER}/${ROLL}_backend:${TAG} ./backend

                docker tag ${DOCKER_HUB_USER}/${ROLL}_frontend:${TAG} ${DOCKER_HUB_USER}/${ROLL}_frontend:latest
                docker tag ${DOCKER_HUB_USER}/${ROLL}_backend:${TAG} ${DOCKER_HUB_USER}/${ROLL}_backend:latest
                """
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub_creds', 
                    usernameVariable: 'USER', 
                    passwordVariable: 'PASS'
                )]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push Images to Docker Hub') {
            steps {
                sh """
                docker push ${DOCKER_HUB_USER}/${ROLL}_frontend:${TAG}
                docker push ${DOCKER_HUB_USER}/${ROLL}_frontend:latest

                docker push ${DOCKER_HUB_USER}/${ROLL}_backend:${TAG}
                docker push ${DOCKER_HUB_USER}/${ROLL}_backend:latest
                """
            }
        }

        stage('Verify Images') {
            steps {
                sh 'docker images'
            }
        }
    }

    post {
        always {
            sh 'docker logout'
            cleanWs()
        }

        success {
            echo 'Pipeline executed successfully! Images pushed to Docker Hub.'
        }

        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
