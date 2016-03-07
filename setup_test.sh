#!/bin/bash

# Intall dependence modules
pip install --upgrade -r requirements/test.txt

# Install loacal package
pushd Nurse_A
python setup.py sdist
python setup.py install

popd

# Run test scripts
#pushd Nurse_A/Script/Suites
#rm -rf ../reports/*
#python PR_R_A.py
pushd Nurse_A/Script/PR_Regression
xvfb-run python Test_chat.py Chat.test_urgent_send_quick_message
