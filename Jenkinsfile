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
        stage('Desplegar') {
            steps {
                sshagent(['Credenciales-ID']) {
                    sh """
                    ssh maquinapruebas@192.168.0.13 'docker stop cuenta-regresiva || true'
                    ssh maquinapruebas@192.168.0.13 'docker rm cuenta-regresiva || true'
                    scp cuenta-regresiva.tar maquinapruebas@192.168.0.13:/tmp
                    ssh maquinapruebas@192.168.0.13 'docker load < /tmp/cuenta-regresiva.tar'
                    ssh maquinapruebas@192.168.0.13 'docker run -d -p 5000:5000 cuenta-regresiva'
                    """
                }
            }
        }
    }
}
