#include <stdio.h>
#include <cv.h>
#include <highgui.h>


int main(int argc, char* argv[])
{

	int i;
	float *p;
	double w = 320, h = 240;

	IplImage *src_img = 0, *gray_img = 0;
	CvMemStorage *storage;
	CvSeq *circles = 0;
	CvCapture *capture = 0;


	/* この設定は，利用するカメラに依存する */
	capture = cvCreateCameraCapture (0);

	// (2)キャプチャサイズを設定する．
	cvSetCaptureProperty (capture, CV_CAP_PROP_FRAME_WIDTH, w);
	cvSetCaptureProperty (capture, CV_CAP_PROP_FRAME_HEIGHT, h);


	cvNamedWindow ("circles", CV_WINDOW_AUTOSIZE);


	while(1) {


		src_img = cvQueryFrame (capture);

		CvSize sizeOfImage = cvGetSize(src_img);
		//IplImage *gray_img = cvCreateImage(cvGetSize(src_img), IPL_DEPTH_8U, 1);
		gray_img = cvCreateImage(cvGetSize(src_img), IPL_DEPTH_8U, 1);

		// グレイスケールに変換
		cvCvtColor(src_img, gray_img, CV_BGR2GRAY);

		//src_img_gray = cvQueryFrame (capture);


		// (2)ハフ変換のための前処理（画像の平滑化を行なわないと誤検出が発生しやすい）
		cvSmooth (gray_img, gray_img, CV_GAUSSIAN, 11, 11, 0, 0);
		storage = cvCreateMemStorage (0);

		// (3)ハフ変換による円の検出と検出した円の描画
		
		circles = cvHoughCircles (gray_img, storage, CV_HOUGH_GRADIENT,
				1, 100, 20, 50, 10, MAX (gray_img->width, gray_img->height));

		for (i = 0; i < circles->total; i++) {
			p = (float *) cvGetSeqElem (circles, i);
			cvCircle (src_img, cvPoint (cvRound (p[0]), cvRound (p[1])), 3, CV_RGB (0, 255, 0), -1, 8, 0);
			cvCircle (src_img, cvPoint (cvRound (p[0]), cvRound (p[1])), cvRound (p[2]), CV_RGB (255, 0, 0), 3, 8, 0);
		}
		// (4)検出結果表示用のウィンドウを確保し表示する

		cvShowImage ("circles", src_img);
		cvWaitKey (10);

	}

	cvDestroyWindow ("circles");
	cvReleaseImage (&src_img);
	cvReleaseImage (&gray_img);
	cvReleaseMemStorage (&storage);

	return 0;

}