cd ~/app/py/cardbox
rm -rf build/ dist/ cardbox.egg-info/
python3 setup.py sdist bdist_wheel
twine upload dist/* && rm -rf build/ dist/ cardbox.egg-info/
cd ..
