# AIコードレビュー実験：新人AIくん、レビューをお願いします

社内発表用のGitHub Pull Request実験です。

## 手順
1. このフォルダの内容を自分のGitHubリポジトリに追加する。
2. `src/pricing.py` のバグ入りコードをPRとして提出する。
3. 利用可能なAIレビュアーにレビューを依頼し、コメントを記録する。
4. 正常版 `src/pricing_clean.py` もレビューさせ、誤検知を確認する。
5. `experiment/scorecard.csv` に実際の結果を記録する。

## GitHubへ登録
新規リポジトリにこのフォルダの中身を置き、ローカルで以下を実行します。

```bash
git init
git add .
git commit -m "Add AI code review experiment"
git branch -M main
git remote add origin https://github.com/自分のアカウント/リポジトリ名.git
git push -u origin main
git checkout -b experiment/buggy-review
```

`src/pricing.py` は最初からバグ入りです。変更をコミットしてPushし、GitHubで `main` 向けPull Requestを作成します。PR上にAIレビュー機能が表示されない場合は、Copilotの契約・権限・リポジトリ設定を確認してください。

## テスト
Python 3.10以上を推奨します。

```bash
python -m unittest discover -s tests -v
```

テストは正常版を対象にしています。

## 注意
- AIの指摘は編集せず記録し、「正しい指摘」「誤検知」「見逃し」「修正案の正しさ」を人間が判定します。
- 実際の結果に合わせて発表し、検出結果を捏造しないでください。
- これは教育用の小さな例であり、実際の脆弱性検査や本番システムの安全性を保証しません。
- 会社のソースコードは社内ルールの確認なしに個人アカウントや外部AIへアップロードしないでください。
