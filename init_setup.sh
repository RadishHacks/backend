#### DO NOT RUN THIS TWICE ####

echo "Running on:"
python3 --version

python3 -m venv backenv

echo "Activating new virtualenv..."
source backenv/bin/activate

pip install wheel
pip install -r requirements.txt

echo "Run source backenv/bin/activate to enter virtualenv"
echo "Installed packages:"
cat requirements.txt

