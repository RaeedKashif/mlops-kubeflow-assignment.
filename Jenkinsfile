pipeline {
    agent any

    environment {
        VENV_PATH = "venv"
    }

    stages {

        // ------------------------
        stage('Environment Setup') {
            steps {
                echo "Setting up Python environment..."
                // Checkout code
                checkout scm
                // Create virtual environment
                bat 'python -m venv venv'
                // Upgrade pip and install dependencies
                bat 'call venv\\Scripts\\pip install --upgrade pip'
                bat 'call venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        // ------------------------
        stage('Run MLflow Pipeline') {
            steps {
                echo "Running MLflow pipeline..."
                // Run your MLflow pipeline script
                bat 'call venv\\Scripts\\python pipeline_runner.py'
            }
        }

        // ------------------------
        stage('Verify Outputs') {
            steps {
                echo "Verifying pipeline outputs..."
                // Check if model artifact exists
                bat 'if exist models\\rf_model.joblib (echo Model exists) else (echo Model missing & exit 1)'
                // Check if metrics file exists
                bat 'if exist models\\metrics.txt (echo Metrics exists) else (echo Metrics missing & exit 1)'
            }
        }
    }

    post {
        success {
            echo "MLflow pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs for errors."
        }
    }
}
