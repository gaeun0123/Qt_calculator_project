# file save and read
import os
from datetime import datetime, timedelta

class File:
    def __init__(self):
        self.path = "/home/addinedu/cal_result.txt"

    

    def createDirectory(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print("Error: Failed to create the directory.")

    
    
    def addText(self, dataList):
        # 파일 경로에서 디렉토리 경로 추출
        directory = os.path.dirname(self.path)
        
        self.createDirectory(directory)
                                                                                                                                                                                                                                                                                    
        with open(self.path, "a") as file:
            file.writelines(dataList)

        print("file save complete!")

