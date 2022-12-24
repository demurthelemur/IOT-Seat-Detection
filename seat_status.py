import cv2
import pandas as pd
# import matplotlib.pyplot as plt - used to make rois

import os
from object_detection import Object_detect

# CONVENTION
# rois : {"cam_num" : [
#                          [bottom_right_x, bottom_right_y, top_left_x, top_left_y]
#                    ]}
rois = {
        '1' : [ [210,255,145,160], [290,255,210,160], [270,170,210,110], [210,180,140, 85] ],
    }

# if the model only detects chairs or detects nothing at all then zoom in (search in these rois)
no_person_rois = {
     '1' : [ [210,215,150,160], [280,210,215,160], [270,165,220,120], [210,180,140,140] ],
    }  

# mapping seat status to a value
seat_status_indicator = {'empty' : 0, 'occupied' : 1, 'on hold' : 2}

# check in the smaller rois (only called when no object is detected or only chair is detected in the big ROI)
def check_table_roi(cam_num, idx, img):
    table_section = no_person_rois[cam_num][idx]
    df = Object_detect(img[table_section[3]:table_section[1],table_section[2]:table_section[0],:], confThreshold=0.3, nmsThreshold=0.5)
    if df.empty:
        status = 'empty'
    else:
        status = 'on hold'
    return status

# detect images in folder 
def load_images_from_folder(folder, roomNumber = '1'):
    final_df = pd.DataFrame(columns = ['Room Number', 'Chair Number', 'Status' ])
    filename = "Result.png"
    img = cv2.imread(os.path.join(folder, filename))
    img = cv2.resize(img , (352, 288))
    roi = rois[roomNumber]
    if img is not None:
        for idx, chair in enumerate(roi):
            print(f"Room Number: {roomNumber} \t ROI number : {idx + 1} is being processed.")
            # Initialize flag and status to default values for each chair
            flag = 0
            status = 'empty'
            
            # calling Object_detect on ROI
            df = Object_detect(img[chair[3]:chair[1],chair[2]:chair[0],:], confThreshold=0.3, nmsThreshold=0.5)

            # check if df is empty
            if df.empty:
                # print("\n\nRECHECKING\n")
                status = check_table_roi(roomNumber, idx, img)
            else:
                if 1 in df['ClassIds'].values:
                    status = 'occupied'
                else:
                    unique_vals = df['ClassIds'].unique()
                    for item in unique_vals:
                        if item not in [57,69,70,71,73,14]: # ignore chairs ( all these items have been mapped to chairs, manually by us )
                            status = 'on hold'
                            flag = 1
                            break
                    
                    if flag == 0:
                        # print("rechecking because we got only chair")
                        status = check_table_roi(roomNumber, idx, img)
            print(f"Status : {status}\n")
            final_df = final_df.append({'Room Number' : roomNumber, 'Chair Number' : idx + 1, 'Status' : seat_status_indicator[status]}, ignore_index=True)
        print("Instance complete")
        return final_df

                

# change folder name to: 'f1', 'f2', 'f3' to test other images
folder_name = 'photo'
final_df = load_images_from_folder(folder_name)

# changing type to 'int' so as to sort by camera number
final_df = final_df.astype(int)
final_df = final_df.sort_values(by=['Room Number', 'Chair Number'], ascending=True)

# save final_df in a csv file
final_df.to_csv('seat_status.csv', index = False)
