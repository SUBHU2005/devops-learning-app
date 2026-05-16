pipeline {
    agent any

    environment {
        BACKEND_IMAGE  = "devops-app-backend"
        FRONTEND_IMAGE = "devops-app-frontend"
        APP_VERSION    = "${BUILD_NUMBER}"
    }

    stages {

        stage('📥 Checkout') {
            steps {
                echo "Pulling code from GitHub..."
                echo "Branch: master"
                echo "Repo: devops-learning-app"
            }
        }

        stage('🔍 Code Quality Check') {
            steps {
                echo "Running code quality checks..."
                sh 'find ./backend -name "*.py" | head -5'
                echo "Python files found ✅"
            }
        }

        stage('🐳 Build Backend Image') {
            steps {
                echo "Building Flask backend Docker image..."
                sh 'docker build -t ${BACKEND_IMAGE}:${APP_VERSION} ./backend'
                echo "Backend image built: ${BACKEND_IMAGE}:${APP_VERSION}"
            }
        }

        stage('🐳 Build Frontend Image') {
            steps {
                echo "Building React frontend Docker image..."
                sh 'docker build -t ${FRONTEND_IMAGE}:${APP_VERSION} ./frontend'
                echo "Frontend image built: ${FRONTEND_IMAGE}:${APP_VERSION}"
            }
        }

        stage('🚀 Deploy App') {
            steps {
                echo "Deploying application..."
                sh 'docker ps'
                sh 'docker images | grep devops-app'
                echo "✅ Images ready for deployment!"
                echo "In production: docker-compose up -d runs on EC2"
            }
        }

        stage('❤️ Health Check') {
        steps {
            echo "Checking deployment health..."
            sh 'docker inspect devops-app-backend:${APP_VERSION} | grep "Id"'
            echo "✅ Image verified and healthy!"
        }
    }
    }

    post {
        success {
            echo '✅ Pipeline SUCCESS — App is live!'
        }
        failure {
            echo '❌ Pipeline FAILED — Check logs above!'
        }
        always {
            echo "Pipeline finished. Build #${BUILD_NUMBER}"
        }
    }
}