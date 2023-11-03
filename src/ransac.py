import cv2 as cv
import numpy as np


def image_name_creator(i):
        return f"data/goldengate/goldengate-0{i}.png"

def ransac(i, j):

        image1 = cv.imread(image_name_creator(i))
        image2 = cv.imread(image_name_creator(j)) 
        
        sift = cv.SIFT_create()
        kp1, dp1 = sift.detectAndCompute(image1, None)
        kp2, dp2 = sift.detectAndCompute(image2, None)

        bf = cv.BFMatcher(crossCheck=True)

        matches = bf.match(dp1, dp2)

        pts1 = np.float32([kp1[m.queryIdx].pt for m in matches])
        pts2 = np.float32([kp2[m.trainIdx].pt for m in matches])  

        homography, mask = cv.findHomography(pts1, pts2, cv.RANSAC, 5.0)

        np.savetxt(f"data/goldengate/h_{i}-{j}.txt", homography)

        transformed_pts1 = cv.perspectiveTransform(pts1.reshape(-1, 1, 2), homography).reshape(-1,2)

        distances = np.linalg.norm(transformed_pts1 - pts2, axis=1)
        inlier_mask = distances < 5.0
        inlier_matches = [match for match, mask_value in zip(matches, inlier_mask) if mask_value]

        inlier_image = cv.drawMatches(image1, kp1, image2, kp2, inlier_matches, None)
        cv.imwrite(f"data/goldengate/inliers_{i}-{j}.png", inlier_image)
        
        inlier_indices = [(match.queryIdx, match.trainIdx) for match, mask_value in zip(matches, inlier_mask) if mask_value]

        np.savetxt(f"data/goldengate/inliers_{i}-{j}.txt", inlier_indices, fmt='%d')

        
def main():

        for i in range(0, 6):
                for j in range(i+1, 6):
                        ransac(i, j)

        print("Successfully Done!")

if __name__ == "__main__":
        main()

