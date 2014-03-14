// main.cpp
#include <iostream>
#include <string>
#include <opencv2/opencv.hpp>
#include <opencv2/nonfree/nonfree.hpp>

using namespace std;
using namespace cv;

int main(int argc, char* argv[]) {
  // load color image
  const char* imagename = argc > 1 ? argv[1] : "./img/lena.png";
  Mat colorImage = imread(imagename, 1);
  if (colorImage.empty()) {
    cout << "file not found" << endl;
    return -1;
  }

  // convert color image to grayscale for feature extraction
  Mat grayImage;
  cvtColor(colorImage, grayImage, CV_BGR2GRAY);

  // initialize SURF class
  SURF calc_surf = SURF(500, 4, 2, true);

  // extract SURF
  vector<KeyPoint> kp_vec;
  vector<float> dest_vec;
  calc_surf(grayImage, Mat(), kp_vec, dest_vec);

  // draw keypoints
  cout << "Image keypoints: " << kp_vec.size() << endl;
  for (int i = 0; i < kp_vec.size(); ++i) {
    KeyPoint* point = &(kp_vec[i]);
    Point center(cvRound(point->pt.x), cvRound(point->pt.y));
    int radius = cvRound(point->size * 0.25);
    circle(colorImage, center, radius, Scalar(255, 255, 0), 1, 8, 0);
  }

  namedWindow("SURF", CV_WINDOW_AUTOSIZE);
  imshow("SURF", colorImage);
  waitKey(0);

  return 0;
}
