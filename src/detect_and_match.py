import cv2 as cv

def image_name_creator(folder_path, i):
       return folder_path + "goldengate-0" + str(i) + ".png"

def sift_keypoints_name_creator(folder_path, i):
       return folder_path + "sift_keypoints-" + str(i) + ".png"

def tentative_correspondences_name_creator(folder_path, i, j):
       return folder_path + "tentative correspondences_" + str(i) + "-" + str(j) + ".png"

def sift_name_creator(folder_path, i):
        return folder_path + "sift_" + str(i) + ".txt"

def tentative_correspondences_data_name_creator(folder_path, i, j):
        return folder_path + "tentative correspondences_" + str(i) + "-" + str(j) + ".txt"

def keypoints_and_descriptors_detector(image):
        sift = cv.SIFT_create()
        return sift.detectAndCompute(image,None)

def draw_keypoints(image, keypoints, output_path):
        draw_image = cv.drawKeypoints(image, keypoints, None)
        cv.imwrite(output_path, draw_image)

def feature_matcher(descriptoprs_1, descriptors_2):
        matcher = cv.BFMatcher()
        return matcher.match(descriptoprs_1, descriptors_2)

def draw_matches(image_1, image_1_keypoints, image_2, image_2_keypoints, matches, output_path):
        image = cv.drawMatches(image_1, image_1_keypoints, image_2, image_2_keypoints, matches, None)
        cv.imwrite(output_path, image)

def save_sift(image_attributes_list, output_path):
        with open(output_path, 'w') as file:
                file.write("Keypoints:\n")
                for kp, desc in zip(image_attributes_list[1], image_attributes_list[2]):
                        x = kp.pt[0]
                        y = kp.pt[1]
                        size = kp.size
                        angle = kp.angle
                        desc_str = ', '.join(str(value) for value in desc)

                        file.write(f"x = {x}, y = {y}, size = {size}, angle = {angle}\n")
                        file.write(f"Descriptor: {desc_str}\n\n")

def save_tentative_correspondences(matches, output_path):
        with open(output_path, 'w') as file:
                file.write(f"Tentative_Correspondences for image {matches[0]} to image {matches[1]}:\n")
                for i in matches[2:]:
                        for j in i:
                                file.write(f"Query Index:{j.queryIdx}, Train Index:{j.trainIdx}, Distance:{j.distance}\t")
                                file.write("\n")

FOLDER_PATH = "data/goldengate/"

Images = list()

#Part a:
for i in range(0,6):
        image = cv.imread(image_name_creator(FOLDER_PATH, i))
        Images.append([image])

for i in range(0,6):
        keypoints, descriptors = keypoints_and_descriptors_detector(Images[i][0])
        Images[i].append(keypoints)
        Images[i].append(descriptors)
        
#Part b:
for i in range(0,6):
        draw_keypoints(Images[i][0], Images[i][1], sift_keypoints_name_creator(FOLDER_PATH, i))

#Part c:
matches = list()

for i in range(0,6):
        for j in range(i + 1,6):
                matches.append([i, j, feature_matcher(Images[i][2], Images[j][2])])

#Part d:
index = 0
for i in range(0,6):
        for j in range(i + 1, 6):
                draw_matches(Images[i][0], Images[i][1], Images[j][0], Images[j][1], matches[index][2][:20], tentative_correspondences_name_creator(FOLDER_PATH, i, j))
                index += 1

#Part e:
for i in range(0,6):
        save_sift(Images[i], sift_name_creator(FOLDER_PATH, i))

index = 0
for i in range(0,6):
        for j in range(i + 1,6):
                save_tentative_correspondences(matches[index], tentative_correspondences_data_name_creator(FOLDER_PATH, i ,j))

print("Successfully Done!")                