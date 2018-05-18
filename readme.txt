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

// 拉取代码
git pull origin <branchName> //拉取指定分支代码
git pull --all     //拉取所有分支代码


//分支合并
git merge <branchName>  // 把branchName 和并到当前分支


