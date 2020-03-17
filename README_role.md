# Apache v2.4 パラメータ生成ロール

## Description

本ロールでは、Apache v2.4 Linux版構築済み環境から設定情報を収集する機能と、収集した設定情報からApache Ver2.4 Linux版構築ロール(Apache_Ver2.4)で使用できるパラメータを生成する機能を提供します。
※パラメータ生成の時、「http.conf」から情報を採取する必要となります。設定項目名に対し、読み込む時大小文字を区別して処理します。

## Supports

本ロールは、以下環境をサポートします。

- 管理サーバー（Ansible実行サーバー）
  - OS：RHEL7.4（CentOS7.4）/RHEL8.0（CentOS8.0）
  - Ansible：Version 2.8
  - Python：2.7 or 3.6
- 対象サーバー
  - 利用しているロール、共通部品の仕様に準拠します。

## Dependencies

本ロールでは、以下のロール、共通部品を利用しています。

- 収集機能（Apache24_gathering_linux）
  - gathering ロール
- パラメータ生成機能（Apache24_extracting_linux）
  - パラメータ生成共通部品

## Role Variables

本ロールで指定できる変数値について説明します。

### Mandatory Variables

ロール利用時に必ず指定しなければならない変数値はありません。

### Optional Variables

ロール利用時に以下の変数値を指定することができます。

- 共通

    | Name                            | Default Value | Description                        |
    | ------------------------------- | ------------- | -----------------------------------|
    |`VAR_Apache_gathering_dest`      |'{{ playbook_dir }}/_gathered_data' |収集した設定情報の格納先パス |
    |`VAR_Apache_extracting_dest`     |'{{ playbook_dir }}/_parameters'    |生成したパラメータの出力先パス  |

- Apache24_extracting_linux

    | Name                             | Default Value                    | Description      |
    | -------------------------------- | -------------------------------- | -----------------|
    |`VAR_Apache_extracting_rolename`  |'Apache_setup'                    |パラメータ生成対象 (*1) |

(*1) 本変数値は収集・パラメータ生成時の識別子として使用するため、通常は変更しないでください。

## Results

本ロールの出力について説明します。

### 収集した設定情報の格納先

収集した設定情報は以下のディレクトリ配下に格納します。

- <VAR_Apache_gathering_dest>/<ホスト名/IP>/Apache24_gathering_linux/

本ロールを既定値で利用した場合、以下のように設定情報を格納します。
- Linux版 Apache Ver2.4 の場合

    ```none
    <Playbook実行ディレクトリ>/
      +-_gathered_data/
          +-<ホスト名/IP>/
              +-Apache24_gathering_linux/                      # 収集データ
                  +-files/
                        ：
    ```

### 生成したパラメータの出力例

生成したパラメータは以下のディレクトリ・ファイル名で出力します。

- <VAR_Apache_extracting_dest>/<ホスト名/IP>/<VAR_Apache_extracting_rolename>.yml

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- Apache Ver2.4 の場合

    ```none
    <Playbook実行ディレクトリ>/
      +-_parameters/
          +-<ホスト名/IP>/
			  +-Apache_setup.yml                 # パラメータ
    ```

## Usage

本ロールの利用例について説明します。

### 既定値で設定情報収集およびパラメータ生成を行う場合

以下の例では既定値で設定情報収集およびパラメータ生成を行います。
- `Apache_extracting.yml` (Linux版Apache Ver2.4用Playbook)

    ```yaml
    ---
    - hosts: LinuxGroup
      become: yes
      roles:
        - role: Apache24_gathering_linux
        - role: Apache24_extracting_linux
    ```

- 以下のように設定情報とパラメータを出力します。

    ```none
    <Playbook実行ディレクトリ>/
      +-_gathered_data/
      |   +-<ホスト名/IPアドレス>/
      |       +-Apache24_gathering_linux/              # 収集データ
      |           +-files/
      |               ：
      +-_parameters/
          +-<ホスト名/IPアドレス>/
			  +-Apache_setup.yml               # パラメータ
    ```

### パラメータ再利用

以下の例では、生成したパラメータを使用して構築済Apache Ver2.4の設定を変更します。

- `Apache_setup.yml`（Linux版Apache Ver2.4構築ロールを使用）

    ```yaml
    ---
    - hosts: Apache
      become: yes
      roles:
        - Apache_setup
    ```

- 生成したパラメータを指定してplaybookを実行

    ```sh
    ansible-playbook Apache_setup.yml -i hosts --extra-vars="@_parameters/<ホスト名/IPアドレス>/Apache_setup.yml"
    ```

# Copyright
Copyright (c) 2019 NEC Corporation

# Author Information
NEC Corporation
