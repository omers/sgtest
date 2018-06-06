pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'This stage will be executed first.'
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
