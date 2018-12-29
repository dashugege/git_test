git init // 初始化仓库
git add . // 添加文件到缓冲区
git commit -m "first commit" // 把文件添加到本地仓库 及注释

// 把远程仓库和本地仓库进行连接
git remote add origin 远程地址

//推送到远程仓库
git push -u origin master
//以后用这个命令推送
git push origin master

git branch -r 或者git branch -a //查看远程分支
git branch <branchName> //创建分支
git checkout <branchName> //切换分支
git status //查看当前状态
git diff    // 查看文件变化
git log     //查看提交记录
git log --graph //查看分支合并图
git push origin <localBranchName>:<remoteBranchName> //将本地分支推送到远程仓库，并在远程仓库开了一个子分支
git branch -d <localBranch> //删除本地分支
git push origin --delete <remoteBranchName> //删除远程分支
git push origin :<remoteBranch> // 删除远程分支
git merge <remoteBranchName> // 把remoteBrancheName 分支合并到当前分支

// 拉取代码
git pull origin <branchName> //拉取指定分支代码
git pull --all     //拉取所有分支代码



adb 常见命令
adb devices , 获取设备列表及设备状态
adb get-state  获取设备的状态
adb kill-server , adb start-server , 结束 adb 服务， 启动 adb 服务
adb logcat , 打印 Android 的系统日志
adb install , 安装应用，覆盖安装是使用 -r 选项
adb uninstall , 卸载应用，后面跟的参数是应用的包名，请区别于 apk 文件名
adb pull sdcard/pull.txt d:\   Sdcard 下的 pull.txt 文件到 D 盘
adb push d:\push.txt sdcard/ 推送 D 盘下的 push.txt 至 Sdcard：
adb reboot , 重启 Android 设备

adb shell pm list package -s  列出系统应用
adb shell pm list package -3 列出第三方应用
adb shell pm list package -f 列出应用包名及其安装来源，结果显示例子：
adb shell pm path com.tencent.mobileqq  列出对应包名的 .apk 位置







