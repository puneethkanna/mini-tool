import cv2 as cv
import sys, getopt

def convert(inputfile, outputfile):
	img = cv.imread(inputfile)
	img = cv.GaussianBlur(img,(3,3),0)
	# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
	# h, s, v = cv.split(hsv)
	# lim = 255 - 50
	# v[v > lim] = 255
	# v[v <= lim] += 50
	# final_hsv = cv.merge((h, s, v))
	# img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)
	cartoon_image = cv.stylization(img, sigma_s=60, sigma_r=0.25)  
	dst = cv.detailEnhance(cartoon_image, sigma_s=30, sigma_r=0.1)
	cv.imwrite(outputfile, dst) 
def live():
	video = cv.VideoCapture(0, cv.CAP_DSHOW)
	video.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
	video.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
	while(True):
		ret, frame = video.read()
		frame = cv.GaussianBlur(frame,(5,5),0)
		# hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
		# h, s, v = cv.split(hsv)
		# lim = 255 - 50
		# v[v > lim] = 255
		# v[v <= lim] += 50
		# final_hsv = cv.merge((h, s, v))
		# img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)
		cartoon_image = cv.stylization(frame, sigma_s=60, sigma_r=0.25)  
		dst = cv.detailEnhance(cartoon_image, sigma_s=30, sigma_r=0.1)
		cv.imshow('cartoon', dst)  
		if cv.waitKey(1) & 0xFF == ord('q'): 
			break

def main(argv):
	inputfile = None
	outputfile = None
	opts, args = getopt.getopt(argv,"i:o:l",["input=","output="])
	for opt, arg in opts:
		print(arg)
		if opt in ("-i", "--input"):
			inputfile = arg
		elif opt in ("-o", "--otput"):
			outputfile = arg
		elif arg in ("-l"):
			live()

	if inputfile and outputfile is not None:
		convert(inputfile, outputfile)

 
if __name__ == "__main__":
   main(sys.argv[1:])
