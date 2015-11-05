#!/bin/bash
cd ~/repos/vagrant/boxes/testv-dev;vagrant ssh -- -t "cd ~/repos/website && git status --short"
