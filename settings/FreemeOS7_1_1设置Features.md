# FreemeOS 7.1.1 设置 Features

[TOC]

## WLAN


## 蓝牙
- 替换ICON
- 蓝牙连接亮屏
- 蓝牙状态/已开启/已关闭

## SIM卡
- 显示stk应用
- SIM卡 双卡时，切卡会更新首选SIM卡
- 双卡时开机，默认SIM卡1为主卡；SIM卡变动，默认唯一卡为主卡

## 流量使用情况
- 双卡时，显示默认SIM及对应SIM
- 隐藏数据流量开关
- 移动网络添加移动流量开关
- 双卡时，打开一张卡数据流量开关时，同时关闭另外一张
- 数据流量消耗详情布局问题

## 更多

## 主屏幕应用
- 默认launcher
- remove fallback home
- 隐藏主屏幕入口

## 显示
- 夜间显示优化
- 亮度条
- 永不休眠

## 声音
- 勿扰模式 短信拦截
- 双卡铃声
- 开关机铃声
- 音效改善隐藏

## 高级功能
- 翻转静音 添加闹钟静音

## 指纹
- 指纹入口切换
- 指纹扩展，应用
- 指纹扩展，指纹功能（桌面滑动等）
- 支持上一页
- 指纹安全，退出
- 前后指纹模组判断
- 录入指纹状态，禁止home键
- Reset lockout delayed task in need to enroll on
- Remove spans since of non-gms/gms caused exception.
- After finish enrolling, finish enroll setup wizard

## 帐号
- 过滤应用接口

## 应用
- can't disable security app

## 内存与存储
- summary
- 总存储格式化
- bugfix#19532, update storage entry 

## 电池
- 消耗电量显示作假
- 电量消耗详情ICON颜色

## 语言与输入法
- 虚拟键盘 summary显示当前虚拟键盘

## 安全
- 设备管理器布局优化
- 自启动流量管理入口切换/入口
- 隐藏位置来源开关
- for settings crash when pin is empty

## 开发者选项
- user版本 AEE/ANR弹窗

## 无障碍
- OneHand，放大手势冲突

## 关于手机
- 硬件版本号
- 移除自定义版本
- kernel版本号定制
- 基带版本号定制
- Freeme图标
- FreemeOS版号
- 分享FreemeOS接口
- 设备名称
- CPU信息（仅显示处理器信息）/支持客制化
- 运行内存
- 手机存储
- 手机屏幕
- MEID信息显示
- 系统更新入口切换

## FreemeUI适配
- switchBar样式
- FreemeTheme 界面字体大小/字体样式
- 主界面，第三方应用图标颜色
- remove Suggestions

## 修复BUG
- 7.1主界面加载慢
- we flash the wallpaper before SUW.
- 主界面加载时，隐藏几项