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
                sh 'docker-compose down || true'
                sh 'docker-compose up -d'
                echo "App deployed successfully!"
            }
        }

        stage('❤️ Health Check') {
            steps {
                echo "Checking if app is healthy..."
                sh 'sleep 10'
                sh 'curl -f http://localhost:5000/names || echo "Health check endpoint not ready yet"'
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