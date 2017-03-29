function example()
inputDir = '/input';
outputDir = '/output';

% Add subfolders to the path
currentFolder = fileparts(which(mfilename)); 
addpath(genpath(currentFolder));

nii = load_untouch_nii([inputDir '/orig/FLAIR.nii.gz']);

nii.img(nii.img <  800) = 0;
nii.img(nii.img >= 800) = 1;

save_untouch_nii(nii, [outputDir '/result.nii.gz']);