import matplotlib
import matplotlib.pyplot as plt
import numpy as np 
import cv2

def plot_lines(lines, h, w):
    """ Utility function to plot lines
    """

    for i in range(lines.shape[1]):
        # plt.close('all')
        if abs(lines[0, i] / lines[1, i]) < 1:
            y0 = -lines[2, i] / lines[1, i]
            yw = y0 - w * lines[0, i] / lines[1, i]
            plt.plot([0, w], [y0, yw])
            # plt.clf()
            # plt.show()
            # plt.savefig(filename)
        else:
            x0 = -lines[2, i] / lines[0, i]
            xh = x0 - h * lines[1, i] / lines[0, i]
            plt.plot([x0, xh], [0, h])
            # plt.clf
            # plt.show()
            # plt.savefig(filename)


def plot_epipolar_lines(image1, image2, uncalibrated_1, uncalibrated_2, E, K, plot=True):
    """ Plots the epipolar lines on the images
    """

    """ YOUR CODE HERE
    """

    epipolar_lines_in_1 = []
    epipolar_lines_in_2 = []

    Fundemental = np.dot((np.linalg.inv(K)).T, np.dot(E, np.linalg.inv(K)))

    for idx in range(uncalibrated_1.shape[1]):
      U_1 = [r[idx] for r in uncalibrated_1]
      U_2 = [r[idx] for r in uncalibrated_2]
      epipolar_lines_in_1.append(np.dot(Fundemental.T, U_2))
      epipolar_lines_in_2.append(np.dot(Fundemental, U_1)) 
      
    epipolar_lines_in_1 = np.transpose(epipolar_lines_in_1)
    epipolar_lines_in_2 = np.transpose(epipolar_lines_in_2)

    """ END YOUR CODE
    """
    
    if(plot):

        plt.figure(figsize=(6.4*3, 4.8*3))
        ax = plt.subplot(1, 2, 1)
        ax.set_xlim([0, image1.shape[1]])
        ax.set_ylim([image1.shape[0], 0])
        plt.imshow(image1[:, :, ::-1])
        plot_lines(epipolar_lines_in_1, image1.shape[0], image1.shape[1])

        ax = plt.subplot(1, 2, 2)
        ax.set_xlim([0, image1.shape[1]])
        ax.set_ylim([image1.shape[0], 0])
        plt.imshow(image2[:, :, ::-1])
        plot_lines(epipolar_lines_in_2, image2.shape[0], image2.shape[1])
        
    else:
        return epipolar_lines_in_1, epipolar_lines_in_2
    