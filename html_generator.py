import os
import glob


#スクリプトのパスを取得
base = os.path.dirname(os.path.abspath(__file__))
os.chdir(base)

#本文のパス
content_path = os.path.normpath(os.path.join(base, 'content/'))
content_lists = os.listdir(os.path.normpath(os.path.join(base, 'content')))

#テンプレート(ヘッダー、サイド、フッター)のパス
head_path = os.path.normpath(os.path.join(base, 'template/head.html'))
side_path = os.path.normpath(os.path.join(base, 'template/side.html'))
foot_path = os.path.normpath(os.path.join(base, 'template/foot.html'))

#出力先のパス
output_path = os.path.normpath(os.path.join(base, 'output/'))


#フォーマットを開く
head = open( head_path, 'r' )
side = open( side_path, 'r' )
foot = open( foot_path, 'r' )

#本文のファイル名のみを取得し、ループを回して記事を生成する
filename_list = [f for f in content_lists if os.path.isfile(os.path.join(content_path, f))]
for val in filename_list:

    #本文ファイルを開く
    os.chdir("./content")
    content = open( val, 'r' )
    os.chdir(base)  #書き込み処理のために親ディレクトリに戻る
    
    #結合のためバッファに格納
    headbuf = head.read()
    sidebuf = side.read()
    footbuf = foot.read()
    contentbuf = content.read()
    
    #結合
    outbuf = headbuf + sidebuf + contentbuf + footbuf
    
    #出力
    os.chdir("./output")
    fout = open( val, 'w' ) #吐き出すファイル名は入力と同じ
    fout.write(outbuf)
    fout.close()
    os.chdir(base)  #次周期のために親ディレクトリに戻る
