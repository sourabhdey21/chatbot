# Geminibot

A Kubernetes-based application deployment with auto-scaling capabilities.

## Project Structure

```
k8s/
├── deployment.yaml    # Main application deployment configuration
├── service.yaml      # Service configuration for internal communication
├── ingress.yaml      # Ingress configuration for external access
├── namespace.yaml    # Kubernetes namespace configuration
└── hpa.yaml         # Horizontal Pod Autoscaler configuration
```

## Prerequisites

- Kubernetes cluster (v1.19 or later)
- kubectl configured to communicate with your cluster
- Docker image of the application built and available in your registry

## Configuration Files

### Namespace
- Creates a dedicated `geminibot` namespace
- Provides isolation for the application resources

### Deployment
- Runs 2 replicas by default
- Container port: 8000
- Resource limits:
  - CPU: 200m
  - Memory: 512Mi
- Resource requests:
  - CPU: 100m
  - Memory: 256Mi

### Service
- Type: ClusterIP
- Port: 80
- Target Port: 8000

### Ingress
- Host: geminibot.local (configurable)
- Path: /
- Backend: geminibot-service

### Horizontal Pod Autoscaler (HPA)
- Min replicas: 2
- Max replicas: 10
- Target CPU utilization: 80%

## Deployment Instructions

1. Create the namespace:
```bash
kubectl apply -f k8s/namespace.yaml
```

2. Deploy the application:
```bash
kubectl apply -f k8s/deployment.yaml
```

3. Create the service:
```bash
kubectl apply -f k8s/service.yaml
```

4. Set up the ingress:
```bash
kubectl apply -f k8s/ingress.yaml
```

5. Configure auto-scaling:
```bash
kubectl apply -f k8s/hpa.yaml
```

## Verification

Check the status of your deployment:
```bash
kubectl get all -n geminibot
```

Monitor the HPA:
```bash
kubectl get hpa -n geminibot
```

## Customization

1. Update the image in `deployment.yaml` with your actual image name and tag
2. Adjust resource limits and requests in `deployment.yaml` based on your needs
3. Modify the ingress host in `ingress.yaml` to match your domain
4. Adjust HPA parameters in `hpa.yaml` if different scaling behavior is required

## Maintenance

To update the deployment:
```bash
kubectl set image deployment/geminibot-deployment geminibot=<new-image> -n geminibot
```

To scale manually (if needed):
```bash
kubectl scale deployment geminibot-deployment --replicas=<number> -n geminibot
```

## Troubleshooting

Check pod logs:
```bash
kubectl logs -f deployment/geminibot-deployment -n geminibot
```

Describe resources for detailed information:
```bash
kubectl describe deployment geminibot-deployment -n geminibot
kubectl describe service geminibot-service -n geminibot
kubectl describe ingress geminibot-ingress -n geminibot
```

# Gemini Chat Bot

![Dashboard](screenshots/dashboard.png)

A modern web-based chat interface for interacting with Google's Gemini AI model.

## Features

- Beautiful and responsive web interface
- Real-time chat with Gemini AI
- Typing indicators
- Error handling
- Mobile-friendly design
- Modern UI with Tailwind CSS

## Setup

1. **Create a `.env` file in your project root with your Gemini API key:**

```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the web application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:8000
```

## Usage

- Type your questions or prompts in the input field
- Press Enter or click the Send button to get responses from Gemini
- The chat interface will maintain the conversation history
- Messages are displayed in a modern chat-like interface

## Technical Details

- Built with Flask for the backend
- Uses Tailwind CSS for styling
- Implements real-time typing indicators
- Responsive design that works on all devices
- Error handling for both frontend and backend

## Note

This bot uses the Gemini Pro model, which is capable of handling various types of queries including:
- General knowledge questions
- Code explanations
- Creative writing
- Problem-solving
- And much more! 