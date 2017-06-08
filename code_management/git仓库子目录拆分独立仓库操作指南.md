# 操作指南

[TOC]

## 概述

如题。

## 获取权限

本文操作需要操作人员具有相关权限。具体需要在下文涉及时会明确说明。

## 操作方法

以下面仓库为例

```
ssh://zhuzhongkai@10.20.40.19:29418/freemeos/common/documents
```

该仓库目录结构如下

```
├── code_management
├── features
│   ├── instrument
│   └── prebuilts
├── gerrit
├── issues
├── misc
├── pdf
└── scripts
```

假如将`features/instrument`这个目录独立成git仓库。假如当前documents仓库位于`~/sharedir/projects/documents`目录下，那么操作如下：

```
$ cd ~/sharedir/projects/documents
```

```
$ git subtree split -P features/instrument -b instrument
```

上述命令会将该仓库的`features/instrument`目录下的所有提交过滤到`instrument`分支上。

```
$ cd ~/sharedir/projects/
$ mkdir seperate_instrument
$ cd seperate_instrument
$ git init
$ git pull ~/sharedir/projects/documents -b instrument
```

这样在seperate_instrument就是本地的独立git仓库，可以用`git log`查看提交记录

## 提交代码到gerrit

在gerit上创建仓库，如果没有权限，请联系gerit管理人员创建仓库，注意创建仓库时，不要勾选`Create initial empty commit`.

假如gerrit上创建的仓库路径是：`ssh://你的名字@gitlab.droi.com:29418/freemeos/common/instrument`

```
$ cd seperate_instrument
$ git remote add origin ssh://你的名字@gitlab.droi.com:29418/freemeos/common/instrument
$ git push origin master
```

注意上面最后一条push命令需要特殊gerrit权限。需要联系gerrit管理人员临时赋予你直接推送已有提交历史直接到gerrit仓库的权限。

## 后续

原有仓库可能中的目录请删除。

```
$ cd ~/sharedir/projects/documents
$ git rm -rf features/instrument
$ git commit -m "remove features/instrument for seperate repo"
```

然后在gerrit上合并该提交。

之后根据需要将独立出来的新仓库添加到你的repo工程的`manifests.xml`中。具体方法根据实际项目操作。

# 参考

- https://juejin.im/entry/586afb42ac502e006d81b1da