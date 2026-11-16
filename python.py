# %%
name = "yuuto"

print(name)

# %%
print("Hello, World!")

#%%
for i in range(1, 4):
    print(i, "番目のループです。")
#%%
for i in range(10):
    print(i)
#%%
sum = 0

for i in range(1, 100):
    sum += i
    if sum > 1000:
        break
print("合計が1000を超えるのは、1～", i, "を加算した時です。")

#%%

# ctrl + X + S セーブ
# ctrl + P 前の行へカーソル
# ctrl + N 次の行へカーソル
# ctrl + B 前の文字へカーソル
# ctrl + F 次の文字へカーソル
# ctrl + J 次の行作成
# ctrl + H 前の文字削除
# ctrl + D 次の文字削除
# ctrl + K カーソルの行削除
# ctrl + C コピー
# ctrl + shift + V ペースト
# ctrl + V ページ一番下にカーソル

#%%
x = 50
y = x
x -= 10

data1 = [10, 20, 30]
data2 = data1
data1[1] = 15

print(x, y, data1, data2)

#%%
# Gitコマンドまとめ
# git clone リモートリポジトリをローカルにコピー
# git status リポジトリの状態をチェック
# git add -A 作業エリアの変更をすべてステージ
# git add filename ファイルfilenameの変更をステージ
# git commit -m "Message" メッセージ"Message"を付けてコミット
# git commit コミット(メッセージはエディタで入力)
# git --set-upstream- to=origin/master ローカルと同期させるリモートを設定
# git push リモートをローカルに同期
# git pull ローカルをリモートに同期
# git reset ステージングエリアをコミットせずに破棄
# git reset --hard HEAD 作業エリアとステージングエリアをコミットせずに共に破棄
# git reset --soft HEAD^ コミット履歴だけ一つ前に戻す 
# git reset --mixed HEAD^ コミット履歴を一つ前に戻してステージングエリアもそれに合わせる
# git reset --hard HEAD^ コミット履歴を一つ前に戻して作業エリアとステージングエリアもそれに合わせる
# git log コミット履歴を閲覧する
