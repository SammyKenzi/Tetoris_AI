追加機能 <br>
<br>
1.0<br>
変更点<br>
・ブロックを4×4に修正<br>
・7種類のブロックを7個ごとにランダムに出るように修正（すべてが均等に来るようになった）<br>
・ブロックの修正に伴い、draw_block, 回転の関数を修正<br>

問題点<br>
・配置後のブロックに色がつかない　→　draw_blockを色を塗る関数にする　or　固定の関数を修正　or　新たに色を塗る関数を作成<br>
・回転して画面外に行くとout of range　→　画面を一回り大きくして壁を定義<br>
・長押しで移動できるようにしたい（最初は0.3秒間待つようにすると操作性向上）<br>
・ネクストの表示<br>
・ホールドの実装<br>
・スーパーローテーションシステムの実装<br>
・UIの改善<br>
<br>
AIに学習させるために、いくつかの方法を調べた<br>
・遺伝的アルゴリズム<br>
遺伝子をパラメータとして学習させる<br>
パラメータはスコアを伸ばすために考えられる評価要素の重みを表す<br>
<br>
追加<br>
・スコア計算（仮）、表示<br>
・消去ライン表示<br>
・遺伝的アルゴリズムの基本形の実装（まだ動かない）<br>
<br>
テトリス自体を完成させる（回転入れ以外はしっかりとできるように実装する）<br>
<br>

-----------------------------------------------------------------------------------
2.0<br>
テトリスのコードに全体的に問題があったため、１から作り直した。　　<br>
大まかな機能は実装できた　　<br>
　　<br>
未実装　　<br>
・Iミノのスーパーローテーション（問題あり）<br>　　
・ゲームオーバーの実装　　<br>
・ミノ接触から設置のラグの実装　　<br>
・Iミノの特定の回転でout of rangeになる（バグ）<br>　　
・落下地点の透明の表示が、ミノ本体よりも手前に表示される、重なると透明のほうが優先される　<br>　
・スコアの実装　　<br>

2.1　　<br>
AIがプレイするための機能はすべて実装できた<br> 
ここからAIの実装に入る<br>

------------------------------------------------------------------------------------
AIの実装<br>
・ニューラルネットワークと遺伝的アルゴリズムで学習させる<br>
ニューラルネットワークの説明　：　https://zenn.dev/nekoallergy/articles/ml-basic-nn01<br>
ニューラルネットワークの実装参考　：　https://atmarkit.itmedia.co.jp/ait/articles/2202/09/news027.html<br>
<br>
ニューラルネットワークの実装が完了<br>
遺伝的アルゴリズムで用いる遺伝子の値を明確化した<br>
・パラメータを適当にいじって出力をしてみたが、まったくできている感じがなかったので修正の必要がある可能性あり<br>
・ここからは遺伝的アルゴリズムの実装を行う<br>
遺伝的アルゴリズム実装参考　：　https://qiita.com/ksk001100/items/0f527a72270430017d8d<br>
<br><br>
3.0 update<br>
遺伝的アルゴリズムの実装を完了<br>
またそれに対応して、ニューラルネットワークを一部変更<br>
<br>
課題<br>
・繰り返しPygameを実行することができない<br>
　　runの引数がパラメータになっているため、毎回変更される→Pygameの中でループするとパラメータが変更できない<br>
  解決策<br>
  ・Pygameを何度でも実行できるような方法をさがす（楽）<br>
  ・runの引数を変更して大幅に全体を改良する（面倒）<br>
<br>
・外部情報を増やす<br>

-----------------------------------------------------------------------------------------
学習が行き詰ったので全体的に見直し
１．遺伝的アルゴリズム
　スコアの高さや、消したライン数などを適応度としていたが、AI同士の対戦を通じて適応度を与えることにする（最終的には対戦用のAIをつくるため）
　一つの個体につき1回の試行としていたが、ミノの変化により大きくスコアの差が出ていることが確認できたため試行回数を増やす
 選択、交叉の手法を変える。エリート選択かつランダム選択、一様交叉を用いる（遺伝子同士の比率がＡＩの強さに直結すると考えられるので、一点交叉か一様交叉が良いと思う）
２．ニューラルネットワーク（評価基準）
　評価基準を以下のようにする
 ・凸凹度
 ・凸凹の2乗
 ・状態の遷移数
 ・全体の高さ
 ・上半分の高さの和
 ・上1/4の高さの和
 ・穴の数
 ・穴の数の2乗
 ・穴のセル数
 ・穴のセル数の2乗
 ・オーバーハング（下段から上段がはみ出ている状態）
 ・オーバーハングの2乗
 ・溝の深さ（深いほど高評価、しかし制限超で低評価）
 ・溝の数
３．テトリス
　対戦できるよう、機能追加したものがbattle.py
 
