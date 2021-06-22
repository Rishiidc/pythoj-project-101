import dropbox
import os

class TransferData:
    def __init__(self,access_token):
        self.accesstoken = access_token
    def upload_file(self,sourcefile,file_to):
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=writeMode('overwrite'))

def main():
    access_token = "sl.Ay-9VWXIk8lVDj09I8wmPZiIM-V1KhxW6Q5WZosKIsijz5wZBnvnE0kjcRqQmbjXmyIBCTG12SVlVu4kR1hHahFQpzR8yjGmvSn3Hv_u8aE9TZ2qTU3fAWyZvABt5uvmKc9PGWYzAaM"
    transferData = TransferData(access_token)
    file_from = input("Enter the name of the file")
    file_to = input("Enter the destination")
    transferData.upload_file(file_from,file_to)

if __name__ == "__main__":
    main()


