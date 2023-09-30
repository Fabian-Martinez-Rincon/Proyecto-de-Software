def list_issues():
    """List all issues."""
    issues = [
        {
            'id': 1,
            'email': 'john.doe@example.com',
            'description': 'Unable to log in to the application.',
            'status': 'new'
        },
        {
            'id': 2,
            'email': 'sara.jones@example.com',
            'description': 'App crashes when navigating to the settings page.',
            'status': 'in-progress'
        },
        {
            'id': 3,
            'email': 'mark.smith@example.com',
            'description': 'Feature request: Add dark mode to the application.',
            'status': 'resolved'
        },
        {
            'id': 4,
            'email': 'lisa.johnson@example.com',
            'description': 'Error 404 when trying to access a specific URL.',
            'status': 'new'
        },
        {
            'id': 5,
            'email': 'peter.wilson@example.com',
            'description': 'Performance issue: Application takes too long to load.',
            'status': 'in-progress'
        },
        {
            'id': 6,
            'email': 'mary.brown@example.com',
            'description': 'Bug: Incorrect data displayed in the user profile.',
            'status': 'resolved'
        },
        {
            'id': 7,
            'email': 'alex.miller@example.com',
            'description': 'Feature request: Integrate with third-party API for weather information.',
            'status': 'new'
        },
        {
            'id': 8,
            'email': 'chris.white@example.com',
            'description': 'App freezes when attempting to upload large files.',
            'status': 'in-progress'
        },
        {
            'id': 9,
            'email': 'emily.jones@example.com',
            'description': 'Bug: Unable to delete account from profile settings.',
            'status': 'resolved'
        },
        {
            'id': 10,
            'email': 'david.taylor@example.com',
            'description': 'Feature request: Implement a chat feature within the application.',
            'status': 'new'
        }
    ]
    return issues

# Esto despues se deberia cambiar por la consulta a la base de datos 
# que traiga la informacion