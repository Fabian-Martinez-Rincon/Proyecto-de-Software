def list_issues():
    """List all issues."""
    issues = [ # Consultas a la base de datos
        {
            'id': 1,
            'email': 'fede@gmail.com',
            'description': 'This is a test issue',
            'status': 'new'
        },{
            'id': 2,
            'email': 'sof@gmail.com',
            'description': 'This is a test issue',
            'status': 'new'
        }]
    return issues

# Esto despues se deberia cambiar por la consulta a la base de datos 
# que traiga la informacion