import cv2
import matplotlib.pyplot as plt
import numpy as np

def convert_img(image_path, output_path, n_colors=5):
    image=cv2.imread(image_path)
    image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # plt.imshow(image)
    # plt.axis('off')
    pixel=image.reshape(-1, 3)
    pixels=pixel/255

    from sklearn.cluster import KMeans
    kmeans=KMeans(n_clusters=n_colors)
    kmeans.fit(pixels)
    palette=kmeans.cluster_centers_
    palette=palette*255
    palette=palette.astype(int)
    
    def making_palatte(palette):
        plt.figure(figsize=(8,8))
        for i, color in enumerate(palette):
            plt.subplot(1, n_colors, i+1)
            plt.axis('off')
            plt.imshow([[color]])

    making_palatte(palette)
    new_colors=kmeans.cluster_centers_[kmeans.predict(pixels)]
    #kmeans.predict(pixels)는 각 픽셀이 몇 번 클러스터에 해당하는지 리턴함. (0 부터 k-1 까지 번호.)
    #kmeans.cluster_centers_에는 각 클러스터의 중심값(RGB)이 배열 형태로 저장되어있다.
    #그러니까 new_colors는 pixels를 predict해서 어느 클러스터에 해당하는지 번호를 리턴하고,
    #그 번호를 가진 클러스터의 중심값을 리턴, 이걸 사진의 픽셀 수만큼 해서 new_colors는 
    #모든 픽셀이 자기가 속한 클러스터의 중심값(RGB)로 바뀐 2차원 배열이다.
    new_colors=new_colors*255
    new_colors=new_colors.astype(int)
    new_image=new_colors.reshape(image.shape).astype(np.uint8)
    plt.imshow(new_image)
    plt.axis('off')

    new_image_bgr=cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, new_image_bgr)
    
    return output_path
