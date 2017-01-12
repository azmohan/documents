# 卓易framework组linux开发环境搭建指南

## ubuntu系统安装

安装环境为ubuntu14.04，下载地址为：

iso可从官网下载，也可从公司的ftp服务器上下载（位于software\镜像软件目录下\ubuntu-14.04-desktop-amd64.iso），可使用u盘制作启动盘安装，u盘制作方法请参考网上资料。

linux系统上制作ubuntu启动盘的方法为（需要准备一块可用U盘，根据自己系统的实际情况修改下面命令中的/dev/sdc1）
```
sudo dd if=ubuntu-14.04-desktop-amd64.iso of=/dev/sdc1 bs=1M
```

制作完毕后开机配置bios，通过U盘启动后开始安装过程。

### ubuntu安装硬盘分区方案

因为代码占用空间较大，建议分区方案为：
* 根分区，EXT4格式，25G左右
* swap分区，8G即可
* /home分区，EXT4格式，其余所有空间

如果有两块硬盘，如500G+2T硬盘，建议分区方案为：
500G硬盘：根分区25G + 8G swap分区 + /opt分区(EXT4格式，剩余全部）
2G硬盘，全部/home分区

### 系统配置

公司搭建了ubuntu镜像源，ubuntu系统安装完毕后，请按照如下命令配置源

```
$ sudo gedit /etc/apt/sources.list
```

将该文件全部内容删除后，复制如下内容到该文件中。

```                                                                                                                         [10:37:07]
#copy all the code in /etc/apt/source.list

deb http://192.168.0.193/ubuntu/ trusty main restricted universe multiverse

deb http://192.168.0.193/ubuntu/ trusty-security main restricted universe multiverse

deb http://192.168.0.193/ubuntu/ trusty-updates main restricted universe multiverse

deb http://192.168.0.193/ubuntu/ trusty-proposed main restricted universe multiverse

deb http://192.168.0.193/ubuntu/ trusty-backports main restricted universe multiverse
```

执行如下命令更新源的安装包索引信息

``` bash
$ sudo apt-get update
```
安装必要的软件包

``` bash
$ sudo apt-get install gdebi vim vim-gnome subversion tree p7zip-full openssh-server
```

配置输入法

默认输入法为ibus比较难用，可安装搜狗linux输入法，命令为

``` bash
$ sudo apt-get install fcitx
$ im-config
```

下载搜狗输入法：http://pinyin.sogou.com/linux/ 下载得到deb包后，命令行执行

``` bash
$ sudo gdebi sogoupinyin_2.0.0.0078_amd64.deb
```

## 搭建Android代码编译环境

``` bash
$ sudo apt-get install openjdk-7-jdk
$ sudo apt-get install git-core gnupg flex bison gperf build-essential \
  zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 \
  lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev ccache \
  libgl1-mesa-dev libxml2-utils xsltproc unzip

```

PS. 参考自：https://source.android.com/source/initializing.html

### 安装加密系统

请联系公司IT配置加密系统。

