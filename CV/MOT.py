import cv2

# 트랙커 객체 생성자 함수 리스트
TrList = [cv2.legacy.TrackerBoosting_create,
            cv2.TrackerMIL_create,
            cv2.TrackerKCF_create,
            cv2.legacy.TrackerTLD_create,
            cv2.legacy.TrackerMedianFlow_create,
            cv2.legacy.TrackerCSRT_create,
            cv2.legacy.TrackerMOSSE_create]

trackers = cv2.legacy.MultiTracker_create()
video_src = "./highway.mp4"
v = cv2.VideoCapture(video_src)
ret, frame = v.read()
k = 2  # number of objects
for i in range(k):
    cv2.imshow('Frame',frame)
    bbox_i = cv2.selectROI('Frame',frame)
    tracker_i = TrList[5]()
    print(tracker_i)
    print(type(trackers))
    trackers.add(tracker_i,frame,bbox_i)
while True:
    ret, frame = v.read()
    if not ret:
        break
    ok, boxes = trackers.update(frame)
    for box in boxes:
        (x,y,w,h) = [int(a) for a in box]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(100,205,200),2)

    cv2.imshow('Frame',frame)
    key = cv2.waitKey(5)
    if key == ord('q'):
        break
v.release()
cv2.destroyWindow()
