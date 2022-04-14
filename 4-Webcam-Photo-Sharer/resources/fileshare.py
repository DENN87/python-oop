from filestack import Client


class FileShare:
    # Get api_key from www.filestack.com and added to api_key="<key>"

    def __init__(self, filepath, api_key="AffkdoQtLQeqyulzBexkVz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        """Uploads the filename from file_path to the filestack.com
        and returns the url of the image"""

        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url

