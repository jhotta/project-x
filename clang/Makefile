CXXFLAGS = \
-I/usr/local/include

LDFLAGS = \
-L/usr/local/lib \
-lopencv_core \
-lopencv_highgui \
-lopencv_features2d \
-lopencv_imgproc \
-lopencv_nonfree

circle:
	gcc -o hough_circle hough_circle.c `pkg-config --cflags opencv` `pkg-config --libs opencv` -lm

circle2:
	g++ $(CXXFLAGS) $(LDFLAGS) main.cpp
