import boto3
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.conf import settings
from core.models import S3_File


class FileService:
    """
    This service is to handel File model and S3 object storage
    """

    def __s3_upload(self, InmemoryFile=None, path_to_store=None):
        s3url = settings.AWS_URL
        bucket_name = settings.S3_BUCKETNAME
        access_key = settings.S3_ACCESSKEY
        secret_key = settings.S3_SECRETKEY
        s3_client = boto3.client(
            "s3",
            endpoint_url=s3url,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )
        s3_client.upload_fileobj(InmemoryFile, bucket_name, path_to_store)
        object_url = f"{s3url}/{bucket_name}/{path_to_store}"
        return object_url

    def upload(
        self,
        user_id: int = None,
        app_name: str = None,
        table_name: str = None,
        table_field: str = None,
        file=None,
        path_to_store: str = None,
    ):
        """
        user_id : User ID: Send the user ID as an integer value using the user_id parameter.
            This parameter is required and ensures that the file upload is associated with a specific user in the system.

        app_name : Application Name: Specify the application name using the app_name parameter. 
            This parameter helps in identifying the application context in which the file upload is performed.
            For example, you can specify the application name as "core" if the upload is related to the core functionalities of 
            the system.

        table_name : Table Name: Provide the table name using the table_name parameter. 
            This parameter indicates the name of the table or entity to which the file is attached. 
            It helps in tracking the files based on the entities they are associated with. 
            For instance, if the file is related to user profiles, you can specify the table name as "Profile".
        
        
        table_field : Table Field: Specify the table field name using the table_field parameter. 
            This parameter represents the specific field within the table where the file is stored or referenced. 
            It facilitates easy retrieval and management of files associated with different fields. For example, 
            if the file is a user's profile picture, you can specify the table field as "profile_pic".
        
        file : File: Send the file object using the file parameter. 
            You can retrieve the file object from the request using request.FILES.get("image"). 
            This parameter contains the actual file data that you want to upload to the system.
        
        path_to_store : Path to Store: Specify the path where you want to store the file along with the file name 
            using the path_to_store parameter. This parameter allows you to specify the directory structure and file name for 
            storing the uploaded file. For example, you can specify the path as "profile/file.txt" 
            to store the file in the "profile" directory with the name "file.txt".
        """
        if not settings.AWS_ENABLE:
            raise ValueError("Can't upload to S3. S3 is turned off")
        if not user_id:
            raise ValueError("user_id is required")
        if not app_name:
            raise ValueError("app_name is required")
        if not table_name:
            raise ValueError("table_name is required")
        if not table_field:
            raise ValueError("table_field is required")
        if not table_field:
            raise ValueError("table_field is required")
        if not file:
            raise ValueError("file is required")
        if not path_to_store:
            raise ValueError("path_to_store is required")

        buffer = io.BytesIO()
        for chunk in file.chunks():
            buffer.write(chunk)
        buffer.seek(0)
        content_file = ContentFile(buffer.getvalue())
        in_memory_file = InMemoryUploadedFile(
            content_file, None, path_to_store, None, None, None
        )
        s3ObjectUrl = self.__s3_upload(in_memory_file, path_to_store)
        url = s3ObjectUrl
        app_name = app_name
        table_name = table_name
        table_field = table_field
        user_id = user_id
        s3file_model = S3_File.objects.create(
            url=url,
            app_name=app_name,
            table_name=table_name,
            table_field=table_field,
            user_id=user_id,
        )
        s3file_model.save()
        return s3file_model
