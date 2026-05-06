cd ~/git
git clone https://rweigel@github.com/rweigel/utilrsw
cd utilrsw
pip install -e .[scm]

scm-release --pypi-config-file ~/etc/pypirc --increment-version patch