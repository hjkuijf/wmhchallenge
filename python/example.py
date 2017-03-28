# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:10:18 2017

@author: user
"""

import os
import SimpleITK as sitk

inputDir = '/input'
outputDir = '/output'

# Load the image
flairImage = sitk.ReadImage(os.path.join(inputDir, 'orig', 'FLAIR.nii.gz'))

## Numpy: threshold at 800
#dataArray = sitk.GetArrayFromImage(flairImage)
#dataArray[dataArray <  800] = 0
#dataArray[dataArray >= 800] = 1
#resultImage = sitk.GetImageFromArray(dataArray)
#resultImage.CopyInformation(flairImage)

# SimpleITK: binary threshold between 800 - 100000
resultImage = sitk.BinaryThreshold(flairImage, lowerThreshold=800, upperThreshold=100000)

sitk.WriteImage(resultImage, os.path.join(outputDir, 'result.nii.gz'))