pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                echo 'Build Docker Image'
                bat 'docker build -t myapp:latest .'
            }
        }
        stage('Login'){
            steps{
                echo 'Login to DockerHub account'
                bat 'docker login -u kaching437 -p riddle6diddle!'
            }
        }
        stage('Push'){
            steps{
                echo 'Push Docker Image to DockerHub'
                bat 'docker tag myapp:latest kaching437/myapp:latest'
                bat 'docker push kaching437/myapp:latest'
            }
        }
        stage('Deploy'){
            steps{
                echo 'Deploy the image to kubernetes'
                bat 'kubectl apply -f deployment.yaml validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
    post{
        success{
            echo 'Build was successful'
        }
        failure{
            echo 'Build failed. Check logs for more details.'
        }
    }
}