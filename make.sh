
function make_readme(){
    echo "# CDN" >> "README.md"
    echo "" >> "README.md"
    echo "Github + jsDeliver + PicGo + Imagine" >> "README.md"
    echo "" >> "README.md"
    echo "## PicGo" >> "README.md"
    echo "" >> "README.md"
    echo "[PicGo下载](https://github.com/Molunerfinn/PicGo/releases)" >> "README.md"
    echo "" >> "README.md"
    echo "## Imagine" >> "README.md"
    echo "" >> "README.md"
    echo "[Imagine下载](https://github.com/meowtec/Imagine/releases)" >> "README.md"
    echo "" >> "README.md"
}

function push_to_github(){
    echo "Let's push repo to github!"
    git add .
    git commit -m "update"
    git push
    echo "successfully pushed to github!"
}

function export_file_path(){
    jslink="https://cdn.jsdelivr.net/gh/smithcloud/CDN"
    for file in `ls $1`; do
        ff=$1"/"$file
        if [ -d $ff ]; then
            export_file_path $ff
        else
            echo ${jslink}${ff:1} >> "README.md"
        fi
    done
}

function write_readme(){
    if [ -e "README.md" ]
    then
        rm -rf "README.md"
    fi
    make_readme
    echo "## jsDelivr链接" >> "README.md"
    echo "" >> "README.md"
    export_file_path .
}

write_readme
echo ""
push_to_github