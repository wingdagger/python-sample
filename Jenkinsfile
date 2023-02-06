pipeline {
    agent none 
    stages {
        stage('Prep') { 
            agent {
                docker {
                    image 'python:3.10' 
                }
            }
            steps {
                echo "Starting Build Stage"
                git branch: 'main', url: 'https://github.com/wingdagger/python-sample.git'
                echo "Downloaded code from Github"
                stash(name: 'src', includes: '*') 
            }
        }
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.10' 
                }
            }
            steps {
                echo "Starting Build Stage"
                echo 'Starting Build'
                sh './build.sh' 
                echo "Done with Build"
                stash(name: 'compiled-results', includes: 'dist/*.whl') 
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh './run-tests.sh'
            }
        }        
   }
}