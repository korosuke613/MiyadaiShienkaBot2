# MiyadaiShienkaBot2

[![Code Climate](https://codeclimate.com/github/korosuke613/MiyadaiShienkaBot2/badges/gpa.svg)](https://codeclimate.com/github/korosuke613/MiyadaiShienkaBot2)
[![Build Status](https://travis-ci.org/korosuke613/MiyadaiShienkaBot2.svg?branch=master)](https://travis-ci.org/korosuke613/MiyadaiShienkaBot2)
[![codecov](https://codecov.io/gh/korosuke613/MiyadaiShienkaBot2/branch/master/graph/badge.svg)](https://codecov.io/gh/korosuke613/MiyadaiShienkaBot2)
[![Coverage Status](https://coveralls.io/repos/github/korosuke613/MiyadaiShienkaBot2/badge.svg?branch=master)](https://coveralls.io/github/korosuke613/MiyadaiShienkaBot2?branch=master)
[![Requirements Status](https://requires.io/github/korosuke613/MiyadaiShienkaBot2/requirements.svg?branch=master)](https://requires.io/github/korosuke613/MiyadaiShienkaBot2/requirements/?branch=master)

宮大支援課お知らせBot2は[linebot-miyadai-shienka-news](https://github.com/korosuke613/linebot-miyadai-shienka-news "https://github.com/korosuke613/linebot-miyadai-shienka-news")の後継アプリです。

まだ開発中です。

## ルートの各ファイルの説明
### CI関連
| ファイル名 | 説明 |
|:-----------|:------------|
| .travis.yml | Travis CIの設定(CI) |
| .flake8 | Side CIの設定(コードレビュー) |
| pytest.ini | pytestの設定(テスト) |
| .coveralls.yml | Coverallsの設定(カバレッジ) |
| .gitignore | git ignoreの設定 |
| .gitmodules | git moduleの設定 |
| Doxyfile | Doxygenの設定(ドキュメント) |
| py_filter | Doxypypyの設定(ドキュメント) |

### デプロイ関連
| ファイル名 | 説明 |
|:-----------|:------------|
| requirements.txt | pip installの設定 |
| runtime.txt | Pythonのバージョン設定 |
| Procfile | Herokuの設定 |
