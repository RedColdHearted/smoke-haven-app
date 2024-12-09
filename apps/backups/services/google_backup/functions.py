import datetime
import glob

from django.core.management import call_command

from pydrive2.auth import GoogleAuth, ServiceAccountCredentials
from pydrive2.drive import GoogleDrive
from pydrive2.files import GoogleDriveFile

from dotenv import dotenv_values

config = dotenv_values(".env")

SERVICE_ACCOUNT_PATH = "apps/backups/services/google_backup/service-secrets.json"
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
        SERVICE_ACCOUNT_PATH,
        scopes=DRIVE_SCOPES,
    )
    gauth.ServiceAuth()
    return gauth


def create_folder(
    drive: GoogleDrive,
    title: str,
    parent_folder_id: str = "root",
) -> GoogleDriveFile:
    file_metadata = {
        'title': title,
        'parents': [
            {'id': parent_folder_id},
            ],
        'mimeType': 'application/vnd.google-apps.folder'
    }

    folder = drive.CreateFile(file_metadata)
    folder.Upload()
    return folder


def upload_file(drive: GoogleDrive, file_path: str, parent_folder_id: str) -> None:
    file_drive = drive.CreateFile(
        {
        'title': file_path,
        'parents': [
            {'id': parent_folder_id},
            ],
        },
    )
    file_drive.SetContentFile(file_path)
    file_drive.Upload()


def files_list(drive: GoogleDrive, folder_id: str) -> list[GoogleDriveFile]:
    return drive.ListFile(
        {'q': f"'{folder_id}' in parents and trashed=false"},
    ).GetList()


def clean_folder(drive: GoogleDrive, folder_id: str) -> None:
    for file in files_list(drive, folder_id):
        file.Delete()


def upload_media_dir(drive: GoogleDrive, parent_folder_id: str) -> None:
    for file_path in glob.glob(MEDIA_DIR_GLOB):
        upload_file(drive, file_path, parent_folder_id)


def create_db_dump() -> None:
    with open(DEFAULT_DUMP_PATH,'w') as output:
        call_command('dumpdata',format='json',indent=3,stdout=output)


def load_db_dump() -> None:
    with open(DEFAULT_DUMP_PATH, 'r+') as input:
        call_command('loaddata', stdin=input)


def backup() -> GoogleDriveFile:
    gauth = authenticate_service_account(GoogleAuth())
    drive = GoogleDrive(authenticate_service_account(gauth))
    create_db_dump()
    backup_folder = create_folder(
        drive,
        f"backup_{datetime.datetime.now()}",
        DRIVE_FOLDER_ID,
    )
    upload_file(drive, DEFAULT_DUMP_PATH, backup_folder["id"])
    upload_media_dir(drive, backup_folder["id"])
    return backup_folder
