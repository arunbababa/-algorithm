# 配列に同じ文字が含まれているかを判定する

# step1 
'''
リニアスキャンで各配列要素をキーとしてハッシュマップへ追加していく
※1回のroop
'''

# step2 
'''
※ほんてゃstep逆だけどわかりやすさのために
追加前にそのkeyがすでにハッシュマップに無いか確認しあれば速攻return
'''

# step3
'''
簡単な例外処理を書く
要素数が1の時はないので即returnする
'''

# 実装

# 同じ文字が含まれているかもしれない配列
ram = 'sowjdonencmoo'
my_hash = {}
has_dup_char = '同じ文字があります'
has_not_dup_char = '同じ文字がありません'
hash_length = len(ram)

if hash_length <= 1:
  print(has_not_dup_char)

for i in ram:
  if i in my_hash:
    print(has_dup_char)
    break;
  my_hash[i] = 1