
function push_to_github(){
    echo "Let's push repo to github!"
    git add .
    git commit -m "update"
    git push
    echo "successfully pushed to github!"
}

python ./scripts/build_directory_md.py &> DIRECTORY.md

if [[ $1 != "local" ]];then
    echo "Let's push to github!!"
    push_to_github
fi