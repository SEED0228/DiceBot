# DiceBot

## このボットについて

このボットを導入することでdiscordチャットにコマンドを入力することで乱数を生成することができます。

## コマンド一覧

|コマンド名  |内容  |
|---|---|
|[/dice](#dice)  |1~6の間でランダムに値が出力されます  |
|[/gacha](#gacha)  |配列のうち1つの要素を返します  |

# dice

## /dice \<num\>
1~numの間でランダムに値が出力されます

## /dice \<num1\> \<num2\>
num1\~num2 or num2\~num1の間でランダムに値が出力されます

## /gacha \<文字列1\> \<文字列2\> ... \<文字列n\>
文字列1 ~文字列nのどれか1つが出力されます

## 実行方法

.envに[DISCORD_BOT_TOKEN](https://discordpy.readthedocs.io/ja/latest/discord.html)を記述する。

```
pipenv install
```

```
pipenv run python3 dicebot.py
```
