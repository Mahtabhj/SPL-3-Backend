pipeline {
    agent {
        node {
            label 'wafr'
        }
    }        
    stages{
        stage('Build') {
            steps {
                sh "docker-compose down"
            }
        }        
        stage('Deploy') {
            steps {
                // Define the credentials for AWS access
                withCredentials([
                    [ $class: 'AmazonWebServicesCredentialsBinding', accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY', credentialsId: 'aws-credentials-id' ]
                ]) {
                    sh "docker-compose build"
                    sh "docker-compose up -d"
                }
            }
        }
    }
}
