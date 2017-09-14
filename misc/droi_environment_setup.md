# 卓易framework组linux开发环境搭建指南

[TOC]

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


公司内部部署了加密系统，所有代码在本地加密。需要在本地安装加密客户端，并登陆账号密码。账号为`拼音全名+数字1`、密码为`12345678`，如刘德华的加密账号密码为：

- 账号：liudehua1
- 密码：12345678


只有正确安装了加密客户端，才能从公司服务器上拉取代码。安装加密客户端命令如下，

```
sudo wget http://192.168.0.193/packages/linux/ultrasec_3.5.0_amd64.deb && sudo dpkg -i ultrasec_3.5.0_amd64.deb
```

确保使用加密系统支持的内核，查看内核版本命令为

```
uname -a
```

ubuntu 14.04请使用`3.13.0-24-generic`内核，如果使用高版本内核，请降级内核，命令如下，

```
sudo apt-get remove linux-image-3.13.0-144-generic
```

安装完成后重启系统

确认加密客户端是否安装的方法是（仅以ubuntu系统为例），终端执行`usec`，是否出现：

```
1.Update policy
2.Change password
3.Set workspace
4.View status
5.Offline service
6.Logout
7.About
8.Quit
> Please choose:
```

首先输入设置加密服务器ip地址和端口:

- ip： `192.168.0.128`
- port：`80`

设置账号密码, 如前面描述的刘德华，其账号密码分别是

- 账号：liudehua1
- 密码：12345678

然后根据情况，设置workspace（即要被加密的目录，默认只加密 /home、/root两个目录, 如果代码位于/mnt分区下，请添加workspace）

最后输入4，若出现类似以下输出，则表示加密客户端正确运行

```
Online: zhuzhongkai1
```

如果usec提示未知道匹配的内核，说明加密客户端不支持你的ubuntu系统当前使用的内核。请配置使用指定内核。

如果打开本地代码发现都是乱码。有两种可能：

1. 加密客户端未正常工作。请执行`usec`查看，内核升级、未登陆账号密码都可能导致该问题。请确保内核版本为`3.13.0-24-generic`、账号正确登陆。
2. 加密客户端正常。但是源码所在路径没有被设置为加密目录。

