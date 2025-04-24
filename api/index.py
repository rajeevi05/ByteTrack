from flask import Flask, Response
from bitetrack.app import app
from werkzeug.middleware.proxy_fix import ProxyFix

# Add ProxyFix middleware to handle proxy headers
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

def handler(request):
    """Handle incoming HTTP requests for Vercel serverless functions."""
    try:
        # Create a test client
        with app.test_client() as client:
            # Get the path from the request
            path = request.get('path', '/')
            
            # Get the method
            method = request.get('method', 'GET')
            
            # Get headers
            headers = request.get('headers', {})
            
            # Get body for POST requests
            body = request.get('body', None)
            
            # Make the request
            response = client.open(
                path,
                method=method,
                headers=headers,
                data=body
            )
            
            # Return the response
            return {
                'statusCode': response.status_code,
                'headers': dict(response.headers),
                'body': response.get_data(as_text=True)
            }
            
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e),
            'headers': {'Content-Type': 'text/plain'}
        } 