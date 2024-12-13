pipeline {
    environment {
        githubCredential = 'GITHUB'
    }
    agent any
    stages {
        
        stage('checkout') {
                steps {
                git branch: 'aws-python-flask-db',
                credentialsId: githubCredential,
                url: 'https://github.com/shreenivask/python-jenkins.git'
                }
        }
        
        stage ('Clean Up') {
            steps{
                sh returnStatus: true, script: 'docker stop $(docker ps -a | grep aws-python-flask | awk \'{print $1}\')'
                sh returnStatus: true, script: 'docker rmi $(docker remove | grep aws-python-flask | awk \'{print $1}\')'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh label: '', script: "docker-compose build --no-cache"
            }
        }

        stage('Run Docker Image') {
            steps {
                sh label: '', script: "docker-compose up -d"
            }
        }

        stage('Check Images') {
            steps {
                sh label: '', script: "docker-compose ps"
            }
        }
    }

}
