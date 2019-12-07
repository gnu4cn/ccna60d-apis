# ccna60d-apis

## Changelog

_2019-12-07_

- 籍由 `helpers.reqparse_helpers`，加入对注册、登录用户名、电子邮箱及密码的格式判断，不符合要求的拒绝注册与登录。

_2019-11-25_

- 去除 `activated` 属性，直接使用`user_role`属性判断注册用户是否已激活。`0 - 注册未激活`、`1-注册已激活`、`2-管理员`、`3-超级管理员`
- 使用`itsdangerous`库的`URLSafeTimedSerializer`生成激活链接
- 使用 Flask-Mail 发送激活邮件

_2019-11-24_

- 引入 `activated` 标志，解决`/v1/auth/register` API 未采用 Captcha 限制注册带来的滥用该接口的问题，未激活的注册用户无法登录，系统将定期清理未激活的注册用户。后期可采用图片验证方式，防止自动化注册或登录

- 加入 `lazy = true` 与 `lazy-apps = true` 到 `uwsgi.ini`，解决偶发的Postgresql `operationalError: SSL error`问题 

_2019-11-23_

- 引入 Flask-Migrate 和 Flask-Script，使得数据模型的修改可以反应到数据库

