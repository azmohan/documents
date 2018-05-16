# GMS 基础知识

- GMS 全称为 Google Mobile Service，即谷歌移动服务。GMS 是 Google 开发并推动 Android 的动力，是 Google 提供的 Mobile Device 上的一系列应用服务。
- 目前提供的服务包括 Play Store, Gmail, YouTube, Chrome, Hangouts, Google+, Google Maps 等。

- 如果需要在 Device 上预置 GMS 应用，需要通过 Google 的认证，包括 CTS、GTS 测试以及 Google 自身的商务考量。

- 谷歌 GM 服务包括了搜索类、邮件服务类、联系人日历同步类、社交聊天类、地图导航类以及应用下载。可以说囊括了我们日常在手机上使用的几乎所有服务。由此可见，谷歌 GMS 服务是 Android 智能手机的核心。

- 虽然现在有大量的应用，具备GMS服务的功能，但作为谷歌原生的移动应用服务，GMS 预置的服务具有稳定性好、兼容性好以及更新及时的主要特点。

# GMS 认证

GMS 认证包括三个部分：CTS、GTS、CTS Verifier；Android 8.0 以后，增加了两个新的测试，分别是：VTS 测试 和 cts-on-gsi 。

## CTS

兼容性测试套件 ([CTS](https://source.android.com/compatibility/cts/)) 是一个免费的商业级测试套件，可在[此处下载](https://source.android.com/compatibility/cts/downloads)。CTS 代表兼容性的“机制”。

CTS 在桌面设备上运行，并直接在连接的设备或模拟器上执行测试用例。CTS 是一套单元测试，旨在集成到工程师构建设备的日常工作流程（例如通过连续构建系统）中。其目的是尽早发现不兼容性，并确保软件在整个开发过程中保持兼容性。

CTS 是一个自动化测试工具，其中包括两个主要软件组件：
- CTS tradefed 自动化测试框架会在桌面设备上运行，并管理测试执行情况。
- 单独的测试用例会在被测设备 (DUT) 上执行。测试用例采用 Java 语言编写为 JUnit 测试，并打包为 Android .apk 文件，以在实际目标设备上运行。


### 测试环境与工具

#### PC 端配置

注意：CTS 目前支持 64 位 Linux 和 Mac OS 主机。CTS 无法在 Windows 操作系统上运行。

##### ADB 和 AAPT

在运行 CTS 之前，请确保您已安装最新版本的 [Android 调试桥 (adb)](https://developer.android.com/studio/command-line/adb) 和 [Android 资源打包工具 (AAPT)](https://developer.android.com/guide/topics/manifest/uses-feature-element#testing)，并将这些工具的位置添加到计算机的系统路径中。

例如在 Ubuntu 中：

> export PATH=\$PATH:\$HOME/android-sdk-linux/build-tools/<version>:\$HOME/android-sdk-linux/platform-tools

如果在执行 cts-tradefed 时提示 adb 或者 aapt 找不到，请首先检查确认 adb 或者 aapt 是否正确配置 PATH，如果始终提示找不到，可按如下操作：
- sudo cp <sdk_home>/platform-tools/adb /usr/bin
- sudo cp <sdk_home>/build-tools/<version>/aapt /usr/bin
- sudo cp <sdk_home>/build-tools/<version>/lib64/libc++.so /usr/lib

然后重启再次执行。

##### Java 开发套件 (JDK)

安装正确版本的 Java 开发套件 (JDK)。对于 Android 7.0 以上

- 在 Ubuntu 上，使用 [OpenJDK 8](http://openjdk.java.net/install/)。
- 在 Mac OS 上，使用 [jdk 8u45 或更高版本](http://www.oracle.com/technetwork/java/javase/downloads/java-archive-javase8-2177648.html#jdk-8u45-oth-JPR)。

如需了解详情，请参阅 [JDK 要求](https://source.android.com/setup/requirements#jdk)。

##### CTS 文件

[下载](https://source.android.com/compatibility/cts/downloads)并打开与您设备的 Android 版本以及您的设备支持的所有应用二进制接口 (ABI) 相匹配的 CTS 包。本例中下载 Android 8.1 对应 最新的“android-cts-8.1_r4-linux_x86-arm”。

下载并打开最新版本的 [CTS 媒体文件](https://source.android.com/compatibility/cts/downloads#cts-media-files)。本例中下载最新的“android-cts-media-1.4”。

##### 设备检测

请按照相应的步骤[设置您的系统以检测设备](https://developer.android.com/studio/run/device#setting-up)，例如为 Ubuntu Linux 创建 udev 规则文件, 保证手机可以连接到测试的电脑.

#### Android 设备设置

兼容的设备被定义为具有 user/release-key 签名版本的设备，因此您的设备应运行基于[代号、标签和版本号](https://source.android.com/setup/build-numbers)中已知兼容的用户版本（Android 4.0 及更高版本）的系统镜像。

1. 确保 wifi 可访问 google 服务且稳定，设置 VPN，确保 IPV6 可用。（例如 Droi-test，密码：droitest，然后登陆验证即可）

2. 确保测试设备附近有可用的蓝牙设备。

3. 如果不是刚刷机或者恢复出厂设置的的手机，需要设置 Settings > Backup & reset > Factory data reset

4. 语言要设置为（美式）英语，Settings > Language & input > Language

5. 要打开位置，Settings > Location > On

6. Settings > Security > Screen lock > None

7. Settings > Developer options > USB debugging

8. Settings > Date & time > Use 24-hour format > Off

9. Settings > Developer options > Stay Awake > On

10. 如果设备具有存储卡插槽，请插入空的 SD 卡（CTS 可能会修改/清空插入设备的 SD 卡上的数据。）

11. 如果设备具有 SIM 卡插槽，请将激活的 SIM 卡插入每个插槽。如果设备支持短信，则应填充每个 SIM 卡的号码字段。 （一般最好使用联通卡测试，并插入卡槽一）

12. 保证手机 IMEI 号正确（例如测试用号：864471010000097）

13. 将 CTS 媒体文件复制到设备上，可以单独拷贝某个分辨率的

- 导航 (cd) 到下载并解压缩媒体文件的目录。
- 更改文件权限：chmod u+x copy_media.sh
- ./copy_media.sh

### 运行 CTS 测试

1. 解压缩 CTS 包（android-cts-8.1_r4-linux_x86-armz.zip）

2. 运行 cts-tradefed 脚本（例如 sudo ./android-cts/tools/cts-tradefed）来启动 CTS 控制台

3. 进入后可以执行“help”或者“run cts -–help”查看帮助命令

4. 启动默认测试计划（包含所有测试包）：run cts --plan CTS。这将启动测试兼容性所需的所有 CTS 测试。

对于 Android 7.0 或更高版本，使用的是 [CTS v2 控制台](https://source.android.com/compatibility/cts/run)

#### CTS v2 控制台命令参考

| 主机           | 说明                               |
|:--------------|:-----------------------------------|
| help          | 显示最常用命令的摘要               |
| help all      | 显示可用命令的完整列表             |
| version       | 显示版本。                         |
| exit          | 正常退出 CTS 控制台。所有当前正在运行的测试完成后，控制台将关闭。 |

| 运行                          | 说明                                       |
|:------------------------------|:-------------------------------------------|
| run cts | 运行默认的 CTS 计划（即完整的 CTS 调用）。<br/>在测试过程中，CTS 控制台可以接受其他命令。<br/>如果没有连接任何设备，CTS 台式机（或主机）将等待连接设备后再开始测试。<br/>如果连接了多台设备，则 CTS 主机将自动选择一台设备。| 
| --plan <test_plan_name> | 运行指定的测试计划。|
| --module/-m <test_module_name>  [--module/-m <test_module2>...] | 运行指定的测试模块。例如，run cts --module CtsGestureTestCases 会执行手势测试模块（该命令可以简化为 run cts -m Gesture）。<br/>run cts -m Gesture --test android.gesture.cts.GestureTest#testGetStrokes 会运行指定的包、类或测试。|
| --subplan <subplan_name> | 运行指定的子计划。|
| -- module/-m <test_module_name> -- test <test_name> | 运行指定的模块并进行测试。例如，run cts -m Gesture --test android.gesture.cts.GestureTest#testGetStrokes 会运行指定的包、类或测试。|
| --retry | 重新尝试运行在以前的会话中失败或未执行的所有测试。 使用 list results （l r） 获取会话 ID。 |
| --shards <number_of_shards>  | 将 CTS 运行分为指定数量的独立块，以便在多台设备上并行运行。|
| --serial/-s <deviceID> | 在特定设备上运行 CTS。|
| --include-filter <module_name>  [--include-filter <module2>...] | 仅使用指定的模块运行。|
| --exclude-filter <module_name>  [--exclude-filter <module2>...] | 运行时排除指定的模块。|
| --log-level-display/-l <log_level> | 以显示给 STDOUT 的最小指定日志级别运行。有效值：[VERBOSE, DEBUG, INFO, WARN, ERROR, ASSERT]。|
| --abi <abi_name> | 强制要求测试在给定的 ABI（32 或 64）上运行。默认情况下，CTS 会为设备支持的每个 ABI 运行一次测试。|
| --logcat、--bugreport 和 --screenshoot-on-failure | 显示更详尽的故障信息并帮助进行诊断。|
| --device-token | 指定具有给定令牌的给定设备，例如 --device-token 1a2b3c4d:sim-card.。|
| --skip-device-info | 跳过收集设备相关信息的过程。注意：运行 CTS 以寻求批准时，请勿使用此选项。 |
| --skip-preconditions | 绕过对设备配置的验证和设置，例如推送媒体文件或检查 WLAN 连接。 |

| 列表                          | 说明                                       |
|:------------------------------|:-------------------------------------------|
| list modules | 列出存储区中的所有可用测试模块。 |
| list plans 或 list configs | 列出存储区中的所有可用测试计划（配置）。 |
| list subplans | 列出存储区中的所有可用子计划。 |
| list invocations | 列出设备上当前正在执行的“运行”命令。 |
| list commands | 列出当前在队列中等待分配给设备的所有“运行”命令。 |
| list results | 列出当前存储在存储区中的 CTS 结果。 |
| list devices | 列出当前连接的设备及其状态。<br/>“可用”设备是可正常运行的空闲设备，可用于运行测试。<br/>“不可用”设备是可通过 adb 查看但不响应 adb 命令的设备，不会分配用于测试。<br/>“已分配”设备是当前正在运行测试的设备。 |

| 转储                          | 说明                                       |
|:------------------------------|:-------------------------------------------|
|dump logs | 为所有正在运行的调用转储 tradefed 日志。 |

| 添加                          | 说明                                       |
|:------------------------------|:-------------------------------------------|
| add subplan --name/-n <subplan_name> --result-type [pass \| fail \| timeout \| notExecuted] [--session/-s <session_id>] | 创建从上一会话衍生的子计划；此选项会生成可用于运行测试子集的子计划。<br/>唯一的必选项是 --session。其他选项都是可选的，但如果选用这些选项，必须后跟一个值。--result-type 选项可重复使用；例如 add subplan --session 0 --result-type passed --result-type failed 是有效的。|

例如：
- 执行整个CTS的测试
<br/> run cts --plan CTS

<br/> 如果多台手机一起跑测，可使用下面命令：
<br/> run cts --plan CTS --shards 2 -o -d --skip-system-status-check com.android.compatibility.common.tradefed.targetprep.NetworkConnectivityCheck

<br/> 注：-o = --skip-preconditions, -d =--skip-device-info, --skip-system-status-check com.android.compatibility.common.tradefed.targetprep.NetworkConnectivityChecker<br/> 则可以跳过网络连接检测，这样可以节省不少时间。
<br/> 如果是 64 位机器，则默认每个测试项会执行两遍（arm64-v8a 和 armeabi-v7a），也是很浪费时间，可使用“-a”或者“--abi”选择测试用例，例如：run cts --plan CTS -a armeabi-v7a

- CTS第一遍结束之后，会有很多没有执行的项，首先执行命令：l r
<br/> 根据 session-id，然后再执行：
<br/> run cts --retry <session-id> --retry-type NOT_EXECUTED

- 继续未完成的cts测试
<br/>执行l r 命令，锁定需要继续跑的 session_id：run cts --retry <session_id>

- 执行单独模块或者单独测试项
<br/> 测试单个模块：run cts -m <模块名>
<br/> 测试单个测试项: run cts -m <模块名> -t <test_name>, 如下失败项：

<br/> armeabi-v7a CtsAssistTestCases
| Test             | Result | Details                                        |
|:-----------------|:-------|:-----------------------------------------------|
|android.assist.cts.FlagSecureTest#testSecureActivity | fail | junit.framework.AssertionFailedError |

run cts -m CtsAssistTestCases -t android.assist.cts.FlagSecureTest#testSecureActivity

### 解读 CTS 结果

#### 测试报告

CTS 测试结果位于以下目录中（还有同名压缩包文件）：

$CTS_ROOT/android-cts/results/<start_time>

testResult.xml 文件会包含实际的结果。在浏览器（推荐使用火狐）中打开此文件，即可查看测试结果。

#### 测试 log

CTS 测试 log 位于以下目录中：

$CTS_ROOT/android-cts/logs/<start_time>

## GTS

CTS 测试的环境配置（PC 端与 Andorid 端）基本一致，只是不需要安装CTS media媒体包。

### 运行 GTS 测试

1. 解压缩 GTS 包（gts-5.1_r3-4604229.zip）

2. 运行 gts-tradefed 脚本（例如 sudo ./android-gts/tools/gts-tradefed）来启动 GTS 控制台

3. 进入后可以执行“help”或者“run gts --help”查看帮助命令

4. 启动默认测试计划（包含所有测试包）：run gts --plan GTS

GTS 测试与 CTS 测试命令形式基本一致，可通过“help”命令详细了解。它们的 results 和 logs 存放路径形式也基本一致，可参考 CTS 部分。


# 参考资料
- [兼容性测试套件](https://source.android.com/compatibility/cts/)
- [Android GMS认证](https://www.jianshu.com/c/149b71d69d47)
- [Android CTS test](https://onlinesso.mediatek.com/_layouts/15/mol/topic/ext/Topic.aspx?mappingid=06c6c44d-2ec6-423f-88c2-a036ba45a550)
- [GMS 快速入门](https://onlinesso.mediatek.com/_layouts/15/mol/topic/ext/Topic.aspx?mappingid=af056d4a-d117-4808-9663-b637e064547d)
