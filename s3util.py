import boto3


class s3wrapper(object):
    def __init__(self, bucket,directory):
        self.bucket=bucket
        self.directory=directory
        self.s3 = boto3.resource('s3')
    def upload(self,name,file):
        self.s3.Bucket(self.bucket).put_object(Key=self.directory+name, Body=file)
    def delete(self,name):
        objs = self.s3.Bucket(self.bucket).objects.filter(Prefix=self.directory)
        for obj in objs:
            if name in obj.key:
                print("deleting "+obj.key)
                obj.delete()
    def all(self,prefix="/images"):
        res = []
        objs = list(self.s3.Bucket(self.bucket).objects.filter(Prefix=prefix))
        for obj in objs:
            res.append(obj.key)
        return res
        