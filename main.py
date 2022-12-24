import cv2
import sys
import time
from seat_status import *
from photo import *


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

def main():
  while True:
    takePhoto()
    folder_name = 'f1'
    final_df = load_images_from_folder(folder_name)
    final_df = final_df.astype(int)
    final_df = final_df.sort_values(by=['Camera Number', 'Chair Number'], ascending=True)
    final_df.to_csv('seat_status.csv', index = False)
    time.sleep(240)
