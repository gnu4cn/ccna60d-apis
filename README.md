# ccna60d-apis

## Changelog

_2019-11-24_

- 引入 `activated` 标志，解决`/v1/auth/register` API 未采用 Captcha 限制注册带来的滥用该接口的问题，未激活的注册用户无法登录，系统将定期清理未激活的注册用户
- 后期可采用图片验证方式，防止自动化注册或登录

_2019-11-23_

- 引入 Flask-Migrate 和 Flask-Script，使得数据模型的修改可以反应到数据库

