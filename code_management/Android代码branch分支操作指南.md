# Android代码branch分支操作指南

[TOC]

## 概述

本文讲述如果开发branch分支。

本文以70M项目例讲解，如何从`driver`分支branch出`pcb_oversea`分支的具体方法。

## 获取权限

本文操作需要操作人员具有相关权限，属于`gerrit`的代码管理组（即cm组）。

请具有`cm`权限的人帮忙添加进入改组，添加方法是，打开`gerrit`，在`People` 进入`List Groups`，点击`cm`，将自己的名字加入。

## 拉取代码

首先拉取该项目`driver`分支代码，注意修改`zhuzhongkai`为你的名字。

```
$ mkdir 6570m
$ repo init --no-repo-verify -u ssh://zhuzhongkai@10.20.40.19:29418/freemeos/manifest -m ALPS-MP-M0.MP23-V1.32.3_DROI6570_CTLC_M/driver.xml
$ repo sync
$ repo start --all master
```

## 创建分支

创建本地`pcb_oversea`分支

```
$ repo start --all pcb_oversea
```

将本地`pcb_oversea`分支推送到gerrit服务器上

```
$ repo forall -pc git push origin pcb_oversea
```

执行完毕后前往gerit网页上，进入相关仓库，查看branches页面，是否有`pcb_oversea`分支。

## 提交manifest

```
$ cd .repo
$ cd ALPS-MP-N0.MP1-V1.0.2_DROI6737M_65_N
$ cp driver.xml pcb_oversea.xml
```

编辑该文件，将其中的`revision`字段的`driver`修改为`pcb_oversea`
```
@@ -4,7 +4,7 @@
   <remote  name="origin"
            fetch=".."
            review="http://10.20.40.19:8080/" />
-  <default revision="driver"
+  <default revision="pcb_oversea"
            remote="origin"
            sync-j="4" />
```

请检查其他项目额外项目的`revision`字段也需要替换成对应的分支。

接下来提交代码
```
$ git add pcb_oversea.xml
$ git commit -m "[mainfest] branch pcb_oversea for ALPS-MP-M0.MP23-V1.32.3_DROI6570_CTLC_M"
$ git push origin HEAD:refs/for/master
```

然后请Leader将review该提交。