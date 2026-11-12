# EL6: Comparing Traditional, Microservices, and Serverless Deployments

This lab implements the same Student Information request using three deployment models:

1. **Traditional:** one Flask application.
2. **Microservices:** a Student Service and a Gateway Service running separately.
3. **Serverless:** an AWS Lambda function tested from the AWS Console.

The lab compares deployment units, execution, scaling responsibility, operational work, and failure behavior.

## Objectives

- Run a student endpoint in a traditional Flask application.
- Split the same request across two local Flask services.
- Observe how the Gateway responds when the Student Service is unavailable.
- Deploy and test the same request using AWS Lambda.
- Compare the three deployment models.

## Architecture

```text
Traditional:
Browser ──> Flask application ──> Student JSON

Microservices:
Browser ──> Gateway Service ──> Student Service ──> Student JSON

Serverless:
AWS Lambda Test Event ──> Lambda function ──> Student JSON
                                  │
                                  └──> CloudWatch Logs

el6-deployment-model-comparison/
├── README.md
├── traditional_app/
│   └── app.py
├── microservices/
│   ├── student_service.py
│   └── gateway.py
└── serverless/
    └── lambda_function.py
                                  
