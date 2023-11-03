import cv2 as cv
import numpy as np

def image_name_creator(folder_path, i):
        return folder_path + f"goldengate-0{i}.png"

def cut_image(image):
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        non_zero_pixels = cv.findNonZero(gray)

        x, y, w, h = cv.boundingRect(non_zero_pixels)

        return image[y:y+h, x:x+w]

def stitch(src_image, dst_image, right):

        sift = cv.SIFT_create()
        
        dst_kp, dst_dp = sift.detectAndCompute(dst_image, None)
        src_kp, src_dp = sift.detectAndCompute(src_image, None)

        bf = cv.BFMatcher(crossCheck=True)

        matches = bf.match(src_dp, dst_dp)

        train_pt = np.float32([dst_kp[m.trainIdx].pt for m in matches])
        query_pt = np.float32([src_kp[m.queryIdx].pt for m in matches])

        M, status = cv.findHomography(query_pt, train_pt, cv.RANSAC, 5.0)

        width = dst_image.shape[1] + src_image.shape[1]
        height = max(dst_image.shape[0], src_image.shape[0])

        result = cv.warpPerspective(src_image, M, (width, height))
        result[0:dst_image.shape[0], 0:dst_image.shape[1]] = dst_image
        return result

def main():
        FOLDER_PATH = "data/goldengate/"
        image = cv.imread(image_name_creator(FOLDER_PATH, 0))

        for i in range(1,6):
                temp_image = cv.imread(image_name_creator(FOLDER_PATH, i))
                image = stitch(temp_image, image, True)
                image = cut_image(image)
        cv.imwrite(FOLDER_PATH + "panorama.png", image)
        
        print("Successfully Done!")

if __name__ == "__main__":
        main()


