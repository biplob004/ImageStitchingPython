# pip install largestinteriorrectangle

import stitching, os, cv2

folder_name = 'frames'
img_list= sorted([f'{folder_name}/{x}' for x in os.listdir(f'./{folder_name}')])

# If you do not have a GPU set try_use_gpu=False
stitcher = stitching.Stitcher(try_use_gpu=True, confidence_threshold=0.6)
panorama = stitcher.stitch(img_list)


cv2.imwrite('stch_out_1.jpeg', panorama)






