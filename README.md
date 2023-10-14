# 📁毎朝8時にAI関連記事をツイートしてくれるX(Twitter)bot🎉
# HOW TO GUIDE

# 1.ローカルで、Pythonを動かせるように仮想環境をアクティベート🖥
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2.ツイート機能が動くのかテスト（APIキーなどの環境変数は、ご自身で設定してください）🐦
cd src
python lambda_function.py

# 3.AWS Lambdaに関数を設定する

# 4.AWS EventBridgeで、定時ツイートを設定する