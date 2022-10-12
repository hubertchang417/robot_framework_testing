import os
class Custom_NASInfo:
    ROBOT_LIBRARY_SCOPE = 'SUITE'
    def __init__(self) -> None:
        self.path=""
    @property
    def path(self):
        return self._path
    @path.setter
    def path(self, file_path):
        self._path = file_path
    def set_path(self):
        self.path = os.path.abspath(os.getcwd())
    def create_myfile(self,file_name):
        self._file=f'{self.path}/{file_name}.txt'
        open(self._file,'w')
    def write_msg(self,lists):
        with open(self._file,'w') as f:
            #f.write(f'total msg is {len(lists)}')
            for key, msg in lists.items():
                f.write(f'{key} : {msg}\n')


