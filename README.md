# Introduction-to-Image-Understanding-3

This repository contains the solution for Homework 3 of CENG 391 - Introduction to Image Understanding.

# Assignment Description
The assignment consists of three main exercises that involve image processing, feature detection, RANSAC, and basic image stitching. Each exercise has its own set of tasks and requirements.

# Exercise 1 - Image Processing and Feature Detection
## a. Detect SIFT Interest Points
* Implement a single Python script named src/detect_and_match.py.
* Utilize OpenCV for feature detection and descriptor computation.
* Detect SIFT interest points on the six images of the Golden Gate Bridge located in the "data" folder.
## b. Draw and Store SIFT Interest Points
* Draw the SIFT interest points on each image.
* Save the resulting images in the same folder with names as sift_keypoints_i.png, where i represents the image number.
## c. Calculate SIFT Descriptor Matches
* Calculate SIFT descriptor matches between consecutive pairs of images using brute force matching.
* For example, match descriptors between goldengate-00.png and goldengate-01.png, between goldengate-01.png and goldengate-02.png, and so on.
## d. Draw and Save Tentative Correspondences
* Draw the tentative correspondences on a match image.
* Save the resulting images in the same folder with names as tentative_correspondences_i-j.png, where i and j represent the image numbers.
## e. Save SIFT Interest Points and Correspondences
* Save the SIFT interest points, descriptors, and tentative correspondences as text files in the same folder with names as sift_i.txt and tentative_correspondences_i-j.txt.
# Exercise 2 - RANSAC
## a. Read Keypoints and Correspondences
* Implement a Python script named src/ransac.py.
* Read the keypoints and tentative correspondences for each image pair.
## b. Match Using RANSAC
* Match the keypoints using RANSAC. You can use RANSAC from OpenCV or implement it yourself for bonus points.
## c. Save Homography Matrices
* Save the resulting homography matrices in files within the "data" folder with names such as h_i-j.txt, where i and j are image numbers.
## d. Normalization and Final Estimation
* Ensure normalization and the final estimation over all inliers.
* Optionally perform guided matching.
## e. Draw and Save Final Inlier Correspondences
* Draw and save the resulting final inlier correspondences in files in the "data" folder with names as inliers_i-j.png and inliers_i-j.txt.
# Exercise 3 - Basic Stitching
## a. Stitch Images
* Implement a Python script named src/stitch.py.
* Stitch all the images by calculating a homography matrix from each image to one of the center images (goldengate-02.png or goldengate-03.png).
## b. Save Panorama Image
Save the resulting stitched image in the "data" folder named as panorama.png.
## c. Image Blending
* To blend multiple images, overwrite or average intensities of overlapping pixels.
* How to Use the Code
* Download and extract the contents of ceng391_hw03.tar.gz.
* Open and run the Python scripts detect_and_match.py, ransac.py, and stitch.py located in the src folder.
* The scripts will perform the specified tasks and save the output images and text files in the "data" folder.
