import boto3
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.conf import settings
from core.models import S3_File
from uuid import uuid4

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

    def uploadToS3(
        self,
        request=None,
        key:str=None,
        table_name: str = None,
        table_field: str = None,
        path_to_store: str = None,
    ):
        """
        Function Description:
        This function performs a specific action using the provided parameters.

        Parameters:
        - request: Django request object. (default=None)
                The Django request object associated with the current HTTP request.
        - key: str. (default=None)
            The file key used to access the file. For example, 'image'.
        - table_name: str. (default=None)
                    The name of the table where the file will be stored. For example, 'S3 Upload'.
        - table_field: str. (default=None)
                    The name of the field in the table where the file will be stored. For example, 's3 file'.
        - path_to_store: str. (default=None)
                        The path in the storage system where the file will be stored. For example, '/user/files'.
        """
        if not settings.AWS_ENABLE:
            raise ValueError("Can't upload to S3. S3 is turned off")
        if not request:
            raise ValueError("request is required")
        if not key:
            raise ValueError("key is required")
        if not table_name:
            raise ValueError("table_name is required")
        if not table_field:
            raise ValueError("table_field is required")
        if not table_field:
            raise ValueError("table_field is required")
        if not path_to_store:
            raise ValueError("path_to_store is required")
        file = request.FILES[key]
        user_id = request.user.id
        module_name = request.resolver_match.func.__module__
        app_name = module_name.split(".")[0]
        file_name = file.name
        make_path = ""
        for path in path_to_store.split("/"):
            if path:
                make_path += path+"/"
        make_path+= f"{str(uuid4())}/{file_name}"
        buffer = io.BytesIO()
        for chunk in file.chunks():
            buffer.write(chunk)
        buffer.seek(0)
        content_file = ContentFile(buffer.getvalue())
        in_memory_file = InMemoryUploadedFile(
            content_file, None, make_path, None, None, None
        )
        s3ObjectUrl = self.__s3_upload(in_memory_file, make_path)
        url = s3ObjectUrl
        s3file_model = S3_File.objects.create(
            url=url,
            file_path=make_path,
            file_name=file_name,
            app_name=app_name,
            table_name=table_name,
            table_field=table_field,
            user_id=user_id,
        )
        s3file_model.save()
        return s3file_model




    def get_s3File(self, s3_id):
        """
        This function will return the http response of the file directly
        """
        if not settings.AWS_ENABLE:
            raise ValueError("Can't upload to S3. S3 is turned off")
        if not s3_id:
            raise ValueError("s3_id is required")
        s3_object = S3_File.objects.get(pk=s3_id)
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
        try:
            response = s3_client.get_object(Bucket=bucket_name, Key=s3_object.file_path)
            file_content = response["Body"].read()
            if file_content:
                response = HttpResponse(file_content, content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{s3_object.file_name}"'
                return response
        except Exception as e:
            raise Exception("File not found or error occurred while downloading.")

