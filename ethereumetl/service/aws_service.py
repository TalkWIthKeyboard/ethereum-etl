import subprocess


class AWSService:

    def __init__(self, s3_bucket: str):
        self.s3_bucket = s3_bucket

    def copy_dict_to_s3(self, output_path: str):
        self.exec_command(f'aws s3 sync {output_path} s3://{self.s3_bucket}/ethereumetl/export')

    @staticmethod
    def exec_command(command: str):
        p = subprocess.Popen(command, shell=True)
        return_code = p.wait()
        assert (return_code == 0)
