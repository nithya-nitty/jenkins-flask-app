pipeline {
    triggers {
        pollSCM 'H/10 * * * *'
    }
    
    environment {
        imageName = "nithyanittyy/hello-flask"
        dockerCredentials = "dockerhub_account"
        dockerImage = ""
    }

    agent any

    stages {
        stage("Code Checkout") {
            steps {
                git branch: 'main', url: 'https://github.com/nithya-nitty/jenkins-flask-app.git'
            }
        }

        stage("Build Docker Image") {
            steps {
                script {
                    dockerImage = docker.build imageName + ":$BUILD_NUMBER" 
                }
            }
        }

        stage("Push Docker Image") {
            steps {
                script {
                    docker.withRegistry('', dockerCredentials) {
                        dockerImage.push()
                    }
                }
            }
        }

        stage("Clean Up") {
            steps {
                sh "docker image rm $imageName:$BUILD_NUMBER"
            }

            post {
                success {
                    echo "Docker Image Pushed Successfully - $imageName:$BUILD_NUMBER"
                }
                failure {
                    echo "Build failed... Figure out what's going wrong :)"
                }
            }
        }
    }
}
