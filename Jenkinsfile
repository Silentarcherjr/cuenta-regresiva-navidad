pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Silentarcherjr/cuenta-regresiva-navidad.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t cuenta-regresiva .'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool name: 'SonarQube Scanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                    withSonarQubeEnv('SonarQube') {
                        sh """
                        ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=sqp_80f8be90db3a63d30ab99b62ee61dd505cbc727f \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://192.168.0.11:9000 \
                            -Dsonar.login=sqa_02ce0b4ab95aa6b29d84c5efb6d889569a6f6bc7
                        """
                    }
                }
            }
        }
    }
}

