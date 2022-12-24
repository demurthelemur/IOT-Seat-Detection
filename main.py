import cv2
import sys
import time
from seat_status import *
from photo import *

def main():
  while True:
    takePhoto()
# change folder name to: 'f1', 'f2', 'f3' to test other images
    folder_name = 'photo'
    final_df = load_images_from_folder(folder_name)

# changing type to 'int' so as to sort by camera number
    final_df = final_df.astype(int)
    final_df = final_df.sort_values(by=['Room Number', 'Chair Number'], ascending=True)

# save final_df in a csv file
    final_df.to_csv('seat_status.csv', index = False)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


