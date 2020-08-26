#配置
1.https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal
-Download cuda toolkit 10.0 archive(local installer type)
-安装界面取消VS integration的安装以及GeForce experience的安装
-安装完成配置环境变量-系统变量-新建-变量名：CUDA_PATH_V10_0，变量值：C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0
-系统变量-Path-新建-C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin
	       -新建-C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\libnvvp

2.https://developer.nvidia.com/compute/machine-learning/cudnn/secure/7.6.5.32/Production/10.0_20191031/cudnn-10.0-windows10-x64-v7.6.5.32.zip
-Download cudnn v7.6.5 for cuda 10.0, window10

3.把cudnn文件夹中的东西copy到cuda文件夹中，重复就覆盖
-命令行输入nvcc -V检验

4.https://www.anaconda.com/download/ python 3.6 version
-Download Anaconda3-2020.02-Windows-x86_64(about 478 MB)
-安装过程中'All users'是在当本电脑有多个用户时选择
-控制面板\系统和安全\系统\高级系统设置\环境变量\用户变量\PATH 中添加 (eg: C:\ProgramData\Anaconda3\Scripts, C:\ProgramData\Anaconda3\Library\usr\bin, C:\ProgramData\Anaconda3\Library\bin, C:\ProgramData\Anaconda3\Library\mingw-w64\bin, C:\ProgramData\Anaconda3\)
-打开命令行: 'conda --version'检验

5.Install pycharm-professional-2020.1.1.exe

6.（为了import cv2）如果没有提供VC_redist.x64.exe给你，打开anaconda命令行输入pip install opencv-python

7.用anaconda安装keras，pip install -i https://pypi.tuna.tsinghua.edu.cn/simple keras==2.1.5

8.用anaconda安装tensorflow，pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorflow-gpu==1.13.1 看到下载之后复制链接到浏览器用迅雷下载（链接不出意外应该https://pypi.tuna.tsinghua.edu.cn/packages/a0/dd/8fd5f91345ef290e884343bbb947ab074af4cb73813128b692977160aeec/tensorflow_gpu-1.13.1-cp37-cp37m-win_amd64.whl）
下载完打开anaconda，进入tensorflow下载地址，输入install (tensorflow文件名)

9.打开pycharm, file-settings-project:****-project interpreter-project interpreter choice blank-show all-add button-conda environment-click existing environment-interpreter choce blank-browse-find installed anaconda3 folder-choose python.exe
--如果想要用10.1的时候，anaconda命令行输入conda create -n cuda101 python=3.7.6，重复file-settings-......-find installed anaconda3 folder-envs-cuda101-python.exe


如果希望安装cuda10.1其他步骤差不多，安装tensorflow时pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorflow==2.1
----------

#Report about the Project
##Algorithm
Object Detection via Yolov4, and applying COCO data set.<br>
>Training of 2D detection of the stapler at 360 degree of camera angles, with various stapler state (open/close), and different environment (white wooden desk/brown wooden desk).
>Based on a rigid reference, measure and tell whether installed staples is appropriate and how guiding message, and training of the 2D detection at all common operating angles with various stapler state, and different environment (similar as above).<br>
##Training data set
>We take photos of the target, here is the stapler of course, we take them at common-used angles, with different state of the stapler and different length of nails. <br>
>We need to make our model after training recognize the stapler and nails and whether the length of nails is appropriate, we have to have three kinds of labels here which are the stapler, we named it with ‘t’ in the detection, the nails, we named it with ‘b’, and a reference, we named it with ‘a’.<br>
>After a series of translate, we get a data set which can be used in the yolov4 structure to train, we first put in photos with stapler to train a model just for detect the stapler. Next, put in photos with nails and reference to train a model just for nails detection. While the model is not as what we expected, we take more photos and let the computer do reinforcement learning. After two models are ready, we program to use the two models to automatically label photos for us, and program to integrate the labels for nails and the labels for stapler.<br>
>We make a pre-process before training, we utilize the coco data set which is far more complicate and huge than our data set. We import the coco data set, and apply the transfer learning so that we could lower the risk of gradient explosion or gradient disappear, and also, a larger data set could effectively rise the learning efficiency, and lower the loss of detection at a higher speed. Cuz a training process could usually last for dozens of hours or even several days, a lower risk would prevent us from waiting for a long time, and it collapsed, and we need to retrain and redo the whole process again, and a higher speed could apparently get us a good result earlier.<br>
![Image1](https://github.com/lujiannan/Artificial-Intelligence/blob/master/images/%E5%9B%BE%E7%89%871.png)<br>
##Effect of the algorithm on testing data
![Image2](https://github.com/lujiannan/Artificial-Intelligence/blob/master/images/%E5%9B%BE%E7%89%872.png)<br>
![Image3](https://github.com/lujiannan/Artificial-Intelligence/blob/master/images/%E5%9B%BE%E7%89%873.png)<br>
![Image4](https://github.com/lujiannan/Artificial-Intelligence/blob/master/images/%E5%9B%BE%E7%89%874.png)<br>
![Image5](https://github.com/lujiannan/Artificial-Intelligence/blob/master/images/%E5%9B%BE%E7%89%875.png)<br>
Since the outcome is limited by the camera resolution, suggest use the same camera with both training set and testing set.<br>
##Task time estimation
* Development time: about 2 to 3 weeks, 1 developer <br>
* Label images: 1285 images, 1 to 2 weeks, 1 developer, using labelme tool installed with ‘pip install labelme’ <br>
* Training process: NVIDIA 2080-Ti, 70 hours per training for 1285 images with 3 annotations: ‘reference’, ‘staple’, ‘stapler’ (500 epochs per training) <br>