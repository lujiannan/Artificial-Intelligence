配置：

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

*******************************************************************************************************如果希望安装cuda10.1其他步骤差不多，安装tensorflow时pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorflow==2.1

