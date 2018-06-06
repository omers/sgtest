pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                git 'https://github.com/omers/sgtest.git'
            }
        }
        stage('Test') {
            steps {
               sh 'echo "Pytest"'
            }
        }
	stage('Deploy') {
	   echo 'Scazal Build'
	}
    }
}
