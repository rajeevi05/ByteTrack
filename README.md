# BiteTrack

BiteTrack is a comprehensive meal planning and nutrition tracking application built with Flask. It features an interactive dashboard for meal planning, nutrition analytics, and health monitoring.

## Features

- Interactive dashboard with meal planning
- Nutrition analytics and charts
- Weight progress tracking
- Food allergy alerts
- Meal generation based on preferences
- User authentication system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bitetrack.git
cd bitetrack
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

## Running the Application

1. Set the Flask environment variables:
```bash
set FLASK_APP=bitetrack.app
set FLASK_ENV=development
```

2. Run the application:
```bash
flask run
```

The application will be available at `http://localhost:5000`

## Project Structure

```
bitetrack/
├── app.py              # Main application file
├── static/            # Static files (CSS, JS)
│   ├── css/
│   └── js/
└── templates/         # HTML templates
    ├── base.html
    ├── dashboard.html
    └── analytics.html
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Deployment Options

### 1. Deploy to Render (Recommended)

1. Create a [Render](https://render.com) account
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Fill in the details:
   - Name: bitetrack
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn -c gunicorn_config.py 'bitetrack.app:app'`
5. Click "Create Web Service"

### 2. Deploy to Railway

1. Create a [Railway](https://railway.app) account
2. Click "New Project" and select "Deploy from GitHub repo"
3. Select your repository
4. Railway will automatically detect your Python app
5. Add the following environment variables:
   - `FLASK_ENV=production`
   - `SECRET_KEY=your-secret-key`

### 3. Deploy to PythonAnywhere

1. Create a [PythonAnywhere](https://www.pythonanywhere.com) account
2. Go to the Web tab and click "Add a new web app"
3. Choose Manual Configuration and Python 3.9
4. Set up your virtual environment:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.9 myenv
   pip install -r requirements.txt
   ```
5. Configure your WSGI file according to PythonAnywhere's instructions

## Environment Variables

Make sure to set these environment variables in your deployment platform:

- `FLASK_ENV`: Set to 'production'
- `SECRET_KEY`: Your secret key for Flask
- `DATABASE_URL`: Your database URL (if using external database)

## Database Setup

The application uses SQLite by default, but for production, it's recommended to use PostgreSQL:

1. Create a PostgreSQL database in your deployment platform
2. Set the `DATABASE_URL` environment variable
3. The application will automatically use the PostgreSQL database in production

## Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python -m flask run
```

## Features

- User authentication
- Meal tracking
- Nutrition analytics
- Progress monitoring
- Meal planning
- Interactive dashboard 