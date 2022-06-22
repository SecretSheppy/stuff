package com.secretsheppy.ocv.main;

import java.util.List;

import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.MatOfRect;
import org.opencv.core.Point;
import org.opencv.core.Rect;
import org.opencv.core.Scalar;
import org.opencv.highgui.HighGui;
import org.opencv.imgproc.Imgproc;
import org.opencv.objdetect.CascadeClassifier;
import org.opencv.videoio.VideoCapture;

/**
 * <h1>OpenCV Detection Demonstration - Java</h1>
 * 
 * Demonstration of Java OpenCV Detection for Windows.
 * 
 * Built in JavaSE-1.8
 * 
 * To run, add the opencv libray (download: https://opencv.org/releases/) to the java project build path and insert path to cascade where specified
 * 
 * @author SecretSheppy
 */
public class opencvdemo {

	public static void main(String [] args) {
		
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		
		VideoCapture videoStream = new VideoCapture(0);
		Mat frame = new Mat();
		Mat frameGray = new Mat();
		
		CascadeClassifier cascade = new CascadeClassifier();
		// insert path to cascade below
		if (!cascade.load("C:/...")) {
			System.err.println("Cascade could not be found!");
			System.exit(0);
		}
		
		while (videoStream.read(frame)) {
			if (frame.empty()) {
				System.err.println("Frame could not be captured!");
				System.exit(0);
			}
			
			Imgproc.cvtColor(frame, frameGray, Imgproc.COLOR_RGB2GRAY);
			Imgproc.equalizeHist(frameGray, frameGray);
			
			MatOfRect detected = new MatOfRect();
			cascade.detectMultiScale(frameGray, detected);
			
			List<Rect> listOfRect = detected.toList();
			for (Rect object : listOfRect) {
		    	Imgproc.rectangle(frame, 
		    			new Point(object.x, object.y), 
		    			new Point(object.x + object.width, object.y + object.height), 
		    			new Scalar(0, 0, 255), 2);
		    }
		    
		    HighGui.imshow("Object Detection", frame);
		    if (HighGui.waitKey(10) == 27) {
		    	break;
		    }
		}
		
	}
	
}
