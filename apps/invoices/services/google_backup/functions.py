import glob

from django.core.management import call_command

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from pydrive2.auth import ServiceAccountCredentials

from dotenv import dotenv_values

config = dotenv_values(".env")

SERVICE_ACCOUNT_FILE = "apps/invoices/services/google_backup/service-secrets.json"
DRIVE_SCOPES = (
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive.appdata",
    "https://www.googleapis.com/auth/drive.appfolder",
    )
DRIVE_FOLDER_ID = config.get("DRIVE_FOLDER_ID")
MEDIA_DIR_GLOB = "media/*/*/*/*/*"
DEFAULT_DUMP_PATH = "db_dump.json"


def authenticate_service_account(gauth: GoogleAuth) -> GoogleAuth:
    gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(
        SERVICE_ACCOUNT_FILE,
        scopes=DRIVE_SCOPES,
    )
    gauth.ServiceAuth()
    return gauth


def upload_file(drive: GoogleDrive, file_path) -> None:
    file_drive = drive.CreateFile(
        {
        'title': file_path,
        'parents': [
            {'id': DRIVE_FOLDER_ID},
            ],
        },
    )
    file_drive.SetContentFile(file_path)
    file_drive.Upload()


def upload_media_dir(drive: GoogleDrive) -> None:
    for file_path in glob.glob(MEDIA_DIR_GLOB):
        upload_file(drive, file_path)


def create_db_dump() -> None:
    with open(DEFAULT_DUMP_PATH,'w') as output:
        call_command('dumpdata',format='json',indent=3,stdout=output)


def load_db_dump() -> None:
    with open(DEFAULT_DUMP_PATH, 'r+') as input:
        call_command('loaddata', stdin=input)


def backup():
    gauth = authenticate_service_account(GoogleAuth())
    drive = GoogleDrive(authenticate_service_account(gauth))
    create_db_dump()
    upload_file(drive, DEFAULT_DUMP_PATH)
    upload_media_dir(drive)
