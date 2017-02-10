#!/bin/bash

function checkargs() {
    local file=$1
    if [ ! -f "$file" ]; then
        echo "$file not exsited, you must create it with scandir.py"
        exit
    fi
}

action=$1

function _setupvar() {
    projects_file=project.list
    checkargs $projects_file
    git_lists=($(cat $projects_file))
    git_lists_num=${#git_lists[@]}
    git_location_lists=($(cat ${projects_file%.*}.gerrit))
    gerrituser=$(git config user.name)
}

function clone_manifests() {
    local src_base=$1
    local src_name=$2
    local new_base=$3
    local new_name=$4

    cp -frp $src_name $new_name

    find $new_name -name "*.xml" | xargs sed -i "{
    s/$src_base/$new_base/
    s/$src_name/$new_name/
    }"
}

#reference:
#  http://stackoverflow.com/questions/23929235/multi-line-string-with-extra-space-preserved-indentation
#  http://blog.csdn.net/shaobingj126/article/details/7395570
#  http://www.cnblogs.com/emanlee/p/3583769.html
#  http://www.1987.name/264.html

read -r -d '' commitmsg << EOM
[freemeos/create] init repo
EOM

function create_empty_gits() {
    for i in ${git_lists[*]}
    do 
        cd $i
        if [  -d ".git" ]; then
            echo "WARN: $i git repo already exsited!"
        else
            git init
            cp ~/Downloads/commit-msg .git/hooks/
            git commit --allow-empty -q -m "$commitmsg"
            echo "$i git init over"
        fi 
    done
}

read -r -d '' commitmsg2 << EOM
[freemeos/bringup] add init code
EOM

function add_code_gits() {
    for i in ${git_lists[*]}
    do 
        cd $i
        git add -f .
        git commit -q -m "$commitmsg2"
        echo "$i git add commit over"
    done
}

#gerrit_path="droi/freemeos/"
function create_gerrit_projects() {
    for g in ${git_location_lists[*]}
    do 
        ssh -p 29418 ${gerrituser}@10.20.40.19 gerrit create-project $gerrit_path$g.git
        echo "ssh -p 29418 ${gerrituser}@10.20.40.19 gerrit create-project $gerrit_path$g.git"
    done
}

function push_gerrit_projects() {
    #for i in ${git_lists[*]}
    for ((i=0;i<git_lists_num;i++))
    do 
        local p=${git_lists[$i]}
        local g=${git_location_lists[$i]}
        echo "cd $p"
        cd $p
        git remote add origin ssh://${gerrituser}@10.20.40.19:29418/$gerrit_path$g.git
        #git push origin HEAD:master
        git push origin HEAD:refs/for/master
    done
}

function review_gerrit_projects() {
    for ((i=0;i<git_lists_num;i++))
    do 
        local p=${git_lists[$i]}
        local g=${git_location_lists[$i]}
        cd $p
        echo "cd $p"
        #--verified +1
        local gitsha=($(git rev-list --reverse HEAD | tr -s "\n" " "))
        if [ "${#gitsha[@]}" -eq 0 ];then
            echo "reveiw $gerrit_path$g.git is empty"
            continue
        fi

        local l=1
        for c in ${gitsha[@]}; do
            echo "reveiw [$l] $gerrit_path$g.git $c"
            ssh -p 29418 ${gerrituser}@10.20.40.19 gerrit review --code-review +2 --submit --project $gerrit_path$g.git $c
            l=$(($l+1))
        done
    done
}

function wrapper() {
    local cmd=$1
    local log=$2
    echo "##### $2 start... ###"
    $cmd
    echo "##### $2 over ###"
}

function help() {
cat <<EOF
usage: creategit.sh <command> [<args>]
- clone: clone manifests to a new one, run in manifests git repo
    creategit.sh clone mt6580 ALPS-MP-N0.MP2-V1_DROI6580_WE_N mt6737 ALPS-MP-N0.MP1-V1.0.2_DROI6737M_65_N
- s0: diff xml with aosp directory and create helper files
    creategit.sh s0 manifests.xml
- s1: run step 1
    creategit.sh s1
- s2: run step 2
    creategit.sh s2
- s3: run step 3
    creategit.sh s3
- s4: run step 4
    creategit.sh s4
EOF
}

shift
case $action in
    help)
        help
        ;;
    clone)
        clone_manifests "$@"
        ;;
    s0|step0)
        _dirpath=$(dirname $0)
        scandir=${_dirpath:-"."}/scandir.py
        if [ ! -f "$scandir" ]; then
            echo "error: cannot find scandir.py"
            exit
        fi
        
        manifest=$1
        if [ ! -f "$manifest" ]; then
            echo "error: $manifest is not exsited!"
            exit
        fi

        wrapper "python $scandir -f $manifest $(pwd)" "diff xml with workplace"
        ;;
    s1|step1)
        _setupvar
        wrapper create_empty_gits "create local empty git repo"
        wrapper add_code_gits "add code to local git repo"
cat <<EOF
Now, you may fix the git repo which has sub git repos, such as "device/", run:
      git rm --cached sub-git-dir; echo "sub-git-dir/" >> .gitignore
      git add .gitignore
      git commit -m "[freeme] ignore xxx]
      git push origin HEAD:refs/for/master
EOF
        ;;
    s2|step2)
        _setupvar
        wrapper create_gerrit_projects "create gerrit projects"
        ;;
    s3|step3)
        _setupvar
        wrapper push_gerrit_projects "push to gerrit projects"
        ;;
    s4|step4)
        _setupvar
        wrapper review_gerrit_projects "review change in gerrit projects"
        ;;
    *)
        echo "fail: unknown subcommand!"
        ;;
esac
