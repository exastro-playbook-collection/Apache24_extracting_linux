# Apache パラメータ生成Role

## Trademarks

- Linuxは、Linus Torvalds氏の米国およびその他の国における登録商標または商標です。
- RedHat、RHEL、CentOSは、Red Hat, Inc.の米国およびその他の国における登録商標または商標です。
- Windows、PowerShellは、Microsoft Corporation の米国およびその他の国における登録商標または商標です。
- Ansibleは、Red Hat, Inc.の米国およびその他の国における登録商標または商標です。
- pythonは、Python Software Foundationの登録商標または商標です。
- Apacheは、Apache Software Foundationの登録商標または商標です。
- NECは、日本電気株式会社の登録商標または商標です。
- その他、本ロールのコード、ファイルに記載されている会社名および製品名は、各社の登録商標または商標です。

## Description
本Roleは、Apache構築済の実環境（サーバ）からソフトウェアの動作に必要となる設定情報を収集し、収集データからAnsible Playbookへ投入するパラメータ値（extra_vars）を生成します。

現在対象となる、ApacheのRoleは以下となります。
* Apache v2.4
  * Windows版
    * Apache_Ver2.4_windows2016
  * Linux版
    * Apache_Ver2.4

各ロールの説明はREADME_role.mdをご参照ください。

# Copyright
Copyright (c) 2019 NEC Corporation

# Author Information
NEC Corporation