import cv2

lineSegment = cv2.createLineSegmentDetector(0)


image_input = cv2.imread("test_image.jpg")
scale = 0.25
image = cv2.resize(image_input, (1000, 1000))
image_greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
lines = lineSegment.detect(image_greyscale)[0]
for i in range(10):
    grid_lines = cv2.line(image, (100*i, 0), (100*i, 1000), [255, 0, 0], 1)
    cv2.putText(grid_lines, str(i), (100*i, 90), cv2.FONT_HERSHEY_SIMPLEX, 4, [255, 255, 255], 2, cv2.LINE_AA)
for i in range(10):
    grid_lines = cv2.line(image, (0, i*100), (1000, i*100), [255, 0, 0], 1)
    cv2.putText(grid_lines, str(i), (0, 100*i + 90), cv2.FONT_HERSHEY_SIMPLEX, 4, [255, 255, 255], 2, cv2.LINE_AA)

# print(lines)
print(lines[0])
drawn_img = lineSegment.drawSegments(grid_lines, lines=lines[0])
cv2.imshow('test', drawn_img)
cv2.waitKey(-1)
cv2.destroyAllWindows()
