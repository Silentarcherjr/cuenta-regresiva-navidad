pipeline {
    agent any
    stages {
        stage('Clonar Repositorio') {
            steps {
                git 'https://github.com/Silentarcherjr/cuenta-regresiva-navidad.git'
            }
        }
        stage('Construir') {
            steps {
                sh 'docker build -t cuenta-regresiva .'
            }
        }
        stage('Ejecutar') {
            steps {
                sh 'docker run -d -p 5000:5000 cuenta-regresiva'
            }
        }
    }
}
