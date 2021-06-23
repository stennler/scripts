#!/bin/bash

# s         => git status --short
# s a       => adds all unstaged files
# s u       => unstages all staged files
# s r       => reverts all unstaged files
# s c       => comits all staged files
#
# s a 1 3   => add files 1 and 3; git add
# s u 1 3   => unstages files 1 and 3; git restore --staged
# s r 1 3   => reverts files 1 and 3; git restore

if [ $# -eq 0 ]; then
    git status --short | nl
elif [ "$1" == 'u' ]; then
    shift

    if [ $# -gt 0 ]; then
        while (( "$#" )); do
            line=$1
            file=$(git status --short | nl | awkc 3 | sed -n "$line p")

            echo "Unstaging file: $file"
            git restore --staged "$file"

            shift
        done
    else
        echo "Unstaging all staged files"
        git status --short | nl | awkc 3 | xargs git restore --staged
    fi

    echo ""
    git status --short | nl
elif [ "$1" == 'r' ]; then
    shift

    allChangedFiles=$(git status --short | nl | awkc 3)

    if [ $# -gt 0 ]; then 
        while (( "$#" )); do
            line=$1
            file=$(echo allChangedFiles | sed -n "$line p")

            echo "Reverting file: $file"
            git restore "$file"

            shift
        done
    else
        echo "Reverting all unstaged files"
        git status --short | nl | awkc 3 | xargs git restore
    fi

    echo ""
    git status --short | nl
elif [ "$1" == 'c' ]; then
    if [ $# -eq 2 ]; then
        git commit -m "$2"
    else
        git commit
    fi
else
    # a is default.
    if [ "$1" == 'a' ]; then
        shift
    fi

    if [ $# -gt 0 ]; then 
        while (( "$#" )); do
            line=$1
            file=$(git status --short | nl | awkc 3 | sed -n "$line p")

            echo "Adding file: $file"
            git add "$file"

            shift
        done
    else
        echo "Adding all files"
        git status --short | nl | awkc 3 | xargs git add
    fi

    echo ""
    git status --short | nl
fi