from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os.path

# Escopos necessários para acessar a Google Classroom API
SCOPES = ['https://www.googleapis.com/auth/classroom.rosters.readonly']

def main():
    # Autenticação
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '725871482028-nnfu338mjc2e5f2etqass24f2frmfirc.apps.googleusercontent.com', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Conectando à API do Google Classroom
    service = build('classroom', 'v1', credentials=creds)

    # ID da turma específica que você deseja consultar
    course_id = 'https://meet.google.com/psu-hiix-toy'

    # Requisitando a lista de alunos
    results = service.courses().students().list(courseId=course_id).execute()
    students = results.get('students', [])

    # Exibindo a quantidade de alunos
    print(f"Número de alunos na turma {course_id}: {len(students)}")

if __name__ == '__main__':
    main()