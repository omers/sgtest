pipeline {
    agent any
    environment {
        VERSION = '1.1.1'
    }
    stages {
        stage('Clone') {
            steps {
                git url:'https://github.com/omers/sgtest.git', changelog: true
            }
        }
        stage('Build') {
            steps {
                sh '. ~/venvs/SGApp/bin/activate && pip3 install -r requirements.txt'
                sh 'docker build -t sgapp:${VERSION} -f Deployment/Dockerfile .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -d -p 5000:5000 --rm --name sgapp sgapp:${VERSION}'
            }
        }
        stage('Test') {
            steps {
                sleep(5)
                /* sh '. ~/venvs/SGApp/bin/activate && cd IntegrationTests && pytest --junit-xml=reports/junit.xml TestSuite.py' */
            }
        }
        stage('Deploy') {
            steps {
                input "Does the staging environment look ok?"
            }
        }
    }
    post {
        always {
            archiveArtifacts '**/reports/*.xml'
            junit '**/reports/*.xml'
            sh 'docker stop sgapp'
        }
        success {
            echo 'I succeeeded!'
        }
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            echo 'I failed :('
        }
        changed {
            echo 'Things were different before...'
        }
    }
}
