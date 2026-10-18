# QVD-2026-56312 POC
## 条件：JeecgBoot ≤ 3.9.3

JeecgBoot ≤ 3.9.3中有一条 `/**/*.js` 的放行规整
使得本身不能触碰到sql语句的请求可以进行sql语句拼接

使用方法:
```bash
python poc.py base_url
```

其中base_url是JeecgBoot的基址，不是网站基址，默认是网站基址+/jeecg-boot
例如：http://example.xom/jeecg-boot
如果改了context-path配置文件：
```yaml
server:
  servlet:
    context-path: /NewPath
```
那就base_url就是http://example.xom/NewPath
需要另行自己探测
成功应该响应：`"success":true,"message":"操作成功！"`  类似内容

ps:我手写的