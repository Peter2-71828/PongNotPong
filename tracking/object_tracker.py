from tracking.centroid_register import CentroidRegister
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
from cv2 import dnn
import itertools

print("[INFO] loading model...")
net = dnn.readNetFromCaffe("detection/deploy.prototxt", "detection/res10_300x300_ssd_iter_140000.caffemodel")

print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

cr = CentroidRegister()
(H, W) = (None, None)

def movement(net = net, vs = vs, cr = cr, H = H, W = W):

	while True:
		frame = vs.read()
		frame = imutils.resize(frame, width=400)

		if W is None or H is None:
			(H, W) = frame.shape[:2]

		blob = dnn.blobFromImage(frame, 1.0, (W, H),
			(104.0, 177.0, 123.0))
		net.setInput(blob)
		detections = net.forward()
		rects = []

		for i in range(0, detections.shape[2]):

			if detections[0, 0, i, 2] > 0.5:
							# confidence value 0.5

				box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
				rects.append(box.astype("int"))

				(startX, startY, endX, endY) = box.astype("int")
				cv2.rectangle(frame, (startX, startY), (endX, endY),
					(0, 255, 0), 2)

		objects = cr.update(rects)

		for k, v in objects.items():
			global head
			head = v[1]


		for (objectID, centroid) in objects.items():

			text = "ID {}".format(objectID)
			cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
			cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

		if key == ord("q"):
			break

	cv2.destroyAllWindows()
	vs.stop()
