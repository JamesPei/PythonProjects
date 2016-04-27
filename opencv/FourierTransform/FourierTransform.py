#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

#使用numpy完成傅里叶变换
def numpy_fourier_transform():

    img = cv2.imread('messi.jpg',0)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f) #Shift the zero-frequency component to the center of the spectrum
    magnitude_spectrum = 20*np.log(np.abs(fshift))  #log求对数

    # plt.subplot(121),plt.imshow(img, cmap = 'gray')
    # plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    # plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    # plt.show()

    rows, cols = img.shape
    crow,ccol = rows/2 , cols/2
    fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    plt.subplot(131),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
    plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(img_back)
    plt.title('Result in JET'), plt.xticks([]), plt.yticks([])

    plt.show()

#opencv的傅里叶变换,照例比Numpy快了很多
def opencv_fourier_transform():
    img = cv2.imread('messi.jpg',0)

    # Performs a forward or inverse Discrete Fourier transform of a 1D or 2D floating-point array
    #cv2.dft(src[, dst[, flags[, nonzeroRows]]]) → dst
    dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

    # plt.subplot(121),plt.imshow(img, cmap = 'gray')
    # plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    # plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    # plt.show()

    #以下是逆DFT，用于低通滤波
    rows, cols = img.shape
    crow,ccol = rows/2 , cols/2

    # create a mask first, center square is 1, remaining all zeros
    mask = np.zeros((rows,cols,2),np.uint8)
    mask[crow-30:crow+30, ccol-30:ccol+30] = 1

    # apply mask and inverse DFT
    fshift = dft_shift*mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    #Calculates the magnitude of 2D vectors
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

#为什么拉普拉斯算子是高通滤波器
def why_Laplacian_is_a_HPF():
    # simple averaging filter without scaling parameter
    mean_filter = np.ones((3,3))

    # creating a guassian filter, cv2.getGaussianKernel(ksize, sigma[, ktype]) → retval
    x = cv2.getGaussianKernel(5,10)
    gaussian = x*x.T

    # different edge detecting filters
    # scharr in x-direction
    scharr = np.array([[-3, 0, 3],
                       [-10,0,10],
                       [-3, 0, 3]])
    # sobel in x direction
    sobel_x= np.array([[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]])
    # sobel in y direction
    sobel_y= np.array([[-1,-2,-1],
                       [0, 0, 0],
                       [1, 2, 1]])
    # laplacian
    laplacian=np.array([[0, 1, 0],
                        [1,-4, 1],
                        [0, 1, 0]])

    filters = [mean_filter, gaussian, laplacian, sobel_x, sobel_y, scharr]
    filter_name = ['mean_filter', 'gaussian','laplacian', 'sobel_x', 'sobel_y', 'scharr_x']
    fft_filters = [np.fft.fft2(x) for x in filters]
    fft_shift = [np.fft.fftshift(y) for y in fft_filters]
    mag_spectrum = [np.log(np.abs(z)+1) for z in fft_shift]

    for i in xrange(6):
        plt.subplot(2,3,i+1),plt.imshow(mag_spectrum[i],cmap = 'gray')
        plt.title(filter_name[i]), plt.xticks([]), plt.yticks([])

    plt.show()


# numpy_fourier_transform()
why_Laplacian_is_a_HPF()