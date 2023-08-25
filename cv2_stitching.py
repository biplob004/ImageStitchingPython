import cv2, os

folder_name = 'frames'
image_paths= sorted([f'{folder_name}/{x}' for x in os.listdir(f'./{folder_name}')])
print(image_paths)
imgs = []

for i in range(len(image_paths)):
	imgs.append(cv2.imread(image_paths[i]))
	imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)



stitchy=cv2.Stitcher.create()
# stitchy.setPanoConfidenceThresh(0.1) 
(dummy,output)=stitchy.stitch(imgs)

# check stiching done successfully
if dummy != cv2.STITCHER_OK:
	print("stitching ain't successful")
else:
	print('Your Panorama is ready!!!')

	# final output
	cv2.imshow('final result',output)
	cv2.imwrite('cv2_s_1.jpeg', output)
	cv2.waitKey(5000)



