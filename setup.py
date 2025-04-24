from setuptools import setup, find_packages

setup(
    name="bitetrack",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask==2.0.1',
        'flask-sqlalchemy==2.5.1',
        'flask-login==0.5.0',
        'flask-wtf==0.15.1',
        'gunicorn==20.1.0',
        'python-dotenv==0.19.0',
        'Werkzeug==2.0.1',
        'SQLAlchemy==1.4.23',
        'WTForms==2.3.3',
        'email-validator==1.1.3',
        'psycopg2-binary==2.9.1',
    ],
    python_requires='>=3.11.0',
) 